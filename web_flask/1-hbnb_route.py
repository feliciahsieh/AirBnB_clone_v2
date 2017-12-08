#!/usr/bin/python3
"""1-hbnb_route.py"""
from flask import Flask
app = Flask(__name__)
app.run(host='0.0.0.0', port=5000);
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """hello_hbnb"""
    return 'Hello HBNB!'

@app.route('/nbnb')
def hbnb():
    """hbnb"""
    return 'HBNB'
