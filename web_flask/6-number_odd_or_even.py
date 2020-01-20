#!/usr/bin/python3
"""Use flask route"""
from flask import Flask, escape, render_template

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


@app.route('/number/<int:n>')
def number(n):
    return ('%d is a number' % n)


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)
