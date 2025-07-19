from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy import null
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db.tables import Festival, FestivalDay
from app.models.festival import FestivalRead, FestivalCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=FestivalRead)
def create_festival(festival: FestivalCreate, db: Session = Depends(get_db)):
    db_festival = Festival(
        festival_name = festival.festival_name,
        start_date = festival.start_date,
        end_date = festival.end_date,
        location = festival.location
    )
    db.add(db_festival)
    db.commit()
    db.refresh(db_festival)

    no_of_days = festival.start_date - festival.end_date

    days = []

    for x in range(no_of_days):
        festival_day_date = festival.start_date + x - 1
        db_day = FestivalDay(
            day_number = x,
            date = festival_day_date,
            festival_id = db_festival.festival_id,
            artists_seen = null
        )
        db.add(db_day)
        days.append(db_day)
    db.commit()
    for day in days:
        db.refresh(day)
    return festival

