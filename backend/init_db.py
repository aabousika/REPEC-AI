from flask import Flask 
from datetime import datetime
from app.models.city import City , Attractionn 
from app.models.booking import Booking
from app.models.user import User
from app import db,app


def initialize_database():
    """Initialize the database with default values"""
    with app.app_context():
        
            # Create all tables
            db.create_all()

            if City.query.count() == 0:
                cities_data = [
                   
                    {
            "id": 3,
            "image_url": "lattakia.jpg",
            "city_name": "Lattakia",
            "best_season": "spring,summer,winter,autumn",
            "budget_category": 2,
            "visiting_hours": 7,
            "address": "Lattakia, Syria"
        },
        {
            "id": 4,
            "image_url": "aleppo.jpg",
            "city_name": "Aleppo",
            "best_season": "spring,summer,winter,autumn",
            "budget_category": 1,
            "visiting_hours": 6,
            "address": "Aleppo, Syria"
        },
       
        {
            "id": 6,
            "image_url": "damascus.jpg",
            "city_name": "Damascus",
            "best_season": "spring,summer,winter,autumn",
            "budget_category": 3,
            "visiting_hours": 7,
            "address": "Damascus, Syria"
        },
        {
            "id": 7,
            "image_url": "hama.jpg",
            "city_name": "Hama",
            "best_season": "spring,summer,winter,autumn",
            "budget_category": 2,
            "visiting_hours": 5,
            "address": "Hama, Syria"
        },
        {
            "id": 8,
            "image_url": "homs.jpg",
            "city_name": "Homs",
            "best_season": "spring,summer,winter,autumn",
            "budget_category": 2,
            "visiting_hours": 5,
            "address": "Homs, Syria"
        },
        {
            "id": 9,
            "image_url": "palmyra.jpg",
            "city_name": "Palmyra",
            "best_season": "spring,summer,winter,autumn",
            "budget_category": 3,
            "visiting_hours": 7,
            "address": "Palmyra, Syria"
        },
       
        {
            "id": 11,
            "image_url": "tartus.jpg",
            "city_name": "Tartus",
            "best_season": "spring,summer,winter,autumn",
            "budget_category": 3,
            "visiting_hours": 9,
            "address": "Tartus, Syria"
        }
      
                   
                ]

                for city_data in cities_data:
                 city = City(
                    id=city_data["id"],
                    image_url=city_data["image_url"],
                    city_name=city_data["city_name"],
                    best_season=city_data["best_season"],
                    visiting_hours=city_data["visiting_hours"],
                    address=city_data["address"],
                    budget_category=city_data["budget_category"]
                )
                db.session.add(city)

                attraction_data=[
                      {
                    "city_id": 3,  # Lattakia
                    "name": "Lattakia Beach",
                    "description": "Beautiful Mediterranean beach with golden sands",
                    "image_url": "LatakiaBeach.jpg",
                    "category": 40
                },
                  {
                    "city_id": 4,  # Aleppo
                    "name": "Aleppo Citadel",
                    "description": "The Aleppo Citadel is a monumental medieval fortress in Syria, showcasing over 4,000 years of history and architectural mastery.",
                    "image_url": "latakia_beach_attraction.jpg",
                    "category": 25
                },
                  {
                    "city_id": 6,  # Damascus
                    "name": "Souq ALHamidiya",
                    "description": "Souq Al-Hamidiyah in Damascus is a vibrant, historic market filled with shops, scents, and colors — the perfect place to experience authentic Syrian culture.",
                    "image_url": "SouqAl-Hamidiyah.jpg",
                    "category": 25
                },
                  {
                    "city_id": 6,  # Damascus
                    "name": "Umayyad Mosque",
                    "description": "The Umayyad Mosque in Damascus is one of the oldest and grandest mosques in the world, renowned for its stunning architecture and deep spiritual significance.",
                    "image_url": "UmayyadMosque.jpg",
                    "category": 1
                },
                  {
                    "city_id": 11,  # tartous 
                    "name": "Tartus ",
                    "description": "Tartus is a charming coastal city in Syria, known for its ancient history, relaxed seaside atmosphere, and beautiful Mediterranean views.",
                    "image_url": "Tartus.jpg",
                    "category": 100
                },
                  {
                    "city_id": 7,  # hama
                    "name": "Hama ",
                    "description": "Hama is a historic Syrian city famous for its ancient wooden water wheels (norias) and peaceful setting along the Orontes River.",
                    "image_url":"Hama.jpg",
                    "category": 50
                },
                  {
                    "city_id": 9,  # palmyra
                    "name": "Palmyra",
                    "description": "Palmyra is an ancient Syrian city, once a vibrant oasis of culture and trade, famed for its grand Roman ruins and timeless desert beauty.",
                    "image_url": "Palmyra.jpg",
                    "category": 100
                },
                  {
                    "city_id": 2,  # Homs
                    "name": "Homs",
                    "description": "Homs is a historic Syrian city known for its rich heritage, vibrant spirit, and key location connecting the country’s major regions.",
                    "image_url": "Homs.jpg",
                    "category": 50
                }
                ]


                for attraction in attraction_data:
                 attraction = Attractionn(
                    city_id=attraction_data["city_id"],
                    name=attraction_data["name"],
                    description=attraction_data["description"],
                    image_url=attraction_data["image_url"],
                    category=attraction_data["category"]
                )
                db.session.add(attraction)
            
            db.session.commit()
            print("Database initialized with cities and attractions data.")

            

if __name__ == '__main__':
    initialize_database()