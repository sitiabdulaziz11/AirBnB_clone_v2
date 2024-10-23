#!/usr/bin/python3
"""
A script that starts a Flask web application:
"""

from flask import Flask, render_template

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


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """
    display “C ” followed by the value of the text variable
    """
    text_with_space = text.replace('_', ' ')
    return f'C {text_with_space}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """
    display “Python ”, followed by the value of the text variable
    """
    """if text is None or text.strip() == "":
        return f'Python is cool'
    else:
        value = text.replace('_', ' ')
        return f'Python {value}'"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    display “n is a number” only if n is an integer
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', value=n)


if __name__ == "__main__":
    """excute when it is main function"""
    app.run(host='0.0.0.0', port=5000)