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


@app.route('/process', methods=["POST"])
def process():

    i = 0
    datas = []
    if request.form["sinon"]:
        results = Producteurs.query.filter(Producteurs.cat.contains(request.form["sinon"]), Producteurs.dept.contains("Seine-Maritime"))
    else:
        results = Producteurs.query.filter(Producteurs.cat.contains(request.form["chooseYourFarm"]), Producteurs.dept.contains("Seine-Maritime"))
    for result in results:
        addr = result.name + " " + result.addr + " " + result.cp + " " + result.ville + " " + result.dept
        datas.append({"name" : result.name,
                      "cat" : result.cat,
                      "addr": addr,
                      "contact": result.contact,
                      "lat": result.lat,
                      "lon": result.lon})
        i += 1
    if i == 0:
        return "error"
    else:
        return jsonify(datas)


if __name__ == "__main__":
    app.run()
