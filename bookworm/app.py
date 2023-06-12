from flask import render_template, request

import config
from models import Author

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route('/', methods=['GET', 'POST'])
@app.route('/<int:page>', methods=['GET', 'POST'])
def home(page=1):
    authors = Author.query.paginate(page=page, per_page=3, error_out=False)

    return render_template("index.html", authors=authors)


@app.route('/search', methods=['GET'])
def search():
    if request.method == 'GET':
        data = request
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
