#!/usr/bin/python3
"""Use flask route"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    return ('HBNB')
