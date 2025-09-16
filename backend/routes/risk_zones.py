from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from models.risk_zone import RiskZone
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter(prefix="/api/risk-zones", tags=["risk-zones"])

class RiskZoneCreate(BaseModel):
    name: str
    description: Optional[str] = None
    latitude: float
    longitude: float
    radius: float

class RiskZoneUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    radius: Optional[float] = None

@router.get("/", response_model=List[dict])
def get_risk_zones(db: Session = Depends(get_db)):
    """Get all risk zones"""
    risk_zones = db.query(RiskZone).all()
    return [risk_zone.to_dict() for risk_zone in risk_zones]

@router.get("/{risk_zone_id}", response_model=dict)
def get_risk_zone(risk_zone_id: int, db: Session = Depends(get_db)):
    """Get a specific risk zone by ID"""
    risk_zone = db.query(RiskZone).filter(RiskZone.id == risk_zone_id).first()
    if not risk_zone:
        raise HTTPException(status_code=404, detail="Risk zone not found")
    return risk_zone.to_dict()

@router.post("/", response_model=dict)
def create_risk_zone(risk_zone: RiskZoneCreate, db: Session = Depends(get_db)):
    """Create a new risk zone"""
    db_risk_zone = RiskZone(
        name=risk_zone.name,
        description=risk_zone.description,
        latitude=risk_zone.latitude,
        longitude=risk_zone.longitude,
        radius=risk_zone.radius
    )
    db.add(db_risk_zone)
    db.commit()
    db.refresh(db_risk_zone)
    return db_risk_zone.to_dict()

@router.put("/{risk_zone_id}", response_model=dict)
def update_risk_zone(risk_zone_id: int, risk_zone: RiskZoneUpdate, db: Session = Depends(get_db)):
    """Update a risk zone"""
    db_risk_zone = db.query(RiskZone).filter(RiskZone.id == risk_zone_id).first()
    if not db_risk_zone:
        raise HTTPException(status_code=404, detail="Risk zone not found")
    
    update_data = risk_zone.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_risk_zone, field, value)
    
    db.commit()
    db.refresh(db_risk_zone)
    return db_risk_zone.to_dict()

@router.delete("/{risk_zone_id}")
def delete_risk_zone(risk_zone_id: int, db: Session = Depends(get_db)):
    """Delete a risk zone"""
    db_risk_zone = db.query(RiskZone).filter(RiskZone.id == risk_zone_id).first()
    if not db_risk_zone:
        raise HTTPException(status_code=404, detail="Risk zone not found")
    
    db.delete(db_risk_zone)
    db.commit()
    return {"message": "Risk zone deleted successfully"}
