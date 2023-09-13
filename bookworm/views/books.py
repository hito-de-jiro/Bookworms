# books.py

from flask import Blueprint, request, jsonify

from bookworm.models.models import Book, Author, book_schema, books_schema, db

books_bp = Blueprint('books', __name__)


@books_bp.route('/books', methods=['GET'])
def read_all():
    """display a list of all books"""
    books = Book.query.all()
    data = books_schema.dump(books)

    if books is not None:
        return data, 200
    else:
        return jsonify(
            {
                "code": "404",
                "message": "Information not found"
            }
        ), 404


@books_bp.route('/books/<int:book_id>', methods=['GET'])
def read_one(book_id):
    """display one book"""
    book = Book.query.get(book_id)

    if book is not None:
        return book_schema.dump(book)
    else:
        return jsonify(
            {
                'code': '404',
                'message': f"Book with ID:{book_id} does not exists",
            }
        ), 404


@books_bp.route('/books', methods=['POST'])
def create():
    """create a new book"""
    book = request.get_json()
    author_id = book.get("author_id")
    author = Author.query.get(author_id)
    title = book.get("title")
    existing_book = Book.query.filter(Book.title == title).one_or_none()

    if existing_book is None:
        new_book = book_schema.load(book, session=db.session)
        author.books.append(new_book)
        db.session.commit()
        data = book_schema.dump(new_book)
        return data, 201
    else:
        return jsonify(
            {
                'code': '409',
                'message': f"Author with ID: {author_id} added this book",
            }
        ), 406


@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update(book_id):
    """update book"""
    book = request.get_json()
    existing_book = Book.query.get(book_id)

    if existing_book:
        update_book = book_schema.load(book, session=db.session)
        existing_book.title = update_book.title
        existing_book.text = update_book.text
        existing_book.genre = update_book.genre
        db.session.merge(existing_book)
        db.session.commit()
        data = book_schema.dump(existing_book)
        return data, 201
    else:
        return jsonify(
            {
                'code': '404',
                'message': f"Note with ID {book_id} not found",
            }
        ), 404


@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete(book_id):
    """delete the book with the selected ID"""
    existing_book = Book.query.get(book_id)

    if existing_book:
        db.session.delete(existing_book)
        db.session.commit()
        return jsonify(
            {
                'Code': "200",
                'message': f"Book with ID:{book_id} successfully deleted",
            }
        ), 200
    else:
        return jsonify(
            {
                'code': '404',
                'message': f"Book with ID:{book_id} not found",
            }
        ), 404
