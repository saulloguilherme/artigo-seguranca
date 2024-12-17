from flask import Flask

app = Flask(import_name=__name__)


def index():
    return f"<h1>Hello World</h1>"


@app.route("/identify")
def  identify():
    return "Hello World."
