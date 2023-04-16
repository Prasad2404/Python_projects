
# from  flask import Flask,redirect,url_for
#
# app=Flask(__name__)
#
# @app.route('/')
# def home():
#     return redirect(url_for('wel'))
#
# @app.route('/welcome')
# def wel():
#     return "test route"
#
# if __name__=='__main__':
#     app.run(debug=True)




from  flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return "hii"

@app.route("/user/<name>")
def user(name):
    if name=="student":
        return redirect(url_for("student"))
    else:
        return redirect(url_for("customer"))

@app.route('/student')
def student():
    return "i am student"

@app.route('/customer')
def customer():
    return "i am customer"


if __name__=='__main__':
    app.run(debug=True)