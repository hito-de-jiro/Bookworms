# books.py

from flask import abort, make_response, Blueprint

from bookworm.config import db
from bookworm.models.models import Book, Author, book_schema, books_schema

books_bp = Blueprint('books', __name__)
book_bp = Blueprint('book', __name__)


@books_bp.route('/books', methods=['GET'])
def read_all():
    books = Book.query.all()
    return books_schema.dump(books)


@books_bp.route('/books/<int:book_id>', methods=['GET'])
def read_one(book_id):
    book = Book.query.get(book_id)

    if book is not None:
        return book_schema.dump(book)
    else:
        abort(404, f"Book with ID {book_id} not found")


@books_bp.route('/books', methods=['POST'])
def create(book):
    author_id = book.get("author_id")
    author = Author.query.get(author_id)
    "TODO: fix double book creation"
    if author:
        new_book = book_schema.load(book, session=db.session)
        author.books.append(new_book)
        db.session.commit()
        return book_schema.dump(new_book), 201
    else:
        abort(404, f"Person not found for ID: {author_id}")


@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update(book_id, book):
    existing_book = Book.query.get(book_id)

    if existing_book:
        update_book = book_schema.load(book, session=db.session)
        existing_book.title = update_book.title
        existing_book.text = update_book.text
        existing_book.genre = update_book.genre
        db.session.merge(existing_book)
        db.session.commit()
        return book_schema.dump(existing_book), 201
    else:
        abort(404, f"Note with ID {book_id} not found")


@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete(book_id):
    existing_book = Book.query.get(book_id)

    if existing_book:
        db.session.delete(existing_book)
        db.session.commit()
        return make_response(f"{book_id} successfully deleted", 204)
    else:
        abort(404, f"Note with ID {book_id} not found")
