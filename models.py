from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define your Member model
class Member(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    username = db.Column(db.String(50),unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(100))
    gender = db.Column(db.String(20))
    country = db.Column(db.String(20))
    city = db.Column(db.String(20))
    


    