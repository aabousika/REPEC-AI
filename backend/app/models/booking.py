from app import db
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    city_name = db.Column(db.String(20), db.ForeignKey('city.city_name'), nullable=False)
    num_travels = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(80), default='unpaid')
    status = db.Column(db.String(20), default='pending')
    date = db.Column(db.Date, nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Removed redundant foreign keys to city attributes
    # Kept only the essential city_name foreign key

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "city_name": self.city_name,
            "num_travels": self.num_travels,
            "total_price": self.total_price,
            "payment_status": self.payment_status,
            "status": self.status,
            "date": str(self.date),
            "notes": self.notes,
            "created_at": str(self.created_at)
        }
    
class ChatSession(db.Model):
    __tablename__='chat_messages'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content=db.Column(db.String(200),nullable=False)
    recomended_city=db.Column(db.String(200),nullable=False)


    def to_json(self):
        return{
             "id": self.id,
            "user_id": self.user_id,
            "content":self.content,
            "recomended_city":self.recomended_city

        }

