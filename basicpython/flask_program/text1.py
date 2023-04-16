
from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "WELCOME"

@app.route('/name')
def name():
    return "PRASAD TUPE"

@app.route('/contact')
def contact():
    return "8862024942"

@app.route('/address')
def address():
    return "dhankwadi"

@app.route('/office')
def office():
    return "fortune cloud"


if __name__=='__main__':
    app.run(debug=True)