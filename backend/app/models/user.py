from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=True)
    user_name=db.Column(db.Integer , unique=True ,nullable=False)
    first_name=db.Column(db.String(50) , nullable=False)
    last_name=db.Column(db.String(50),nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Specify foreign key explicitly
    bookings = db.relationship(
        'Booking', 
        backref='user_ref',
        foreign_keys='Booking.user_id',
        lazy=True
    )

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
             "password":self.password,
             "user_name":self.user_name,
             "first_name":self.first_name,
             "last_name":self.last_name,
             "created_at":self.created_at,
             "update_at":self.updated_at
        }
     
    def set_password(self, password1):
        self.password = generate_password_hash(password1)

    def check_password(self, password1):
        return check_password_hash(self.password, password1)