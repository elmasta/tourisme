import logging as lg

from unittest.loader import VALID_MODULE_NAME
from flask_sqlalchemy import SQLAlchemy
from .views import app

db = SQLAlchemy(app)


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    catprod = db.Column(db.String(200), nullable=False)
    bio = db.Column(db.Integer, nullable=False)
    ville = db.Column(db.String(200), nullable=False)
    departement = db.Column(db.String(200), nullable=False)
    longitude = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.String(100), nullable=False)
    contact = db.column(db.String(200))

    def __init__(self, name, catprod, bio, ville, departement, longitude, latitude, contact):
        self.name = name
        self.catprod = catprod
        self.bio = bio
        self.ville = ville
        self.departement = departement
        self.longitude = longitude
        self.latitude = latitude
        self.contact = contact
