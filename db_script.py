import os
import config
import json
import sqlite3

from flask_sqlalchemy import SQLAlchemy
from app.models import Producteurs
from flask import Flask

app = Flask(__name__)
db_name = 'app.db'
db = SQLAlchemy(app)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(config.basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# def fill_db():

#     with open("producteurs.json", encoding='utf-8') as file:
#         file = json.load(file)
#         for producers in file:
#             print(db.session)
#             item = Producteurs(producers["name"],
#                                producers["cat"],
#                                producers["addr"],
#                                int(producers["cp"]),
#                                producers["ville"],
#                                producers["dept"],
#                                producers["contact"],
#                                producers["lat"],
#                                producers["lon"])
#             db.session.add(item)
#             db.session.commit()
#             # create a message to send to the console
#             print("The producer" + producers["name"] + "has been submitted.")
#             break

# fill_db()

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

def fill_db():

    with open("producteurs.json", encoding='utf-8') as file:
        file = json.load(file)
        for producers in file:
            cat_str = ""
            for i in producers["cat"]:
                cat_str += i
            sql = """INSERT INTO producteurs (name,
                    cat, addr, cp, ville, dept, contact, lat, lon)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            val = (str(producers["name"]),
                   str(producers["cat"]),
                   str(producers["addr"]),
                   str(producers["cp"]),
                   str(producers["ville"]),
                   str(producers["dept"]),
                   str(producers["contact"]),
                   str(producers["lat"]),
                   str(producers["lon"]))
            cursor.execute(sql, val)
            connection.commit()

fill_db()
