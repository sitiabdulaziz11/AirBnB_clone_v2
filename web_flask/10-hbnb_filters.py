#!/usr/bin/python3
""" A script that starts a Flask web application
"""

from flask import Flask, render_template
# import logging

from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)



@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """ Function that loads all states and their cities.
    """
    states = storage.get_all(State).values()
    sorted_states = sorted(states, key=lambda k: k.name)
    
    # Sort the cities within each state by name
    for state in sorted_states:
        state.cities = sorted(state.cities, key=lambda k: k.name)
        
    sorted_aminetis = sorted(storage.get_all(Amenity).values(), key=lambda amenity: amenity.name)
    
    return render_template('10-hbnb_filters.html', states=sorted_states, amenities=sorted_aminetis)


@app.teardown_appcontext
def close_storage(exception):
    """ Closes the the current session storage to free up resources
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            debug=True, port=5000)
