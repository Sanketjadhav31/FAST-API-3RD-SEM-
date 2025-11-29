from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime, timezone

from app.database import get_session
from app.models import Task, TaskLabel, Label, ActivityLog
from app.schemas import TaskCreate, TaskUpdate, TaskRead, TaskReadWithRelations

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def log_activity(session: Session, task_id: int, action: str, description: str, performed_by: str = "system"):
    """Helper function to log task activities"""
    activity = ActivityLog(
        task_id=task_id,
        action=action,
        description=description,
        performed_by=performed_by
    )
    session.add(activity)

@router.post("/", response_model=TaskRead, status_code=201)
def create_task(task_data: TaskCreate, session: Session = Depends(get_session)):
    """Create a new task with optional labels"""
    # Create task
    task = Task(
        title=task_data.title,
        description=task_data.description,
        status=task_data.status,
        priority=task_data.priority,
        due_date=task_data.due_date
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    
    # Add labels if provided
    if task_data.label_ids:
        for label_id in task_data.label_ids:
            # Verify label exists
            label = session.get(Label, label_id)
            if not label:
                raise HTTPException(status_code=404, detail=f"Label with id {label_id} not found")
            
            task_label = TaskLabel(task_id=task.id, label_id=label_id)
            session.add(task_label)
        session.commit()
    
    # Log activity
    log_activity(session, task.id, "created", f"Task '{task.title}' created")
    session.commit()
    
    return task

@router.get("/", response_model=List[TaskRead])
def get_tasks(
    status: Optional[str] = Query(None, description="Filter by status"),
    priority: Optional[str] = Query(None, description="Filter by priority"),
    label_id: Optional[int] = Query(None, description="Filter by label ID"),
    sort_by: Optional[str] = Query("created_at", description="Sort by field (created_at, updated_at, due_date, priority, status, title)"),
    sort_order: Optional[str] = Query("desc", description="Sort order (asc or desc)"),
    skip: int = Query(0, ge=0, description="Number of records to skip (pagination)"),
    limit: int = Query(100, ge=1, le=100, description="Maximum number of records to return"),
    session: Session = Depends(get_session)
):
    """Get all tasks with optional filters, sorting, and pagination"""
    query = select(Task)
    
    # Apply filters
    if status:
        query = query.where(Task.status == status)
    if priority:
        query = query.where(Task.priority == priority)
    if label_id:
        # Join with task_labels to filter by label
        query = query.join(TaskLabel).where(TaskLabel.label_id == label_id)
    
    # Apply sorting
    sort_field = getattr(Task, sort_by, Task.created_at)
    if sort_order.lower() == "asc":
        query = query.order_by(sort_field.asc())
    else:
        query = query.order_by(sort_field.desc())
    
    # Apply pagination
    query = query.offset(skip).limit(limit)
    
    tasks = session.exec(query).all()
    return tasks

@router.get("/{task_id}", response_model=TaskReadWithRelations)
def get_task(task_id: int, session: Session = Depends(get_session)):
    """Get a single task with all relations (comments and labels)"""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Manually load labels through task_labels relationship
    labels = []
    for task_label in task.task_labels:
        labels.append(task_label.label)
    
    # Create response with relations
    task_dict = TaskRead.model_validate(task).model_dump()
    task_dict["comments"] = task.comments
    task_dict["labels"] = labels
    
    return task_dict

@router.patch("/{task_id}", response_model=TaskRead)
def update_task(task_id: int, task_data: TaskUpdate, session: Session = Depends(get_session)):
    """Update a task"""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Track changes for activity log
    changes = []
    
    # Update fields
    update_data = task_data.model_dump(exclude_unset=True)
    label_ids = update_data.pop("label_ids", None)
    
    for key, value in update_data.items():
        if value is not None:
            old_value = getattr(task, key)
            if old_value != value:
                setattr(task, key, value)
                changes.append(f"{key}: {old_value} → {value}")
    
    task.updated_at = datetime.now(timezone.utc)
    
    # Update labels if provided
    if label_ids is not None:
        # Remove existing labels
        for task_label in task.task_labels:
            session.delete(task_label)
        
        # Add new labels
        for label_id in label_ids:
            label = session.get(Label, label_id)
            if not label:
                raise HTTPException(status_code=404, detail=f"Label with id {label_id} not found")
            
            task_label = TaskLabel(task_id=task.id, label_id=label_id)
            session.add(task_label)
        changes.append("labels updated")
    
    session.add(task)
    session.commit()
    session.refresh(task)
    
    # Log activity
    if changes:
        log_activity(session, task.id, "updated", f"Task updated: {', '.join(changes)}")
        session.commit()
    
    return task

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    """Delete a task"""
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    session.delete(task)
    session.commit()
    
    return None
