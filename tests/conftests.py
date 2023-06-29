import pytest
from bookworm import config

from bookworm.config import db
from bookworm.app import app
from bookworm.models import Author


@pytest.fixture
def client():
    # app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:root27@localhost/test_library'  # connect database
    app.config.from_object(config.TestConfig)
    with app.test_client():
        with app.app_context():
            yield client


@pytest.fixture
def init_database():
    db.create_all()

    test_authors = []

    def create_post_model(author):
        return Author(**author)

    mapped_authors = map(create_post_model, test_authors)
    t_authors = list(mapped_authors)


    db.session.add_all(t_authors)

    db.session.commit()

    yield db

    db.session.remove()

    db.drop_all()