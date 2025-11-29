from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from typing import List, Optional

from app.database import get_session
from app.models import ActivityLog, Task
from app.schemas import ActivityLogRead

router = APIRouter(prefix="/activity-logs", tags=["Activity Logs"])

@router.get("/", response_model=List[ActivityLogRead])
def get_activity_logs(
    task_id: Optional[int] = Query(None, description="Filter by task ID"),
    action: Optional[str] = Query(None, description="Filter by action type"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(50, ge=1, le=100, description="Maximum number of records"),
    session: Session = Depends(get_session)
):
    """Get activity logs with optional filters and pagination"""
    query = select(ActivityLog)
    
    # Apply filters
    if task_id:
        query = query.where(ActivityLog.task_id == task_id)
    if action:
        query = query.where(ActivityLog.action == action)
    
    # Sort by most recent first
    query = query.order_by(ActivityLog.created_at.desc())
    
    # Apply pagination
    query = query.offset(skip).limit(limit)
    
    logs = session.exec(query).all()
    return logs

@router.get("/{log_id}", response_model=ActivityLogRead)
def get_activity_log(log_id: int, session: Session = Depends(get_session)):
    """Get a single activity log by ID"""
    log = session.get(ActivityLog, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Activity log not found")
    
    return log

@router.get("/task/{task_id}", response_model=List[ActivityLogRead])
def get_task_activity_logs(
    task_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    session: Session = Depends(get_session)
):
    """Get all activity logs for a specific task"""
    # Verify task exists
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    query = select(ActivityLog).where(ActivityLog.task_id == task_id)
    query = query.order_by(ActivityLog.created_at.desc())
    query = query.offset(skip).limit(limit)
    
    logs = session.exec(query).all()
    return logs
