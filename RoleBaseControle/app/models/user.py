# User table — role field isme hai jo RBAC ke liye use hoti hai

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum as SAEnum
from sqlalchemy.sql import func
from app.db.session import Base
from app.config.roles import Role


class User(Base):
      __tablename__ = "users"
      id= Column(Integer,primaryKey=True,index=True, autoincrement=True)
      name = Column(String(100),nullable=False)
      email = Column(String(100),unique=True,index=True,nullable=False)
      password =Column(String(255),nullable=False)
      role = Column(SAEnum(Role), default=Role.USER, nullable=False)# RBAC role
      is_active = Column(Boolean, default=True)
      created_at = Column(DateTime(timezone=True), server_default=func.now())
      updated_at = Column(DateTime(timezone=True), onupdate=func.now())
