# models.py

from datetime import datetime

from marshmallow_sqlalchemy import fields

from config import db, ma


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

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
        order_by="desc(Book.timestamp)"
    )

    def __repr__(self) -> str:
        return f"Book: {self.first_name} {self.last_name}, id: {self.id}"


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
        sqla_session = db.session
        include_relationships = True

    books = fields.Nested(BookSchema, many=True)


book_schema = BookSchema()
books_schema = BookSchema(many=True)
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
