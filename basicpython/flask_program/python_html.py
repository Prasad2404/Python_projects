from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def test1():
    name="Prasad"
    return render_template("test1.html",student_name=name)

@app.route('/test2')
def test2():
    num=9
    return render_template("test2.html",num=num)

@app.route('/test3')
def test3():
    d={'sub1':70,'sub2':80,'sub3':90}
    return render_template("test3.html",d=d)

if __name__=='__main__':
    app.run(debug=True)