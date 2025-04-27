from flask import Flask
from app import app, db
from app.models import *
from app.utils import *
from app.routes import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
