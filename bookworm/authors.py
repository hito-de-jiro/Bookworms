from flask import abort, make_response
from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


AUTHORS = {
    "Dumas": {
        "id_author": 1,
        "first_name": "Alexandre",
        "last_name": "Dumas",
        "borne": "1802-07-24",
        "died": "1870-12-05",
        "books": "The Three Musketeers",
        "create": get_timestamp(),
    }
}


def read_all():
    return list(AUTHORS.values())


def create(author):
    id_author = author.get("id_author")
    last_name = author.get("last_name", "")
    first_name = author.get("first_name", "")
    borne = author.get("borne", "")
    died = author.get("died", "")

    if id_author and id_author not in AUTHORS:
        AUTHORS[id_author] = {
            "id_author": id_author,
            "last_name": last_name,
            "first_name": first_name,
            "borne": borne,
            "died": died,
            "create": get_timestamp(),
        }
        return AUTHORS[id_author], 201
    else:
        abort(
            406,
            f"Person with last name {id_author} already exists",
        )


def read_one(id_author):
    if id_author in AUTHORS:
        return AUTHORS[id_author]
    else:
        abort(
            404, f"Person with last name {id_author} not found"
        )


def update(id_author, person):
    if id_author in AUTHORS:
        AUTHORS[id_author]["first_name"] = person.get("first_name", AUTHORS[id_author]["first_name"])
        AUTHORS[id_author]["last_name"] = person.get("last_name", AUTHORS[id_author]["last_name"])
        AUTHORS[id_author]["borne"] = person.get("borne", AUTHORS[id_author]["borne"])
        AUTHORS[id_author]["died"] = person.get("died", AUTHORS[id_author]["died"])
        AUTHORS[id_author]["create"] = get_timestamp()
        return AUTHORS[id_author]
    else:
        abort(
            404,
            f"Person with last name {id_author} not found"
        )


def delete(id_author):
    if id_author in AUTHORS:
        del AUTHORS[id_author]
        return make_response(
            f"Author id:{id_author} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Person with last name {id_author} not found"
        )
