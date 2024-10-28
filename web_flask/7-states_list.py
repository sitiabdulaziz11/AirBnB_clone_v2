#!/usr/bin/python3
""" A script that starts a Flask web application
"""

from flask import Flask, render_template


from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Function that display states list and sort them.
    """
    # states = storage.get_all('State')
    states = sorted(storage.get_all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states1=states)


@app.teardown_appcontext
def close_storage(exception):
    """ Closes the the current session storage to free up resources
    """
    storage.close()  # Calls the close method of DBStorage to release resources 



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
