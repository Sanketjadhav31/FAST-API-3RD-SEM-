from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.models.task import Task

class ActivityLog(SQLModel, table=True):
    __tablename__ = "activity_logs"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int = Field(foreign_key="tasks.id", index=True)
    action: str = Field(max_length=50)
    description: str = Field(max_length=500)
    performed_by: str = Field(max_length=100)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Relationships
    task: "Task" = Relationship(back_populates="activity_logs")
