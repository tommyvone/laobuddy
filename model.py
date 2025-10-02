# model.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Member(db.Model):
    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(100), unique=True,nullable=False)
    email = db.Column(db.String(100), unique=True,nullable=False)
    password = db.Column(db.String(100))
    gender = db.Column(db.String(50))
    country = db.Column(db.String(50))
    city = db.Column(db.String(100))
