# Pydantic schemas = API ke request aur response ka format
# UserCreate  → user banate waqt kya bhejega client
# UserUpdate  → update karte waqt kya bhejega
# UserResponse → API kya wapas dega

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True  # SQLAlchemy object ko Pydantic mein convert karta hai