from flask import Flask
from __init__ import db
from models import booking
from datetime import date

class City(db.Model) :
    __tablename__='city'
    id=db.Column(db.Integer ,primary_key=True, unique=True)
    image_url = db.Column(db.String(255))
    name=db.Column(db.String(20) ,nullable=False)
    best_season=db.Column(db.PickleType,nullable=False)
    budget_category=db.Column(db.Integer ,nullable=False)
    description=db.Column(db.Text ,nullable=False)
    category=db.Column(db.Integer ,nullable=False)
    visiting_hours=db.Column(db.Integer ,nullable=False)
    adress=db.Column(db.String(60),nullable=False)
    bookings = db.relationship('Booking', backref='city', lazy=True)



