import pandas
import os
import config

from flask_sqlalchemy import SQLAlchemy
from .app.views import app

db_name = 'app.db'
db = SQLAlchemy(app)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(config.basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

def add_users_to_db():
    # CVS Column Names
    col_names = ['name', 'addr', 'cp', 'ville', 'dept', 'contact', 'lat', 'lon']
    # Use Pandas to parse the CSV file
    csvData = pandas.read_csv(os.path.join(config.basedir, 'producteurs.csv'),names=col_names, header=None)
    for i,row in csvData.iterrows():
        print(i,row['name'],row['addr'],row['cp'],row['ville'],row['dept'],row['contact'],row['lat'],row['lon'])
        # db.session.add(i,row['name'],row['catprod'],row['bio'],row['ville'],row['departement'],row['longitude'],row['latitude'],row['contact'])
    # db.session.commit()

def query_db(list):
    db.session.query(list)
    # checker si ok
    db.session.commit()
