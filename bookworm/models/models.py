# models.py

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    title = db.Column(db.String(255), nullable=False)  # , unique=True
    text = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"Book: {self.title}, id: {self.id}"


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True
        sqla_session = db.session
        include_fk = True


class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    borne = db.Column(db.String(45))
    books = db.relationship(
        Book,
        backref="author",
        cascade="all, delete, delete-orphan",
        single_parent=True,
    )

    def __repr__(self) -> str:
        return f"Author: {self.first_name} {self.last_name}, id: {self.id}"


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
        sqla_session = db.session
        include_relationships = False


book_schema = BookSchema()
books_schema = BookSchema(many=True)
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
