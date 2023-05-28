# config.py

import pathlib

import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir=basedir)

app = connex_app.app
app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root27@localhost/library'  # connect database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
