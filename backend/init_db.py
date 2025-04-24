from flask import Flask 
from datetime import date
from app.models.city import City 
from app.models.booking import Booking
from app.models.user import User
from app.models.__init__ import db,app


def init_db():
    'default value in db'

with app.app_context():
    db.create_all()

lattakia_Beach=City(
    id=2,
    image_url='latakia Beach.jpg',
    city_name='lattakia',
    best_season=['spring','summer','winter','autumn'],
    budget_category=1,
    description='A calm Mediterranean beach city with beautiful coastal views, affordable public beaches, and a relaxing atmosphere. Ideal for low to mid-budget travelers.',
    category=40,
    visiting_hours=6,
    adress='Mediterranean Coast, Lattakia, Syria'
)

lattakia=City(
     id=2,
    image_url='lattakia.jpg',
    city_name='lattakia',
    best_season=['spring','summer','winter','autumn'],
    budget_category=2,
    description='A peaceful coastal city with Mediterranean beaches, historic charm, and affordable travel experiences',
    category=50,
    visiting_hours=7,
    adress=' Lattakia, Syria'
    
)

aleppo=City(
    id=3,
    image_url='Aleppo.jpg',
    city_name='Aleppo',
    best_season=['spring','summer','winter','autumn'],
    budget_category=2,
    description='ancient city with beautiful castl and greate history and natural view   ',
    category=50,
    visiting_hours=6,
    adress='Aleppo, Syria'

)

aleppo_Citadel=City(
    id=4,
    image_url='Aleppo Citadel.jpg',
    city_name='Aleppo',
    best_season=['spring','summer','winter','autumn'],
    budget_category=2,
    description='ancient citadel with beautifull natural view and high level    ',
    category=35,
    visiting_hours=4,
    adress='Aleppo citadel Aleppo, Syria'

)


damascus=City(
    id=5,
    image_url='Damascus.jpg',
    city_name='Damascus',
    best_season=['spring','summer','winter','autumn'],
    budget_category=3,
    description='this city is located between ancient and modern building and has alot of entrainment places ',
    category=100,
    visiting_hours=7,
    adress='damascus, Syria'

)

hama=City(
    id=6,
    image_url='Hama.jpg',
    city_name='Hama',
    best_season=['spring','summer','winter','autumn'],
    budget_category=2,
    description='peacfull city has alot of nice place  and has a beautifull waterwheels  ',
    category=35,
    visiting_hours=5,
    adress='Hama, Syria'
)

homs=City(
    id=7,
    image_url='Homs.jpg',
    city_name='Homs',
    best_season=['spring','summer','winter','autumn'],
    budget_category=2,
    description='beautifull city has alot of quit country and famous for homs clock ',
    category=50,
    visiting_hours=5,
    adress='homs, Syria'

)

palmyra=City(
    id=8,
    image_url='Palmyra.jpg',
    city_name='palmyra',
    best_season=['spring','summer','winter','autumn'],
    budget_category=3,
    description='ancient city famous for amphitheatre ,tourists come to visite palmyra from long distance  ',
    category=70,
    visiting_hours=7,
    adress='palmyra, Syria'

)

souq_alhamidiya=City(
    id=8,
    image_url='Souq Al_Hamidiyah.jpg',
    city_name='Damascus',
    best_season=['spring','summer','winter','autumn'],
    budget_category=1,
    description='traditional market in Damascus has alot of beautifull product and has famous   arabic ice_cream ',
    category=25,
    visiting_hours=3,
    adress='Damascus , Syria'

)
tartus=City(
    id=9,
    image_url='Tartus.jpg',
    city_name='Tartus',
    best_season=['spring','summer','winter','autumn'],
    budget_category=3,
    description='tartus has a very beautiful beach , it is tittle as bridegroom of the sea',
    category=100,
    visiting_hours=9,
    adress='Aleppo citadel Aleppo, Syria'

)

Umayyad_Mosque=City(
    id=10,
    image_url='Umayyad Mosque.jpg',
    city_name='Damascus',
    best_season=['spring','summer','winter','autumn'],
    budget_category=1,
    description='very beautiful architect building , has a very important value for muslim ',
    category=25,
    visiting_hours=1,
    adress='Damascus, Syria'

)



