#!/usr/bin/python3
"""Use flask route"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    """tear down app context"""
    storage.close()


@app.route('/hbnb_filters/')
def hbnb_filters():
    """display filters
    Returns:
        Amenities
        States
        City
    """
    _dict_states = storage.all(State)
    _dict_amenities = storage.all(Amenity)
    _dict_places = storage.all(Place)
    all_states = []
    all_amenities = []
    all_places = []
    for k, v in _dict_states.items():
        all_states.append(v)
    for k, v in _dict_amenities.items():
        all_amenities.append(v)
    for k, v in _dict_places.items():
        all_places.append(v)
    return render_template('100-hbnb.html', all_states=all_states,
                           all_amenities=all_amenities, all_places=all_places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
