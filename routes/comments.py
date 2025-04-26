from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

class Comment(BaseModel):
    id: int
    content: str
    user_id: int
    post_id: int

# In-memory storage for comments
comments_db = []

@router.get("/", response_model=List[Comment])
async def get_comments():
    return comments_db

@router.get("/{comment_id}", response_model=Comment)
async def get_comment(comment_id: int):
    for comment in comments_db:
        if comment["id"] == comment_id:
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@router.post("/", response_model=Comment)
async def create_comment(comment: Comment):
    comments_db.append(comment.dict())
    return comment

@router.put("/{comment_id}", response_model=Comment)
async def update_comment(comment_id: int, comment: Comment):
    for i, c in enumerate(comments_db):
        if c["id"] == comment_id:
            comments_db[i] = comment.dict()
            return comment
    raise HTTPException(status_code=404, detail="Comment not found")

@router.delete("/{comment_id}")
async def delete_comment(comment_id: int):
    for i, comment in enumerate(comments_db):
        if comment["id"] == comment_id:
            comments_db.pop(i)
            return {"message": "Comment deleted successfully"}
    raise HTTPException(status_code=404, detail="Comment not found")
