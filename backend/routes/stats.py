from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.tourist import Tourist
from models.alert import Alert
from models.risk_zone import RiskZone
from database.connection import get_db

router = APIRouter(prefix="/api/stats", tags=["stats"])

@router.get("/")
def get_stats(db: Session = Depends(get_db)):
    total_tourists = db.query(Tourist).count()
    active_tourists = db.query(Tourist).filter(Tourist.status == "active").count()
    total_alerts = db.query(Alert).count()
    unresolved_alerts = db.query(Alert).filter(Alert.is_resolved == "false").count()
    risk_zones = db.query(RiskZone).count()
    
    return {
        "total_tourists": total_tourists,
        "active_tourists": active_tourists,
        "total_alerts": total_alerts,
        "unresolved_alerts": unresolved_alerts,
        "risk_zones": risk_zones
    }
