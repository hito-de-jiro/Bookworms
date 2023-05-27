from flask import abort, make_response

from config import db
from models import Author, author_schema, authors_schema


def read_all():
    autors = Author.query.all()
    return authors_schema.dump(autors)


def create(author):
    id_author = author.get("id_author")
    existing_author = Author.query.filter(Author.lname == id_author).one_or_none()

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
    person = Author.query.filter(Author.lname == id_author).one_or_none()

    if person is not None:
        return author_schema.dump(person)
    else:
        abort(404, f"Person with last name {id_author} not found")


def update(id_author, person):
    existing_person = Author.query.filter(Author.lname == id_author).one_or_none()

    if existing_person:
        update_person = author_schema.load(person, session=db.session)
        existing_person.first_name = update_person.first_name
        existing_person.last_name = update_person.last_name
        existing_person.borne = update_person.borne
        existing_person.died = update_person.died
        db.session.merge(existing_person)
        db.session.commit()
        return author_schema.dump(existing_person), 201
    else:
        abort(
            404,
            f"Person with last name {id_author} not found"
        )


def delete(id_author):
    existing_person = Author.query.filter(Author.lname == id_author).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()
        return make_response(f"Author id:{id_author} successfully deleted", 200)
    else:
        abort(
            404,
            f"Person with last name {id_author} not found"
        )
