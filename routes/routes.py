from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel
from api.google_maps import GoogleMapsRouter
from fastapi.responses import JSONResponse
router = APIRouter(
    prefix="/routes",
    tags=["routes"]
)

google_maps_router = GoogleMapsRouter()

class Route(BaseModel):
    id: int
    name: str
    description: str
    user_id: int


@router.get("/route", response_model=List[Route])
async def get_routes():
    origin = "Vienna, Austria"
    destination = "Prague, Czechia"
    route = google_maps_router.get_route(origin, destination)
    return JSONResponse(content=route)