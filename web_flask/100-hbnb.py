#!/usr/bin/python3
'''start flas app'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb')
def advenced():
    '''PAth'''
    list_states = list(storage.all(State).values())
    list_states.sort(key=lambda x: x.name)
    amenities = list(storage.all(Amenity).values())
    amenities.sort(key=lambda x: x.name)
    places = list(storage.all(Place).values())
    places.sort(key=lambda x: x.name)
    for state in list_states:
        state.cities.sort(key=lambda x: x.name)
    for place in places:
        place.description = Markup(place.description)
    dictionar = {
        'states': list_states,
        'amenities': amenities,
        'places': places
    }
    return render_template('100-hbnb.html', **dictionar)


@app.teardown_appcontext
def flaskdown(exc):
    '''end request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
