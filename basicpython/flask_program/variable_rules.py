
from  flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "variable rules"

@app.route('/hello/<name>')
def hello(name):
    return "hello %s"%name

@app.route('/test/<int:id>')
def test(id):
    return "id=%d"%id

@app.route('/marks/<float:percent>')
def marks(percent):
    return "percent=%f"%percent


if __name__=='__main__':
    app.run(debug=True)