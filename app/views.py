import json
# from models import query_db

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

app.config.from_object('config')


@app.route("/")
@app.route("/main/")
def index():

    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():

    if request.method == 'POST':
        # ou faire pleins de form
        list = []
        for item in request.form:
            list.append(item)
        # items = Content.query.filter_by(style=request.form[]).order_by(Content.name).all()

        # retour json d'une liste provenant de la BDD
        return jsonify({"lat": items["lat"],
                        "longi": items["lng"]})
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run()
