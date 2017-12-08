#!/usr/bin/python3
"""2-c_route.py"""
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

@app.route('/c/', strict_slashes=False)
def c():
    """c"""
    return 'blank %s' % text

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """c"""
    """text = text.replace('_', ' ')"""
    return 'C %s' % text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
