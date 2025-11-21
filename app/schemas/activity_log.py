from pydantic import BaseModel
from datetime import datetime

class ActivityLogRead(BaseModel):
    id: int
    task_id: int
    action: str
    description: str
    performed_by: str
    created_at: datetime
    
    class Config:
        from_attributes = True
