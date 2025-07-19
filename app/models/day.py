from pydantic import BaseModel
from datetime import date


class DayBase(BaseModel):
    day_number: int
    date: date
    artists_seen: list[str]

class DayCreate(DayBase):
    pass

class DayRead(DayBase):
    id: str

