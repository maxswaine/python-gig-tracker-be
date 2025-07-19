import uuid

from sqlalchemy import Column, String, Date, Boolean, ForeignKey, Table, Integer, JSON
from sqlalchemy.orm import relationship

from app.db.database import Base

# Many-to-many: Gigs ↔ Users
gig_attendees = Table(
    "gig_attendees",
    Base.metadata,
    Column("gig_id", ForeignKey("gigs.id")),
    Column("user_id", ForeignKey("users.id"))
)
# Many-to-many: Festivals ↔ Users (attendees at a whole festival)
festival_attendees = Table(
    "festival_attendees",
    Base.metadata,
    Column("festival_id", ForeignKey("festivals.id")),
    Column("user_id", ForeignKey("users.id"))
)

# Many-to-many: Days ↔ Artists
festival_day_artists = Table(
    "festival_day_artists",
    Base.metadata,
    Column("day_id", ForeignKey("festival_days.id")),
    Column("artist_name", String, nullable=False)  # Assuming artist as String for now
)

class Gig(Base):
    __tablename__ = "gigs"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    artist = Column(String, nullable=False)
    venue = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    favourite = Column(Boolean, nullable=False)

    moments = relationship("Moment", back_populates="gig", cascade="all, delete-orphan")
    gig_attendees = relationship("User", secondary=gig_attendees, back_populates="gigs")


class Moment(Base):
    __tablename__ = "moments"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    description = Column(String, nullable=False)
    gig_id = Column(String, ForeignKey("gigs.id"))

    gig = relationship("Gig", back_populates="moments")

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    gigs = relationship("Gig", secondary=gig_attendees, back_populates="gig_attendees")
    festivals = relationship("Festival", secondary=festival_attendees, back_populates="festival_attendees")
class Festival(Base):
    __tablename__ = "festivals"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    festival_name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    location = Column(String, nullable=False)

    days = relationship("FestivalDay", back_populates="festival")
    festival_attendees = relationship("User", secondary=festival_attendees, back_populates="festivals")


class FestivalDay(Base):
    __tablename__ = "festival_days"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    day_number = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    festival_id = Column(String, ForeignKey("festivals.id"))
    artists_seen = Column(JSON, nullable=False, default=list)

    festival = relationship("Festival", back_populates="days")
