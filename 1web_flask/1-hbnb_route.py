#!/usr/bin/python3
"""
A script that starts a Flask web application:
"""

from flask import Flask

# Create a Flask application
app = Flask(__name__)


# Define a route for the root URL ("/")
@app.route('/', strict_slashes=False)
def hello():
    """
    function is the view function for the root route.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    function that display “HBNB”
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
