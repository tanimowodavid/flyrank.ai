from pydantic import BaseModel, Field
from typing import Optional

# Base properties shared across schemas
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, examples=["Finish FlyRank Assignment"])
    done: bool = Field(default=False)

# Schema for creating a task (input payload)
class TaskCreate(TaskBase):
    pass

# Schema for updating a task
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    done: Optional[bool] = None

# Schema for returning a task (response)
class TaskResponse(TaskBase):
    id: int

    class Config:
        from_attributes = True