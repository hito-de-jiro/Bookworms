# build_database.py

from faker import Faker
from lorem.text import TextLorem

from bookworm.app import create_app
from bookworm.models.models import Author, Book, db


def main():
    """Create database with fake data"""
    fake = Faker()
    lorem = TextLorem(srange=(2, 3))

    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()

        for _ in range(10):  # Set range for num person in db
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


if __name__ == "__main__":
    main()
    print('The database has been created!')

