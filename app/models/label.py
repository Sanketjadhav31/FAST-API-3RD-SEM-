from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.task import Task

class Label(SQLModel, table=True):
    __tablename__ = "labels"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True, max_length=50)
    color: str = Field(default="#808080", max_length=7)
    
    # Relationships
    task_labels: List["TaskLabel"] = Relationship(back_populates="label")

class TaskLabel(SQLModel, table=True):
    __tablename__ = "task_labels"
    
    task_id: int = Field(foreign_key="tasks.id", primary_key=True)
    label_id: int = Field(foreign_key="labels.id", primary_key=True)
    
    # Relationships
    task: "Task" = Relationship(back_populates="task_labels")
    label: Label = Relationship(back_populates="task_labels")
