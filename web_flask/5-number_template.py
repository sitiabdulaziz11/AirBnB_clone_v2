#!/usr/bin/python3
""" A script that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function that display root route
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function that display hbnb route
    """
    return "HBNBH"

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ Function that display C with text route
    """
    return f"C {text.replace('_', ' ')}"

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_fun(text="is cool"):
    """ Function that display C with text route
    """
    return f"Pyhton {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Function that display a number only if n is an integer
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Display HTML page only if n is an integer
    """
    return render_template('5-number.html', n1=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
)