from flask import Flask, request

from functions import get_row
from random_forest_model import train_model

app = Flask(import_name=__name__)

rf = train_model("datasets/data_base.csv")

def index():
    return f"<h1>Hello World</h1>"


@app.route("/identify")
def  identify():
    url = request.args["url"]
    atribute_row = get_row(url)
    print(atribute_row)

    predict = rf.predict(atribute_row)
    if predict[0] == 0:
        print("Not Phishing")
    else:
        print("Phishing")

    return "Hello World."
