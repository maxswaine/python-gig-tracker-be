from pydantic import ConfigDict, BaseModel

class MomentBase(BaseModel):
    description: str

class MomentCreate(MomentBase):
    pass

class MomentRead(MomentBase):
    id: str
    description: str

class MomentsWrapper(BaseModel):
    moments: list[MomentCreate]
    model_config = ConfigDict(from_attributes=True)