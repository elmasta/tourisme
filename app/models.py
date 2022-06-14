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


def init_db():
<<<<<<< HEAD
    # CVS Column Names
    col_names = ['name','catprod','bio', 'ville', 'departement', 'longitude', 'latitude', 'contact']
    # Use Pandas to parse the CSV file
    csvData = pandas.read_csv(filePath,names=col_names, header=None)
    for i,row in csvData.iterrows():
        print(i,row['name'],row['catprod'],row['bio'],row['ville'],row['departement'],row['longitude'],row['latitude'],row['contact'])
        # db.session.add(i,row['name'],row['catprod'],row['bio'],row['ville'],row['departement'],row['longitude'],row['latitude'],row['contact'])
    db.session.commit()
    lg.warning('Database initialized!')

def query_db(list):
    db.session.query(list)
    # checker si ok
    db.session.commit()
=======
    db.drop_all()
    db.create_all()
    lg.warning('Database initialized!')
>>>>>>> parent of 9bf6db8 (prepare for ddb and parsers, more front done)
