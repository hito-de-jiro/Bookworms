# app.py

from flask import Flask

from bookworm import config
from bookworm.config import db, ma, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from bookworm.views.authors import authors_bp
    from bookworm.views.books import books_bp
    app.register_blueprint(authors_bp, url_prefix='/api/v1')
    app.register_blueprint(books_bp, url_prefix='/api/v1')

    @app.route('/')
    def hello():
        return 'Hello, Dude!'

    return app
