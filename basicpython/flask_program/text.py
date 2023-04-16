
from flask import Flask

app=Flask(__name__)

@app.route('/')
def user():
    return "my first flask programp"

@app.route('/')
def test():
    return "test"

@app.route('/info')
def info():
    return "info"

if __name__=='__main__':
    app.run(debug=True)
