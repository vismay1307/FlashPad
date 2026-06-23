from fastapi import APIRouter

router = APIRouter()

@router.get("/register")
def register():
    return {
        "message": "Auth Route Working"
    }