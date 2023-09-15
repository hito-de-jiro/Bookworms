# app.py

from flask import Flask

from bookworm.config import DevelopmentConfig
from bookworm.models.models import db, ma


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    ma.init_app(app)

    from bookworm.views.authors import authors_bp
    from bookworm.views.books import books_bp
    app.register_blueprint(authors_bp, url_prefix='/api/v1')
    app.register_blueprint(books_bp, url_prefix='/api/v1')

    @app.route('/')
    def hello():
        return 'Hello, Dude!'

    return app
