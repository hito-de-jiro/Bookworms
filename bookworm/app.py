# app.py
from config import app

from books import books_bp
from authors import authors_bp


app.register_blueprint(authors_bp, url_prefix='/api/v1')
app.register_blueprint(books_bp, url_prefix='/api/v1')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
