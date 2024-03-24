#!/usr/bin/python3
"""start Flash Web App"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>')
def numberPath(n):
    '''numberPath'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def numberTemplatePath(n):
    '''numberTemplatePath'''
    dictio = {
        'n': n
    }
    return render_template('5-number.html', **dictio)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
