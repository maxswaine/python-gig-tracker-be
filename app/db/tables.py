import uuid
from sqlalchemy import Column, String, Date, Boolean, ForeignKey, Table, Integer
from sqlalchemy.orm import relationship
from app.db.database import Base

GIG_ID_FOREIGN_KEY = "gigs.id"

# Many-to-many: Gigs ↔ Users
gig_attendees = Table(
    "gig_attendees",
    Base.metadata,
    Column("gig_id", String, ForeignKey(GIG_ID_FOREIGN_KEY), primary_key=True),
    Column("user_id", String, ForeignKey("users.id"), primary_key=True)
)

# Many-to-many: Festivals ↔ Users
festival_attendees = Table(
    "festival_attendees",
    Base.metadata,
    Column("festival_id", String, ForeignKey("festivals.id"), primary_key=True),
    Column("user_id", String, ForeignKey("users.id"), primary_key=True)
)

# Many-to-many: FestivalDays ↔ Artists
festival_day_artists = Table(
    "festival_day_artists",
    Base.metadata,
    Column("day_id", String, ForeignKey("festival_days.id"), primary_key=True),
    Column("artist_id", String, ForeignKey("artists.id"), primary_key=True)
)

# Many-to-many: Gigs ↔ Artists
gig_artists = Table(
    "gig_artists",
    Base.metadata,
    Column("gig_id", ForeignKey(GIG_ID_FOREIGN_KEY), primary_key=True),
    Column("artist_id", ForeignKey("artists.id"), primary_key=True)
)

class Gig(Base):
    __tablename__ = "gigs"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    venue = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    favourite = Column(Boolean, nullable=False)

    artists = relationship(
        "Artist",
        secondary=gig_artists,
        back_populates="gigs"
    )
    moments = relationship("Moment", back_populates="gig", cascade="all, delete-orphan")
    attendees = relationship("User", secondary=gig_attendees, back_populates="gigs")

class Moment(Base):
    __tablename__ = "moments"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    description = Column(String, nullable=False)
    gig_id = Column(String, ForeignKey(GIG_ID_FOREIGN_KEY))

    gig = relationship("Gig", back_populates="moments")

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    gigs = relationship("Gig", secondary=gig_attendees, back_populates="attendees")
    festivals = relationship("Festival", secondary=festival_attendees, back_populates="attendees")

class Festival(Base):
    __tablename__ = "festivals"
    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    festival_name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    location = Column(String, nullable=False)

    days = relationship("FestivalDay", back_populates="festival", cascade="all, delete-orphan")
    attendees = relationship("User", secondary=festival_attendees, back_populates="festivals")

class FestivalDay(Base):
    __tablename__ = "festival_days"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    day_number = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    festival_id = Column(String, ForeignKey("festivals.id"))

    festival = relationship("Festival", back_populates="days")
    artists = relationship(
        "Artist",
        secondary=festival_day_artists,
        back_populates="festival_days"
    )

class Artist(Base):
    __tablename__ = "artists"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False, unique=True)

    gigs = relationship(
        "Gig",
        secondary=gig_artists,
        back_populates="artists"
    )
    festival_days = relationship(
        "FestivalDay",
        secondary=festival_day_artists,
        back_populates="artists"
    )