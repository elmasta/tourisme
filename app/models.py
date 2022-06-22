from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import logging as lg

app = Flask(__name__)

db = SQLAlchemy(app)


class Producteurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    cat = db.Column(db.String(500))
    addr = db.Column(db.String(300))
    cp = db.Column(db.String(20))
    ville = db.Column(db.String(200))
    dept = db.Column(db.String(200))
    contact = db.Column(db.String(300))
    lat = db.Column(db.String(100), nullable=False)
    lon = db.Column(db.String(100), nullable=False)

    def __init__(self, name, cat, addr, cp, ville, dept, contact, lat, lon):
        self.name = name
        self.cat = cat
        self.addr = addr
        self.cp = cp
        self.ville = ville
        self.dept = dept
        self.contact = contact
        self.lat = lat
        self.lon = lon

def init_db():
    db.drop_all()
    db.create_all()
    lg.warning('Database initialized!')

init_db()