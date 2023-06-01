from flask import render_template

import config
from models import Author, Book

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route('/', methods=['GET'])
def home():
    authors = Author.query.all()
    return render_template("home.html", authors=authors)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
