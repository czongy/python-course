from flask import Flask
from random import randint

app = Flask(__name__)

random_num = randint(0, 9)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route("/<int:number>")
def check(number):
    if number == random_num:
        return "<h1>You found me!</h1>"
    elif number < random_num:
        return "<h1>Too low, try again!</h1>"
    else:
        return "<h1>Too high, try again!</h1>"


if __name__ == "__main__":
    app.run(debug=True)