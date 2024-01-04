#!/usr/bin/python3
'''
Simple flask application that prints a text variable
'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return f"C {text.replace('_',' ')}"


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text='is_cool'):
    return f"Python {text.replace('_',' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
