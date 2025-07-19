from datetime import date

from pydantic import ConfigDict, BaseModel

from app.models.day import DayRead
from app.models.user import UserRead


class FestivalBase(BaseModel):
    festival_name: str
    start_date:date
    end_date: date
    location: str

class FestivalCreate(FestivalBase):
    pass

class FestivalRead(FestivalBase):
    id: str
    days: list[DayRead] = []
    attendees: list[UserRead] = []
    model_config = ConfigDict(from_attributes=True)


