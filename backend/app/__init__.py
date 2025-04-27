from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from app.models import *
db = SQLAlchemy()
migrate = Migrate()



def create_app():
    app = Flask(__name__,template_folder='REPEC-AI/frontend/templates',static_folder='REPEC-AI/frontend/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        from .models import city, user, booking
    
    return app

app = create_app()
