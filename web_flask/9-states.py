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


@app.route('/states/')
def states():
    """list states from storage method
    Returns:
        HTML
    """
    _dict = storage.all(State)
    all_states = []
    for k, v in _dict.items():
        all_states.append(v)
    return render_template('9-states.html', all_states=all_states)


@app.route('/states/<id>')
def get_state(id):
    _dict = storage.all(State)
    all_states = []
    all_states_id = []
    for k, v in _dict.items():
        all_states_id.append(v.id)
        all_states.append(v)
    return render_template('9-states.html', all_states=all_states,
                           all_states_id=all_states_id, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
