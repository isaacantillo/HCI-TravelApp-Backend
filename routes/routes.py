from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter(
    prefix="/routes",
    tags=["routes"]
)

class Route(BaseModel):
    id: int
    name: str
    description: str
    user_id: int

# In-memory storage for routes
routes_db = []

@router.get("/", response_model=List[Route])
async def get_routes():
    return routes_db

@router.get("/{route_id}", response_model=Route)
async def get_route(route_id: int):
    for route in routes_db:
        if route["id"] == route_id:
            return route
    raise HTTPException(status_code=404, detail="Route not found")

@router.post("/", response_model=Route)
async def create_route(route: Route):
    routes_db.append(route.dict())
    return route

@router.put("/{route_id}", response_model=Route)
async def update_route(route_id: int, route: Route):
    for i, r in enumerate(routes_db):
        if r["id"] == route_id:
            routes_db[i] = route.dict()
            return route
    raise HTTPException(status_code=404, detail="Route not found")

@router.delete("/{route_id}")
async def delete_route(route_id: int):
    for i, route in enumerate(routes_db):
        if route["id"] == route_id:
            routes_db.pop(i)
            return {"message": "Route deleted successfully"}
    raise HTTPException(status_code=404, detail="Route not found")
