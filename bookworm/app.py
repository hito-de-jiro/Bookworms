# app.py
from config import app

from authors import authors_bp, author_bp


app.register_blueprint(authors_bp, url_prefix='/authors')
app.register_blueprint(author_bp, url_prefix='/author')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
