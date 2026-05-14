# app/models/task.py
# Interns/Users ke tasks — Manager assign karta hai

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey 
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    is_done = Column(Boolean, default=False)
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)  # User ID
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)  # Manager/Admin ID
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())











