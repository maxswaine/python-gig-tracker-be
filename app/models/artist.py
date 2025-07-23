from pydantic import BaseModel, ConfigDict


class ArtistBase(BaseModel):
    name: str

class ArtistCreate(ArtistBase):
    pass

class ArtistRead(ArtistBase):
    id: str
    model_config = ConfigDict(from_attributes=True)