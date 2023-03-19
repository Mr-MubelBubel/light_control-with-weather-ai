from AI import control_algo
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Dataform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    precipitation = db.Column(db.Float(10), nullable=False)
    max_temp = db.Column(db.Float(10), nullable=False)
    min_temp = db.Column(db.Float(10), nullable=False)
    wind = db.Column(db.Float(10), nullable=False)


@app.route("/", methods=['GET', 'POST'])
def data():
    if request.method == "POST":
        new_form = Dataform(
            precipitation=request.form['precipitation'],
            max_temp=request.form['max_temp'],
            min_temp=request.form['min_temp'],
            wind=request.form['wind']
        )
        db.session.add(new_form)
        db.session.commit()

        ai(new_form.precipitation, new_form.max_temp, new_form.min_temp, new_form.wind)

    return render_template("index.html")


def ai(prec: float, max_temp: float, min_temp: float, wind:float):
    ai_output = control_algo.control_algo(prec, max_temp, min_temp, wind)

    if ai_output == "Nieselregen":
        print("1")
    elif ai_output == "Nebel":
        print("2")
    elif ai_output == "Regen":
        print("3")
    elif ai_output == "Schnee":
        print("4")
    elif ai_output == "Sonne":
        print("5")
    elif ai_output is None:
        print("No data received.")
    else:
        print("Error")


if __name__ == "__main__":
    app.run(debug=True)

