from fastapi import FastAPI
from app.api.v1.router import api_router
from app.db.database import Base, engine

import app.models.note
app = FastAPI(
    title="FlashPad API",
    version="1.0.0"
)
Base.metadata.create_all(bind=engine)
app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "FlashPad Running"
    }