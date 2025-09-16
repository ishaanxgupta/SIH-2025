from sqlalchemy.orm import sessionmaker
from database.connection import engine, Base
from models.tourist import Tourist
from models.alert import Alert
from models.risk_zone import RiskZone
from datetime import datetime, timedelta
import random

# Create tables first
Base.metadata.create_all(bind=engine)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Sample tourist data with coordinates from popular tourist destinations
sample_tourists = [
    {
        "name": "Alice Johnson",
        "email": "alice.johnson@email.com",
        "phone": "+1-555-0101",
        "latitude": 40.7589,
        "longitude": -73.9851,
        "status": "active",
        "emergency_contact": "+1-555-0102"
    },
    {
        "name": "Bob Smith",
        "email": "bob.smith@email.com",
        "phone": "+1-555-0201",
        "latitude": 51.5074,
        "longitude": -0.1278,
        "status": "active",
        "emergency_contact": "+1-555-0202"
    },
    {
        "name": "Carol Davis",
        "email": "carol.davis@email.com",
        "phone": "+1-555-0301",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "status": "active",
        "emergency_contact": "+1-555-0302"
    },
    {
        "name": "David Wilson",
        "email": "david.wilson@email.com",
        "phone": "+1-555-0401",
        "latitude": 35.6762,
        "longitude": 139.6503,
        "status": "active",
        "emergency_contact": "+1-555-0402"
    },
    {
        "name": "Eva Brown",
        "email": "eva.brown@email.com",
        "phone": "+1-555-0501",
        "latitude": -33.8688,
        "longitude": 151.2093,
        "status": "active",
        "emergency_contact": "+1-555-0502"
    },
    {
        "name": "Frank Miller",
        "email": "frank.miller@email.com",
        "phone": "+1-555-0601",
        "latitude": 25.7617,
        "longitude": -80.1918,
        "status": "active",
        "emergency_contact": "+1-555-0602"
    },
    {
        "name": "Grace Lee",
        "email": "grace.lee@email.com",
        "phone": "+1-555-0701",
        "latitude": 1.3521,
        "longitude": 103.8198,
        "status": "active",
        "emergency_contact": "+1-555-0702"
    },
    {
        "name": "Henry Taylor",
        "email": "henry.taylor@email.com",
        "phone": "+1-555-0801",
        "latitude": 55.7558,
        "longitude": 37.6176,
        "status": "active",
        "emergency_contact": "+1-555-0802"
    },
    {
        "name": "Iris Garcia",
        "email": "iris.garcia@email.com",
        "phone": "+1-555-0901",
        "latitude": 19.4326,
        "longitude": -99.1332,
        "status": "active",
        "emergency_contact": "+1-555-0902"
    },
    {
        "name": "Jack Anderson",
        "email": "jack.anderson@email.com",
        "phone": "+1-555-1001",
        "latitude": -22.9068,
        "longitude": -43.1729,
        "status": "active",
        "emergency_contact": "+1-555-1002"
    },
    {
        "name": "Kate Martinez",
        "email": "kate.martinez@email.com",
        "phone": "+1-555-1101",
        "latitude": 28.6139,
        "longitude": 77.2090,
        "status": "active",
        "emergency_contact": "+1-555-1102"
    },
    {
        "name": "Liam Thompson",
        "email": "liam.thompson@email.com",
        "phone": "+1-555-1201",
        "latitude": 37.7749,
        "longitude": -122.4194,
        "status": "active",
        "emergency_contact": "+1-555-1202"
    },
    {
        "name": "Maya Rodriguez",
        "email": "maya.rodriguez@email.com",
        "phone": "+1-555-1301",
        "latitude": 41.9028,
        "longitude": 12.4964,
        "status": "active",
        "emergency_contact": "+1-555-1302"
    },
    {
        "name": "Noah White",
        "email": "noah.white@email.com",
        "phone": "+1-555-1401",
        "latitude": 52.5200,
        "longitude": 13.4050,
        "status": "active",
        "emergency_contact": "+1-555-1402"
    },
    {
        "name": "Olivia Harris",
        "email": "olivia.harris@email.com",
        "phone": "+1-555-1501",
        "latitude": 35.6895,
        "longitude": 139.6917,
        "status": "active",
        "emergency_contact": "+1-555-1502"
    }
]

# Sample risk zones data
sample_risk_zones = [
    {
        "name": "High Crime Area - Downtown",
        "description": "Area with reported high crime rates, tourists should avoid at night",
        "latitude": 40.7589,
        "longitude": -73.9851,
        "radius": 2.0
    },
    {
        "name": "Construction Zone - Central Park",
        "description": "Active construction site with heavy machinery and potential hazards",
        "latitude": 40.7829,
        "longitude": -73.9654,
        "radius": 1.5
    },
    {
        "name": "Flood Risk Zone - Riverside",
        "description": "Area prone to flooding during heavy rains",
        "latitude": 40.7505,
        "longitude": -73.9934,
        "radius": 3.0
    }
]

# Sample alert data
alert_types = ["entered_risk_zone", "location_update", "check_in", "emergency"]
severities = ["low", "medium", "high", "critical"]

def seed_database():
    # Clear existing data
    db.query(Alert).delete()
    db.query(Tourist).delete()
    db.query(RiskZone).delete()
    db.commit()
    
    # Add tourists
    for tourist_data in sample_tourists:
        tourist = Tourist(**tourist_data)
        db.add(tourist)
    
    # Add risk zones
    for risk_zone_data in sample_risk_zones:
        risk_zone = RiskZone(**risk_zone_data)
        db.add(risk_zone)
    
    db.commit()
    
    # Get tourist IDs for alerts
    tourists = db.query(Tourist).all()
    
    # Add sample alerts
    for i in range(20):
        tourist = random.choice(tourists)
        alert = Alert(
            tourist_id=tourist.id,
            alert_type=random.choice(alert_types),
            message=f"Sample alert message {i+1}",
            severity=random.choice(severities),
            created_at=datetime.utcnow() - timedelta(hours=random.randint(0, 72)),
            is_resolved="false" if random.random() > 0.3 else "true"
        )
        db.add(alert)
    
    db.commit()
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
