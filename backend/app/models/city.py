from app import db
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType

class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(255))
    city_name = db.Column(db.String(20), nullable=False, unique=True)  # Added unique constraint
    best_season = db.Column(MutableList.as_mutable(PickleType), nullable=False)
    visiting_hours = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(60), nullable=False)  # Fixed spelling from 'adress'
    budget_category = db.Column(db.Integer, nullable=False)
    # Simplified relationship - reference only by city_name
    bookings = db.relationship(
        'Booking', 
        backref='city',
        foreign_keys='Booking.city_name',
        lazy=True
    )

    def to_json(self):
        return {
            "id": self.id,
            "image_url": self.image_url,
            "city_name": self.city_name,
            "best_season": self.best_season,
            "budget_category": self.budget_category,
            "visiting_hours": self.visiting_hours,
            "address": self.address
        }
    
class Attractionn(db.Model):
    __tablename__='attractions'
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(100))
    name=db.Column(db.String(44),nullable=False)
    category = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return{
             "description": self.description,
              "category": self.category,
             "id": self.id,
             "image_url": self.image_url,
             "name":self.name,
             "city_id":self.city_id

        }

