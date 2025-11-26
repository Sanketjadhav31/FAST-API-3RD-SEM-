from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class CommentBase(BaseModel):
    content: str = Field(min_length=1, max_length=1000)
    author: str = Field(min_length=1, max_length=100)

class CommentCreate(CommentBase):
    task_id: int

class CommentUpdate(BaseModel):
    content: Optional[str] = Field(None, min_length=1, max_length=1000)

class CommentRead(CommentBase):
    id: int
    task_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
