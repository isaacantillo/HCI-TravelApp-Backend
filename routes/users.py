from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from database import firestore_manager
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

class User(BaseModel):
    username: str
    email: str
    phone: str
    name: str
    last_name: str
    origin: str
    travel_mode: List[str]


@router.get("/", response_model=List[User])
async def get_users():
    return await firestore_manager.get_all_users()

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    return await firestore_manager.get_user(user_id)

@router.post("/", response_model=User)
async def create_user(user: User):
    return await firestore_manager.create_user(user.model_dump())

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    return await firestore_manager.update_user(user_id, user.model_dump())

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return await firestore_manager.delete_user(user_id)
