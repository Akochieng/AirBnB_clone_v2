#!/usr/bin/python3
'''
SImple flask web server to display a HTML body page
only if an interger is received in the url
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    return f"{n} is a number"


@app.route('/number_template/<int:num>', strict_slashes=False)
def number_template(num):
    return render_template('5-number.html', num=num)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
