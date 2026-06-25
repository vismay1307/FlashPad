from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.note import Note
from app.schemas.note import NoteCreate, NoteResponse
router = APIRouter()

@router.get("/")
def get_notes():
    return {
        "message": "Notes Route Working"
    }

@router.post(
    "/",
    response_model=NoteResponse,
    status_code=status.HTTP_201_CREATED
)
def create_note(
    note: NoteCreate,
    db: Session = Depends(get_db)
):
    db_note = Note(
        title=note.title,
        content=note.content
    )

    db.add(db_note)

    db.commit()

    db.refresh(db_note)

    return db_note

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