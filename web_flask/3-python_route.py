#!/usr/bin/python3
"""3-python_route.py"""
from flask import Flask

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
