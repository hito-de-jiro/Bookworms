# build_database.py

from lorem.text import TextLorem

from config import app, db
from models import Author, Book

from faker import Faker

fake = Faker()
lorem = TextLorem(srange=(2, 3))

with app.app_context():
    db.drop_all()
    db.create_all()

    for _ in range(100):
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
