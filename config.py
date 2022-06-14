import os

SECRET_KEY = "#d#JCqThJ-l54\nilK\\7m\x0bp#\tj~#H"

APP_ID = 1200420960103866

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')