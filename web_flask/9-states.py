#!/usr/bin/python3
""" A script that starts a Flask web application
"""

from flask import Flask, render_template
import logging

from models import storage
from models.state import State


app = Flask(__name__)


# # Set up basic configuration for logging
# logging.basicConfig(level=logging.DEBUG)  # This sets the logging level to DEBUG
# logger = logging.getLogger(__name__)  # Create a logger for this module


@app.route('/states', strict_slashes=False)
def states():
    """ Function that loads all states and their cities.
    """
    states = sorted(storage.get_all(State).values(), key=lambda state: state.name)
    # city = sorted(states.cities, key=lambda city: city.name)
    return render_template('9-states.html', states1=states)
    # return render_template('8-cities_by_states.html', states1=states, city1=city)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """ Function that loads specific state and its cities.
    """
    state = storage.get_by_id(State, id)
    # print(state)
    
    if state:
        cities = sorted(state.cities, key=lambda  city: city.name)
        return render_template('9-states.html', state1=state, cities1=cities)
    else:
        return render_template('9-states.html', state1=None)


@app.teardown_appcontext
def close_storage(exception):
    """ Closes the the current session storage to free up resources
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
