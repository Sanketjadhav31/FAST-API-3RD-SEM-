from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from enum import Enum

if TYPE_CHECKING:
    from app.models.comment import Comment
    from app.models.label import TaskLabel
    from app.models.activity_log import ActivityLog

class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Task(SQLModel, table=True):
    __tablename__ = "tasks"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True, max_length=200)
    description: Optional[str] = None
    status: TaskStatus = Field(default=TaskStatus.TODO, index=True)
    priority: TaskPriority = Field(default=TaskPriority.MEDIUM, index=True)
    due_date: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    comments: List["Comment"] = Relationship(back_populates="task", cascade_delete=True)
    task_labels: List["TaskLabel"] = Relationship(back_populates="task", cascade_delete=True)
    activity_logs: List["ActivityLog"] = Relationship(back_populates="task", cascade_delete=True)
