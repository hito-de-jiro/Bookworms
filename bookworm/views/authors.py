# authors.py

from flask import abort, make_response, Blueprint, request
from sqlalchemy import or_

from bookworm.models.models import Author, author_schema, authors_schema, db

authors_bp = Blueprint('authors', __name__)


@authors_bp.route('/authors', methods=['GET'])
def read_all():
    """display a list of all authors"""
    authors = Author.query.all()
    data = authors_schema.dump(authors)

    if not data:
        abort(404, "Information not found")
    else:
        return data, 200


@authors_bp.route('/authors/<int:id_author>', methods=['GET'])
def read_one(id_author):
    """display one author with the selected ID"""
    author = Author.query.filter(Author.id == id_author).one_or_none()

    if author is not None:
        return author_schema.dump(author)
    else:
        abort(404, f"Author with ID:{id_author} not found")


@authors_bp.route('/authors', methods=['POST'])
def create():
    author = request.get_json()
    _id = author.get("id")
    existing_author = Author.query.filter(Author.id == _id).one_or_none()

    if existing_author is None:
        new_author = author_schema.load(author, session=db.session)
        db.session.add(new_author)
        db.session.commit()
        return author_schema.dump(new_author), 201
    else:
        abort(
            406,
            f"Author with ID:{_id} already exists",
        )


@authors_bp.route('/authors/<int:id_author>', methods=['PUT'])
def update(id_author):
    """update author with the selected ID"""
    author = request.get_json()
    existing_author = Author.query.filter(Author.id == id_author).one_or_none()

    if existing_author:
        update_author = author_schema.load(author, session=db.session)
        existing_author.first_name = update_author.first_name
        existing_author.last_name = update_author.last_name
        existing_author.borne = update_author.borne
        db.session.merge(existing_author)
        db.session.commit()

        return author_schema.dump(existing_author), 201
    else:
        abort(
            404,
            f"Author with ID:{id_author} not found"
        )


@authors_bp.route('/authors/<int:id_author>', methods=['DELETE'])
def delete(id_author):
    """delete author with the selected ID"""
    existing_author = Author.query.filter(Author.id == id_author).one_or_none()

    if existing_author:
        db.session.delete(existing_author)
        db.session.commit()
        return make_response(f"Author with ID:{id_author} successfully deleted", 200)
    else:
        abort(
            404,
            f"Author with ID:{id_author} not found"
        )


@authors_bp.route('/authors/search', methods=['GET'])
def search():
    """search author"""
    if request.method == 'GET' and 'q' in request.args:

        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 5, type=int)
        q = request.args.get('q')
        searched = "%{}%".format(q)
        authors = Author.query.filter(
            or_(Author.last_name.like(searched), Author.first_name.like(searched))).paginate(page=page,
                                                                                             per_page=per_page,
                                                                                             error_out=False)
        data = authors_schema.dump(authors)
        if not data:
            abort(404, "Information not found")
        else:
            return data, 200
    else:
        abort(404, "Information not found")
