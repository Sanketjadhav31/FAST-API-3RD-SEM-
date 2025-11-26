from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class LabelBase(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    color: str = Field(default="#808080", pattern="^#[0-9A-Fa-f]{6}$")

class LabelCreate(LabelBase):
    pass

class LabelUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    color: Optional[str] = Field(None, pattern="^#[0-9A-Fa-f]{6}$")

class LabelRead(LabelBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
