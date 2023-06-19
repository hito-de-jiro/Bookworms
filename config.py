# config.py
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root27@localhost/library'  # connect database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
