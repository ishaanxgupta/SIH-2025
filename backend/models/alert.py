from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from database.connection import Base

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    tourist_id = Column(Integer, ForeignKey("tourists.id"))
    alert_type = Column(String)  # "entered_risk_zone", "location_update", "check_in", "emergency"
    message = Column(String)
    severity = Column(String, default="low")  # low, medium, high, critical
    created_at = Column(DateTime, default=datetime.utcnow)
    is_resolved = Column(String, default="false")

class AlertCreate(BaseModel):
    tourist_id: int
    alert_type: str
    message: str
    severity: str = "low"

class AlertResponse(BaseModel):
    id: int
    tourist_id: int
    alert_type: str
    message: str
    severity: str
    created_at: datetime
    is_resolved: str
    
    class Config:
        from_attributes = True
