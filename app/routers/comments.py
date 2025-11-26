from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from datetime import datetime

from app.database import get_session
from app.models import Comment, Task, ActivityLog
from app.schemas import CommentCreate, CommentUpdate, CommentRead

router = APIRouter(prefix="/comments", tags=["Comments"])

def log_activity(session: Session, task_id: int, action: str, description: str, performed_by: str = "system"):
    """Helper function to log task activities"""
    activity = ActivityLog(
        task_id=task_id,
        action=action,
        description=description,
        performed_by=performed_by
    )
    session.add(activity)

@router.post("/", response_model=CommentRead, status_code=201)
def create_comment(comment_data: CommentCreate, session: Session = Depends(get_session)):
    """Create a new comment on a task"""
    # Verify task exists
    task = session.get(Task, comment_data.task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Create comment
    comment = Comment(
        content=comment_data.content,
        author=comment_data.author,
        task_id=comment_data.task_id
    )
    session.add(comment)
    session.commit()
    session.refresh(comment)
    
    # Log activity
    log_activity(session, task.id, "comment_added", f"Comment added by {comment.author}")
    session.commit()
    
    return comment

@router.get("/", response_model=List[CommentRead])
def get_comments(task_id: int = None, session: Session = Depends(get_session)):
    """Get all comments, optionally filtered by task_id"""
    query = select(Comment)
    
    if task_id:
        query = query.where(Comment.task_id == task_id)
    
    comments = session.exec(query).all()
    return comments

@router.get("/{comment_id}", response_model=CommentRead)
def get_comment(comment_id: int, session: Session = Depends(get_session)):
    """Get a single comment by ID"""
    comment = session.get(Comment, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    return comment

@router.patch("/{comment_id}", response_model=CommentRead)
def update_comment(comment_id: int, comment_data: CommentUpdate, session: Session = Depends(get_session)):
    """Update a comment"""
    comment = session.get(Comment, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    # Update fields
    update_data = comment_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        if value is not None:
            setattr(comment, key, value)
    
    comment.updated_at = datetime.utcnow()
    
    session.add(comment)
    session.commit()
    session.refresh(comment)
    
    # Log activity
    log_activity(session, comment.task_id, "comment_updated", f"Comment updated by {comment.author}")
    session.commit()
    
    return comment

@router.delete("/{comment_id}", status_code=204)
def delete_comment(comment_id: int, session: Session = Depends(get_session)):
    """Delete a comment"""
    comment = session.get(Comment, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    
    task_id = comment.task_id
    author = comment.author
    
    session.delete(comment)
    session.commit()
    
    # Log activity
    log_activity(session, task_id, "comment_deleted", f"Comment deleted by {author}")
    session.commit()
    
    return None
