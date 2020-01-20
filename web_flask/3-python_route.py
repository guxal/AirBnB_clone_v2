#!/usr/bin/python3
"""Use flask route"""
from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    return ('HBNB')


@app.route('/c/<text>')
def c(text):
    return ('C %s' % escape(text).replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python/')
def python(text="is cool"):
    return ('Python %s' % escape(text).replace('_', ' '))
