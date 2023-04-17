import datetime
from flask_login import UserMixin
from app.extensions import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(80), nullable=False)
    image_filename = db.Column(db.String(200))
    admin = db.Column(db.Boolean, nullable=False, default=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    category = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer)
    description = db.Column(db.String(80))
    location = db.Column(db.String(80))
    image_filename = db.Column(db.String(200))
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

