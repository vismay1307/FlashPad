from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(
    title="FlashPad API",
    version="1.0.0"
)

app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message": "FlashPad Running"
    }