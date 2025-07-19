from __future__ import annotations
from pydantic import ConfigDict, BaseModel

class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: str
    username: str
    password: str

class UserCreate(BaseModel):
    pass

class UserRead(BaseModel):
    id: str
    username: str
    model_config = ConfigDict(from_attributes=True)
