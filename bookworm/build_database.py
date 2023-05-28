# build_database.py

from config import app, db
from models import Author, Book

AUTHORS_BOOKS = [
    {
        "last_name": "Dumas",
        "first_name": "Alexandre",
        "borne": "24-07-1802",
        "died": "05-12-1870",
        "books": [
            ("The Three musketeers", "Memoires de Monsieur d`Artagnan", "historical"),
        ],
    },
    {
        "last_name": "von Goethe",
        "first_name": "Johann Wolfgang",
        "borne": "28-08-1749",
        "died": "22-03-1832",
        "books": [
            ("Faust", "Faust is unsatisfied with his life", "drama"),
        ],
    },
    {
        "last_name": "Alighieri",
        "first_name": "Dante",
        "borne": "c. 1265",
        "died": "14-09-1321",
        "books": [
            ("The Divine Comedy", "Poem represents the soul's journey towards God", "poetry"),
        ],
    },
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for data in AUTHORS_BOOKS:
        new_author = Author(
            id_author=data.get("id_author"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
            borne=data.get("borne"),
            died=data.get("died"),
        )
        for title, text, genre in data.get("books", []):
            new_author.books.append(
                Book(
                    title=title,
                    text=text,
                    genre=genre,
                )
            )
        db.session.add(new_author)
    db.session.commit()
