# build_database.py

from faker import Faker
from lorem.text import TextLorem

from config import app, db
from models import Author, Book

PERSON = {
    "first_name": "Petro",
    "last_name": "Pup",
    "borne": "1992-09-18",
}

UPDATE_AUTHOR = {
    "first_name": "Jora",
    "last_name": "Mendel",
    "borne": "1992-09-18",  # dob
}

ADD_BOOK = {
    "author_id": 1,
    "genre": "comics",
    "text": "Amet eius sed. Porro ipsum. Ipsum dolor dolor. Ipsum amet. "
            "Consectetur magnam voluptatem. Adipisci sed. Eius quiquia. "
            "Consectetur aliquam.",
    "title": "77 arrows in indian`s ass"
}

fake = Faker()
lorem = TextLorem(srange=(2, 3))

with app.app_context():
    db.drop_all()
    db.create_all()

    for _ in range(50):
        new_person = Author(
            first_name=fake.first_name(),
            last_name=fake.first_name(),
            borne=fake.date_of_birth(),
        )
        new_person.books.append(
            Book(
                title=lorem.sentence(),
                text=lorem.paragraph(),
                genre=fake.word(),
            )
        )
        db.session.add(new_person)
    db.session.commit()
