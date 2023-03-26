import os
from dotenv import dotenv_values

config = dotenv_values(".env")
username = config["FLASK_USERNAME"]
password = config["FLASK_PASSWORD"]
database = config["FLASK_DATABASE"]

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_ECHO = True
SECRET_KEY = os.urandom(32)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"postgresql://{username}:{password}@localhost:5432/{database}"
