#!/usr/bin/python3
"""6-number_odd_or_even.py"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello_hbnb"""
    return 'Hello HBNB!'


@app.route('/nbnb/', strict_slashes=False)
def hbnb():
    """hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cWithVariable(text):
    """cWithVariable"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>/', strict_slashes=False)
def pythonWithVariable(text="is cool"):
    """pythonWithVariable"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>/', strict_slashes=False)
def withNumber(n):
    """withNumber"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>/', strict_slashes=False)
def withNumberSendWebpage(n=None):
    """withNumberSendWebpage"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>/', strict_slashes=False)
def numOddEven(n=None):
    """numOddEven"""
    if (n % 2) == 0:
        return render_template(
            '6-number_odd_or_even.html', n=n, oddeven="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, oddeven="odd")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
