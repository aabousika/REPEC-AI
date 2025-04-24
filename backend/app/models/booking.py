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
    city_name=db.Column(db.String(20), db.ForeignKey('city.name'),nullable=False )
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
    

