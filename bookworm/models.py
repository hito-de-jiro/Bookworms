from datetime import datetime
from config import db, ma


class Author(db.Model):
    __tablename__ = "author"
    id_author = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    borne = db.Column(db.String(45))
    died = db.Column(db.String(45))


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
        sqla_session = db.session


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
