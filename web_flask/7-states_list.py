#!/usr/bin/python3
'''start flas app'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states():
    '''tht stat list'''
    list_states = list(storage.all(State).values())
    list_states.sort(key=lambda x: x.name)
    diction = {
        'states': list_states
    }
    return render_template('7-states_list.html', **diction)


@app.teardown_appcontext
def flaskdown(exc):
    '''end request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
