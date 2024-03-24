#!/usr/bin/python3
"""start Flash Web App"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    '''index'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''hbnp path'''
    return 'HBNB'


@app.route('/c/<text>')
def cPath(text):
    '''c path'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonPath(text='is cool'):
    '''python Path'''
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
