from bookworm.app import create_app
from bookworm.models.models import db


with create_app().app_context():
    db.create_all()
    