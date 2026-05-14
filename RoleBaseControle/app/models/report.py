# app/models/report.py
# Manager ki reports — Admin dekh sakta hai

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.base import Base

class Report(Base):
    __tablename__ = "reports"

    id  = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title= Column(String(200), nullable=False)
    content  = Column(String(2000), nullable=True)
    created_by  = Column(Integer, ForeignKey("users.id"), nullable=False)  # Manager/Admin
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
    updated_at  = Column(DateTime(timezone=True), onupdate=func.now())
