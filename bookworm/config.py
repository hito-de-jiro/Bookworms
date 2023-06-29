# config.py
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


class Config(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root27@localhost/library'  # connect database
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(DevelopmentConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root27@localhost/test_library'  # connect database
