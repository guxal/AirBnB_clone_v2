#!/usr/bin/python3
"""Use flask route"""
from flask import Flask, escape, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(self):
    """tear down app context"""
    storage.close()


@app.route('/cities_by_states/')
def cities_by_states():
    """list states from storage method
    Returns:
        HTML
    """
    _dict = storage.all(State)
    all_states = []
    for k, v in _dict.items():
        all_states.append(v)
    return render_template('8-cities_by_states.html', states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
