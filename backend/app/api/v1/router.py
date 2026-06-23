from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.notes import router as notes_router

api_router = APIRouter()

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)

api_router.include_router(
    notes_router,
    prefix="/notes",
    tags=["Notes"]
)