from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify
from .models import Producteurs

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object('config')

@app.route("/")
@app.route("/main/")
def index():

    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():

    if request.form["sinon"]:
        print(request.form["sinon"])
        results = Producteurs.query.filter(Producteurs.cat.contains(request.form["sinon"]), Producteurs.dept.contains("Seine-Maritime"))
        for result in results:
            print(result.name)
    else:
        print(request.form["chooseYourFarm"])
    
    return render_template("index.html")

    # items = Content.query.filter_by(style=request.form[]).order_by(Content.name).all()

    # retour json d'une liste provenant de la BDD
    # return jsonify({"lat": items["lat"],
    #                 "longi": items["lng"]})


if __name__ == "__main__":
    app.run()
