from flask import Flask
from __init__ import db,app
from models import booking
from datetime import date
from authlib.integrations.flask_client import OAuth  #for google authentication  
from werkzeug.security import generate_password_hash , check_password_hash

class User(db.Model) :
    __tablename__='user'
    
    id=db.Column(db.Integer , primary_key=True)
    email=db.Column(db.String(50) ,nullable=False)
    password=db.Column(db.String(150) , nullable=True )
    bookings = db.relationship('Booking', backref='user', lazy=True)
   

    def to_json(self):
        return{
            "id":self.id,
            "email":self.email,
            "password":self.password
        }
     
    def set_password(self,password1):
        self.password=generate_password_hash(password1)

    def check_password(self,password1):
        return check_password_hash(self.password,password1)

oauth=OAuth(app) 


