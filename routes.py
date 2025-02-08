
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return {"users": ["user1", "user2", "user3"]}

@router.post("/trade")
def trade():
    return {"status": "Trade executed successfully"}
