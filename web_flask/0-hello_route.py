#!/usr/bin/python3
"""start Flash Web App"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints hello HBNB """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """main functyion"""
    app.run(host='0.0.0.0', port=5000)

