from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from models.tourist import Tourist, TouristCreate, TouristResponse, TouristUpdate
from database.connection import get_db

router = APIRouter(prefix="/api/tourists", tags=["tourists"])

@router.get("/", response_model=List[TouristResponse])
def get_tourists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tourists = db.query(Tourist).offset(skip).limit(limit).all()
    return tourists

@router.get("/{tourist_id}", response_model=TouristResponse)
def get_tourist(tourist_id: int, db: Session = Depends(get_db)):
    tourist = db.query(Tourist).filter(Tourist.id == tourist_id).first()
    if tourist is None:
        raise HTTPException(status_code=404, detail="Tourist not found")
    return tourist

@router.post("/", response_model=TouristResponse)
def create_tourist(tourist: TouristCreate, db: Session = Depends(get_db)):
    db_tourist = Tourist(**tourist.dict())
    db.add(db_tourist)
    db.commit()
    db.refresh(db_tourist)
    return db_tourist

@router.put("/{tourist_id}", response_model=TouristResponse)
def update_tourist(tourist_id: int, tourist: TouristUpdate, db: Session = Depends(get_db)):
    db_tourist = db.query(Tourist).filter(Tourist.id == tourist_id).first()
    if db_tourist is None:
        raise HTTPException(status_code=404, detail="Tourist not found")
    
    update_data = tourist.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_tourist, field, value)
    
    db.commit()
    db.refresh(db_tourist)
    return db_tourist

@router.delete("/{tourist_id}")
def delete_tourist(tourist_id: int, db: Session = Depends(get_db)):
    db_tourist = db.query(Tourist).filter(Tourist.id == tourist_id).first()
    if db_tourist is None:
        raise HTTPException(status_code=404, detail="Tourist not found")
    
    db.delete(db_tourist)
    db.commit()
    return {"message": "Tourist deleted successfully"}
