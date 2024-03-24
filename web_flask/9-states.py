#!/usr/bin/python3
'''start flas app'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def statesPath(id=None):
    '''listStates'''
    listStates = None
    s = None
    states = list(storage.all(State).values())
    codePage = 404
    if id is not None:
        res = list(filter(lambda x: x.id == id, states))
        if len(res) > 0:
            s = res[0]
            s.cities.sort(key=lambda x: x.name)
            codePage = 2
    else:
        listStates = states
        for s in listStates:
            s.cities.sort(key=lambda x: x.name)
        listStates.sort(key=lambda x: x.name)
        codePage = 1
    query = {
        'listStates': listStates,
        's': s,
        'code': codePage
    }
    return render_template('9-listStates.html', **query)


@app.teardown_appcontext
def flaskdown(exc):
    '''end request'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
