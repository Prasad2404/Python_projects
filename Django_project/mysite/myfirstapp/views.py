from django.shortcuts import render,HttpResponse,redirect

from .models import students
# Create your views here.

def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")

def addition(request):
    if request.method=="POST":
        n1 = request.POST["num1"]
        n2 = request.POST["num2"]

        result = int(n1)+int(n2)
        print("Addition=",result)

        return HttpResponse("success")
    else:
        return HttpResponse("fail")

def registration(request):
    if request.method=="POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]

        s=students(fname=fname,lname=lname,email=email,password=password)
        s.save()                             #insert

        #return HttpResponse("Registration success")
        return redirect("/welcome")
    else:
        return HttpResponse("Registration fail")


def welcome(request):
    data = students.objects.all()           #select
    return render(request,"welcome.html",{'data':data})


def delete_stud(request):
    id = request.GET['id']
    students.objects.filter(id=id).delete()
    return redirect("/welcome")


def edit_stud(request):
    id = request.GET['id']
    data = students.objects.all().filter(id=id)
    return render(request,"edit.html",{'data':data})


def update_data(request):
    if request.method=="POST":
        id = request.POST["id"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]

        students.objects.filter(id=id).update(fname=fname,lname=lname,email=email,password=password)

        return redirect("/welcome")
    else:
        return HttpResponse("Registration fail")

def login(request):
    return render(request,"login.html")

def login_check(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        data = students.objects.all().filter(email=email,password=password)

        if len(data)==1:

            request.session["username"]=email     #session start

            return redirect('/dashboard')
        else:
            #return HttpResponse("login fail")
            return redirect("/login")


def dashboard(request):
    if request.session.get("username") is not None:
        return render(request,"dashboard.html")
    else:
        return redirect("/login")

def logout(request):
    del request.session["username"]         #session end
    return redirect("/login")


def addcookie(request):
    res = HttpResponse("Cookie Set")

    res.set_cookie("student_name","abcd")
    return res


def getcookie(request):
    name= request.COOKIES["student_name"]
    return HttpResponse("Name="+name)