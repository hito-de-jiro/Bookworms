# books.py
from flask import abort, make_response

from config import db
from models import Book, Author, book_schema, books_schema


def read_all():
    books = Book.query.all()
    return books_schema.dump(books)


def read_one(book_id):
    book = Book.query.get(book_id)

    if book is not None:
        return book_schema.dump(book)
    else:
        abort(404, f"Book with ID {book_id} not found")


def update(book_id, book):
    existing_book = Book.query.get(book_id)

    if existing_book:
        update_note = book_schema.load(book, session=db.session)
        existing_book.title = update_note.title
        existing_book.text = update_note.text
        existing_book.genre = update_note.genre
        db.session.merge(existing_book)
        db.session.commit()
        return book_schema.dump(existing_book), 201
    else:
        abort(404, f"Note with ID {book_id} not found")


def delete(book_id):
    existing_book = Book.query.get(book_id)

    if existing_book:
        db.session.delete(existing_book)
        db.session.commit()
        return make_response(f"{book_id} successfully deleted", 204)
    else:
        abort(404, f"Note with ID {book_id} not found")


def create(book):
    author_id = book.get("author_id")
    author = Author.query.get(author_id)

    if author:
        new_note = book_schema.load(book, session=db.session)
        author.notes.append(new_note)
        db.session.commit()
        return book_schema.dump(new_note), 201
    else:
        abort(404, f"Person not found for ID: {author_id}")
