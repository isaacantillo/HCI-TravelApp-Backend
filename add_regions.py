import json
from database.firestore import firestore_manager

with open("templates/regions.json", "r") as f:
    regions_json = json.load(f)

if __name__ == "__main__":
    for continent in regions_json:
        continent_doc = firestore_manager.db.collection("destinations").document(continent["continent"].replace(" ", "_"))
        continent_doc.set({
            "continent_name": continent["continent"],
        })  # Create continent document
        
        for region in continent["regions"]:
            region_doc = continent_doc.collection("regions").document(region["name"].replace(" ", "_"))
            region_doc.set({
                "region_name": region["name"],
            })
            
            for city in region["cities"]:
                city_doc = region_doc.collection("cities").document(city["name"].replace(" ", "_"))
                city_doc.set({
                    "city_name": city["name"],
                    "country": city["country"],
                    "price": city["price"],
                })
                print(f"Added city: {city['name']}")
