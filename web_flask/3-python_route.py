#!/usr/bin/python3
"""Write a script that runs a Flask web application"""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Display Hello HBNB! upon GET request"""
    return f"Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB upon GET request"""
    return f"HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Display C followed by various input text upon GET request"""
    return f"C %s" % escape(text).replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Display Python followed by various input text upon GET request"""
    return f"Python %s" % escape(text).replace("_", " ")


@app.route("/python", strict_slashes=False)
def python_default():
    """Display Python is cool"""
    return f"Python is cool"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
