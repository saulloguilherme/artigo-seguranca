from flask import Flask, request

from functions import get_row
from random_forest_model import model_v1, model_v2

rf1 = model_v1()
# rf2 = model_v2()

app = Flask(import_name=__name__)

def index():
    return f"<h1>Hello World</h1>"


@app.route("/v1/identify")
def  identify():
    url = request.args["url"]
    atribute_row = get_row(url)
    print(atribute_row)

    predict = rf1.predict(atribute_row)
    if predict[0] == 0:
        return "Not Phishing"
    else:
        return "Phishing"


# @app.route("/v2/identify")
# def  identify():
#    url = request.args["url"]
#    atribute_row = get_row(url)
#    print(atribute_row)
#
#    predict = rf2.predict(atribute_row)
#    if predict[0] == 0:
#        return "Not Phishing"
#    else:
#        return "Phishing"
