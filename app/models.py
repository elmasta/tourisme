import logging as lg

from unittest.loader import VALID_MODULE_NAME
from flask_sqlalchemy import SQLAlchemy
from .views import app

db = SQLAlchemy(app)


class Producteurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    addr = db.Column(db.String(300))
    cp = db.Column(db.Integer)
    ville = db.Column(db.String(200))
    dept = db.Column(db.String(200))
    contact = db.column(db.String(200))
    lat = db.Column(db.String(100), nullable=False)
    lon = db.Column(db.String(100), nullable=False)

    def __init__(self, name, addr, cp, ville, dept, contact, lat, lon):
        self.name = name
        self.addr = addr
        self.cp = cp
        self.ville = ville
        self.dept = dept
        self.contact = contact
        self.lat = lat
        self.lon = lon

# faire la table des spécialités et la table de liaison

def init_db():
    db.drop_all()
    db.create_all()
    lg.warning('Database initialized!')