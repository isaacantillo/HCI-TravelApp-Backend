from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class TravelMode(Enum):
    DRIVING = "DRIVING"
    WALKING = "WALKING" 
    BICYCLING = "BICYCLING"
    TRANSIT = "TRANSIT"


class GoogleMapsRouter:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        self.routes_api_url = os.getenv("GOOGLE_MAPS_ROUTES_API_URL")
    def get_route(
        self,
        origin: str,
        destination: str,
    ) -> Dict:

        response = requests.post(self.routes_api_url, 
        headers={
            "Content-Type": 'application/json',
            'X-Goog-Api-Key': self.api_key,
            'X-Goog-FieldMask': 'routes.legs.steps.transitDetails,routes.duration,routes.distanceMeters,routes.polyline.encodedPolyline'
        },
        json={
                "origin": {
                    "address": origin
                },
                "destination": {
                    "address": destination
                },
                "travelMode": "TRANSIT",
                "computeAlternativeRoutes": True,
                "transitPreferences": {
                    "routingPreference": "TRANSIT_ROUTING_PREFERENCE_UNSPECIFIED",
                    "allowedTravelModes": ["RAIL"]
                }
            }
        )
        print(response.json())

        return response.json()
