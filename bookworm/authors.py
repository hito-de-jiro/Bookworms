# authors.py

from flask import abort, make_response

from config import db
from models import Author, author_schema, authors_schema


def read_all():
    authors = Author.query.all()
    return authors_schema.dump(authors)


def create(author):
    id_author = author.get("id_author")
    existing_author = Author.query.filter(Author.id_author == id_author).one_or_none()

    if existing_author is None:
        new_author = author_schema.load(author, session=db.session)
        db.session.add(new_author)
        db.session.commit()
        return author_schema.dump(new_author), 201
    else:
        abort(
            406,
            f"Person with last name {id_author} already exists",
        )


def read_one(id_author):
    author = Author.query.filter(Author.id_author == id_author).one_or_none()

    if author is not None:
        return author_schema.dump(author)
    else:
        abort(404, f"Person with last name {id_author} not found")


def update(id_author, author):
    existing_author = Author.query.filter(Author.id_author == id_author).one_or_none()

    if existing_author:
        update_author = author_schema.load(author, session=db.session)
        existing_author.first_name = update_author.first_name
        existing_author.last_name = update_author.last_name
        existing_author.borne = update_author.borne
        existing_author.died = update_author.died
        db.session.merge(existing_author)
        db.session.commit()
        return author_schema.dump(existing_author), 201
    else:
        abort(
            404,
            f"Person with last name {id_author} not found"
        )


def delete(id_author):
    existing_author = Author.query.filter(Author.id_author == id_author).one_or_none()

    if existing_author:
        db.session.delete(existing_author)
        db.session.commit()
        return make_response(f"Author id:{id_author} successfully deleted", 200)
    else:
        abort(
            404,
            f"Person with last name {id_author} not found"
        )
