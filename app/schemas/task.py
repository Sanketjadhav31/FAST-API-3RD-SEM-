from pydantic import BaseModel, Field
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime
from app.models.task import TaskStatus, TaskPriority

if TYPE_CHECKING:
    from app.schemas.comment import CommentRead
    from app.schemas.label import LabelRead

class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    label_ids: Optional[List[int]] = []

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None
    label_ids: Optional[List[int]] = None

class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class TaskReadWithRelations(TaskRead):
    comments: List["CommentRead"] = []
    labels: List["LabelRead"] = []
    
    class Config:
        from_attributes = True
