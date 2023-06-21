# config.py
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
DB_PATH = 'mysql+pymysql://root:root27@localhost/library'  # connect database
TEST_DB_PATH = 'mysql+pymysql://root:root27@localhost/test_library'  # connect database
app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig(Config):
    ENV = "venv"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TEST_DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = True
