#!/usr/bin/python3
"""Write a script that starts a Flask Web Application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Return Hello HBNB!"""
    return f"Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB"""
    return f"HBNB"


app.run(host='0.0.0.0', port=5000)
