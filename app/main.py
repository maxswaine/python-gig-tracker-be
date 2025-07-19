from fastapi import FastAPI

from app.api import gigs, users, moments, festivals
from app.db import tables
from app.db.database import engine

tables.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(gigs.router, prefix="/gigs", tags=["gigs"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(moments.router, prefix="/moments", tags=["moments"])
app.include_router(festivals.router, prefix="/festivals", tags=["festivals"])


@app.get("/")
def read_root():
    return {"message": "Welcome to GigTracker API"}

