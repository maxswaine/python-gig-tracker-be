from pydantic import ConfigDict, BaseModel
from datetime import date

from app.models.artist import ArtistRead
from app.models.moment import MomentRead
from app.models.user import UserRead

class GigBase(BaseModel):
    artists: list[str]
    venue: str
    date: date
    location: str
    favourite: bool

class GigCreate(GigBase):
    pass

class GigRead(GigBase):
    id: str
    artists: list[ArtistRead] = []
    moments: list[MomentRead] = []
    attendees: list[UserRead] = []
    model_config = ConfigDict(from_attributes=True)