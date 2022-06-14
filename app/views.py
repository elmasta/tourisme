import json
from qparser import *
from models import query_db

from flask import Flask, render_template, request, jsonify

from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_object('config')

@app.route("/")
@app.route("/main/")
def index():

    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():

    list = request.form["list"]
    manual = request.form["manual"]
    if manual == None:
        query_db(list)
    else:
        manual = RequestParser()
        manual.string_to_list(manual)
        # gestion de la stop word
        with open("fr.json") as json_file:
            stop_word = json.load(json_file)
        manual.request_reading(stop_word)
        if manual.matchlist.count(1) != 0:
            manual.stop_word_remover(stop_word)
            manual.geocoding_researcher(json)
    return jsonify({"lat" : manual.coordinates["lat"],
                    "longi" : manual.coordinates["lng"],
                    "error" : manual.error})

if __name__ == "__main__":
    app.run()