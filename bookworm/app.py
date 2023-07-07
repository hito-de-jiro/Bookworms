# app.py

from flask import Flask

from bookworm import config
from bookworm.config import db, ma, migrate

from bookworm.views.books import books_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    return app


if __name__ == "__main__":
    application = create_app()
    from bookworm.views.authors import authors_bp
    application.register_blueprint(authors_bp, url_prefix='/api/v1')
    application.register_blueprint(books_bp, url_prefix='/api/v1')
    application.run(port=5000)
