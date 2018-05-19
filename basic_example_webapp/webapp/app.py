#! /usr/bin/python

from flask import Flask
from flask import render_template

app = Flask(__name__)

#define an index (plain text)
#@app.route('/')
#def index():
#    return 'Hello world'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

#dynamic content: you are passing name as a variable
@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
