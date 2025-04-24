from flask import Flask
from __init__ import db
from models import city
from models import user
from datetime import date

class Booking(db.Model) :
    __tablename__='booking'
    id=db.Column(db.Integer ,primary_key=True, unique=True)
    user_id=db.Column(db.Integer , db.ForeignKey('user.id') , nullable=False)
    start_date=db.Column(db.Date , nullable=False)
    end_date=db.Column(db.Date , nullable=False)
    city_name=db.Column(db.String(20), db.ForeignKey('city.city_name'),nullable=False )
    num_travels=db.Column(db.Integer ,nullable=False)
    total_price=db.Column(db.Float ,nullable=False)
    payment_status=db.Column(db.String(80) ,default='unpaid')
    status = db.Column(db.String(20), default='pending')
    date=db.Column(db.Date ,nullable=False)
    notes=db.Column(db.Text)
    best_season=db.Column(db.String(20), db.ForeignKey('city.best_season'),nullable=False)
    budget_category=db.Column(db.Integer , db.ForeignKey('city.budget_category'), nullable=False )
    description=db.Column(db.Text ,db.ForeignKey('city.description'),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    

    def to_json(self):
        return{
            "id":self.id,
            "user_id":self.user_id,
            "start_date":self.start_date,
            "end_date":self.end_date,
            "city_name":self.city_name,
            "num_travels":self.num_travels,
            "total_price":self.total_price,
            "payment_status":self.payment_status,
            "status":self.status,
            "date":self.date,
            "notes":self.notes,
            "best_season":self.best_season,
            "budget_category":self.budget_category,
            "description":self.description,
            "created_at":self.created_at
        }

