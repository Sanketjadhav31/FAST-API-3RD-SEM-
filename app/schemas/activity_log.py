from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ActivityLogRead(BaseModel):
    id: int
    task_id: int
    action: str
    description: str
    performed_by: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
