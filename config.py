# config.py
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
DB_PATH = 'mysql+pymysql://root:root27@localhost/library'  # connect database
app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = DB_PATH
