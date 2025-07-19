from pydantic import ConfigDict, BaseModel
from datetime import date

from app.models.moment import MomentRead
from app.models.user import UserRead

class GigBase(BaseModel):
    artist: str
    venue: str
    date: date
    location: str
    favourite: bool

class GigCreate(GigBase):
    pass

class GigRead(GigBase):
    id: str
    moments: list[MomentRead] = []
    attendees: list[UserRead] = []
    model_config = ConfigDict(from_attributes=True)