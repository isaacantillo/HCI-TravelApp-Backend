from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any
from database.firestore import firestore_manager

router = APIRouter(
    prefix="/destinations",
    tags=["destinations"]
)

# Get all continents
@router.get("/continents", response_model=List[Dict[str, Any]])
async def get_continents():
    """Get all continents"""
    try:
        continents = await firestore_manager.get_all_documents("destinations")
        return [{"id": doc["id"], "name": doc.get("continent_name")} for doc in continents]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get all regions in a continent
@router.get("/continents/{continent_id}/regions", response_model=List[Dict[str, Any]])
async def get_regions(continent_id: str):
    """Get all regions in a continent"""
    try:
        continent_doc = firestore_manager.db.collection("destinations").document(continent_id)
        regions = continent_doc.collection("regions").stream()
        return [{"id": doc.id, "name": doc.get("region_name")} for doc in regions]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get all cities in a region
@router.get("/continents/{continent_id}/regions/{region_id}/cities", response_model=List[Dict[str, Any]])
async def get_cities(continent_id: str, region_id: str):
    """Get all cities in a region"""
    try:
        region_doc = firestore_manager.db.collection("destinations").document(continent_id).collection("regions").document(region_id)
        cities = region_doc.collection("cities").stream()
        return [{"id": doc.id, "name": doc.get("city_name"), "country": doc.get("country"), "price": doc.get("price")} for doc in cities]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get a specific continent
@router.get("/continents/{continent_id}", response_model=Dict[str, Any])
async def get_continent(continent_id: str):
    """Get a specific continent"""
    try:
        continent = await firestore_manager.get_document("destinations", continent_id)
        if not continent:
            raise HTTPException(status_code=404, detail="Continent not found")
        return {"id": continent["id"], "name": continent.get("continent_name")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get a specific region
@router.get("/continents/{continent_id}/regions/{region_id}", response_model=Dict[str, Any])
async def get_region(continent_id: str, region_id: str):
    """Get a specific region"""
    try:
        region_doc = firestore_manager.db.collection("destinations").document(continent_id).collection("regions").document(region_id)
        region = region_doc.get()
        if not region.exists:
            raise HTTPException(status_code=404, detail="Region not found")
        return {"id": region.id, "name": region.get("region_name")}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Get a specific city
@router.get("/continents/{continent_id}/regions/{region_id}/cities/{city_id}", response_model=Dict[str, Any])
async def get_city(continent_id: str, region_id: str, city_id: str):
    """Get a specific city"""
    try:
        city_doc = firestore_manager.db.collection("destinations").document(continent_id).collection("regions").document(region_id).collection("cities").document(city_id)
        city = city_doc.get()
        if not city.exists:
            raise HTTPException(status_code=404, detail="City not found")
        return {
            "id": city.id,
            "name": city.get("city_name"),
            "country": city.get("country"),
            "price": city.get("price")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
