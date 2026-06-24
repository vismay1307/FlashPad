from fastapi import APIRouter
from app.schemas.note import NoteCreate,NoteResponse

from fastapi import status
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

@router.post(
    "/",
    response_model=NoteResponse,
    status_code=status.HTTP_201_CREATED
)
def create_note(note: NoteCreate):
    return {
        "id": 1,
        "title": note.title,
        "content": note.content
    }