from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db.tables import Gig, Moment, User
from app.models.gig import GigCreate, GigRead
from app.models.moment import MomentRead, MomentsWrapper

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_gig(gig_id: str, db: Session = Depends(get_db)):
    print(Gig)
    gig = db.query(Gig).filter(Gig.id == gig_id).first()
    if not gig:
        raise HTTPException(status_code=404,
                            detail="Gig not found")
    return gig

# CREATE
@router.post("/", response_model=GigRead)
def create_gig(gig: GigCreate, db: Session = Depends(get_db)):
    db_gig = Gig(
        artist=gig.artist,
        venue=gig.venue,
        date=gig.date,
        location=gig.location,
        favourite=gig.favourite
    )
    db.add(db_gig)
    db.commit()
    db.refresh(db_gig)
    return db_gig

@router.post("/{gig_id}/moments/", response_model=list[MomentRead])
def add_moment_to_gig(
        gig_id: str,
        moments_wrapper: MomentsWrapper,
        db: Session = Depends(get_db)):
    gig = get_gig(gig_id, db)

    created_moments = []

    for moment in moments_wrapper.moments:
        db_moment = Moment(
            description=moment.description,
            gig_id=gig.id
        )
        db.add(db_moment)
        created_moments.append(db_moment)
    db.commit()
    for m in created_moments:
        db.refresh(m)

    return created_moments

@router.post("/{gig_id}/attendees/")
def add_users_to_gig(
        gig_id: str,
        attendee_ids: list[str],
        db: Session = Depends(get_db)
):
    gig = get_gig(gig_id, db)

    gig_attendants = []

    for attendee_id in attendee_ids:
        user = db.query(User).filter(attendee_id == User.id).first()
        if not user:
            raise HTTPException(status_code=404,
                                detail="User not found")
        db_user = User(
            user_id=user.id,
            gig_id=gig.id
        )
        db.add(db_user)
        gig_attendants.append(db_user)
    db.commit()
    for a in gig_attendants:
        db.refresh(a)
    return gig_attendants

# READ

@router.get("/{gig_id}", response_model=GigRead)
def get_singular_gig(
        gig_id: str,
        db: Session = Depends(get_db)
):
    return get_gig(gig_id, db)


# UPDATE

# DELETE





