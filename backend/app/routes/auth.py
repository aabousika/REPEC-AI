from app.models.user import User
from app.utils.oauth import google
from flask import Flask , render_template , redirect ,request,session,url_for 
from werkzeug.security import generate_password_hash , check_password_hash
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from app import app,db

#chech if email and pass are correct 
@app.route('/')
def home():
    if "email" in session:
        return redirect(url_for('profile')) 
    
    return render_template("login.html")

#login route 
@app.route("/login",methods=["POST"])
def login():
    #collection information from the form
    email=request.form['email']
    password=request.form['password']

    if not email  :
        return render_template("login.html", error="please enter ypor email ")
    if not password:
        return render_template("login.html",error="please enter your password")
    user=User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        session[email]=email
        return redirect(url_for('profile'))
    else:
        return render_template("login.html" , error="incorrect username or password")
    







