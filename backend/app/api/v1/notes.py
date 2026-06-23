from fastapi import APIRouter
from app.schemas.note import NoteCreate
router = APIRouter()

@router.get("/")
def get_notes():
    return {
        "message": "Notes Route Working"
    }

@router.post("/")
def create_note(note: NoteCreate):
    return {
        "received": note
    }