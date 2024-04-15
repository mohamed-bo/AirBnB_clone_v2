#!/usr/bin/python3
'''start flas app'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def filterPath():
    '''filterPath'''
    list_states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    list_states.sort(key=lambda x: x.name)
    amenities.sort(key=lambda x: x.name)
    for state in list_states:
        state.cities.sort(key=lambda x: x.name)
    dictiona = {
        'states': list_states,
        'amenities': amenities
    }
    return render_template('10-hbnb_filters.html', **dictiona)


@app.teardown_appcontext
def flaskdown(exc):
    '''end request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
