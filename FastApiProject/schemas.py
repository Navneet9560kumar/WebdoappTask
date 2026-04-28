# Pydantic schemas for request and response validation in FastAPI.


from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# Request body - user create karte waqt
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

# Request body - user update karte waqt
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None

# Response body - ye return hoga API se
class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True