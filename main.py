from AI import control_algo
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import time as t
# from gpiozero import PWMLED
# from memory_profiler import profile

# Create Flask App and config database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialisation of the LED Pin
# led = PWMLED(17)

class Dataform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    precipitation = db.Column(db.Float(10), nullable=False)
    max_temp = db.Column(db.Float(10), nullable=False)
    min_temp = db.Column(db.Float(10), nullable=False)
    wind = db.Column(db.Float(10), nullable=False)


@app.route("/", methods=['GET', 'POST'])
# @profile
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

        start = t.time()
        ai(new_form.precipitation, new_form.max_temp, new_form.min_temp, new_form.wind) # predict weather
        end = t.time()
        print(end - start)
    return render_template("index.html")


def ai(prec: float, max_temp: float, min_temp: float, wind: float):
    ai_output = control_algo.control_algo(prec, max_temp, min_temp, wind)

    if ai_output == "Nieselregen":
        # led.value(0.7)
        print("1")
    elif ai_output == "Nebel":
        # led.value(1.0)
        print("2")
    elif ai_output == "Regen":
        # led.value(0.8)
        print("3")
    elif ai_output == "Schnee":
        # led.value(0.5)
        print("4")
    elif ai_output == "Sonne":
        # led.value(0.0)
        print("5")
    elif ai_output is None:
        print("No data received.")
    else:
        print("Error")


if __name__ == "__main__":
    app.run(debug=True)

# Kill process
# sudo lsof -i :<PortNumber>
# kill -9 <PID>
