# app.py

from books import books_bp
from bookworm import config
from config import db, ma, migrate
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    return app


if __name__ == '__main__':
    app = create_app()

    from authors import authors_bp
    app.register_blueprint(authors_bp, url_prefix='/api/v1')
    app.register_blueprint(books_bp, url_prefix='/api/v1')
    app.run(port=5000)
