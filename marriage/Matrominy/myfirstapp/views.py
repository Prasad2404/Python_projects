from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *

from django.contrib import messages
import datetime
# Create your views here.

def index(request):
    return render(request,"index.html")

''' Registration Form '''

def registration(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        gender = request.POST['gender']
        us = User.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name,
                                      email=email)
        cust = Customer(user=us, dob=dob, gender=gender)
        us.save()
        cust.save()
        print("User successfully Created")
        messages.success(request, 'User created successfully')
        return redirect('/log_in')
    return render(request, 'register.html')

''' Registratin End '''


''' Login Session '''
def log_in(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        us = authenticate(username=email, password=password)
        if us is not None:
            login(request, us)
            messages.success(request, 'User logged in successfully')
            return redirect('/edit_profile')
        else:
            messages.warning(request, 'Invalid Credintials')
            return redirect('/log_in')
    return render(request,"login.html")


def log_out(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return redirect("/log_in")


'''Create Profile'''


def edit_profile(request):
    return render(request,"edit_profile.html")

def insert_data(request):
    if request.method=="POST":
        profile_photo=request.POST["profile_photo"]
        primary_contact=request.POST["contact"]
        alternate_contact=request.POST["contact2"]
        dob=request.POST["dob"]
        age=request.POST["age"]
        mother_tounge=request.POST["mother_tounge"]
        location=request.POST["location"]
        gender=request.POST["gender"]
        marital_status=request.POST["marital_status"]
        about_profile=request.POST["about_profile"]
        main_origin=request.POST["main_origin"]
        otp=request.POST["otp"]
        update_at=request.POST["update_at"]

        total_member_in_family = request.POST["total_member"]
        relationship = request.POST["relationship"]
        married_status = request.POST["married_status"]
        profession = request.POST["profession"]
        family_type = request.POST["family_type"]
        education = request.POST["education"]
        update_at = request.POST["update_at"]

        citizenship = request.POST["citizenship"]
        address_type = request.POST["address_type"]
        address = request.POST["address"]
        city = request.POST["city"]
        pincode = request.POST["pincode"]
        state = request.POST["state"]
        country = request.POST["country"]
        update_at = request.POST["update_at"]

        religion = request.POST["religion"]
        caste = request.POST["caste"]
        subcaste = request.POST["subcaste"]
        star = request.POST["star"]
        rashi = request.POST["rashi"]
        dosh = request.POST["dosh"]
        manglik = request.POST["manglik"]
        religious_update_at = request.POST["religious_update_at"]

        heighst_education = request.POST["heighst_education"]
        heighst_educatio_stream = request.POST["heighst_educatio_stream"]
        profession = request.POST["profession"]
        office_address = request.POST["office_address"]
        annual_income = request.POST["annual_income"]
        professional_detail_update_at = request.POST["professional_detail_update_at"]

        exp_min_age = request.POST["exp_min_age"]
        exp_max_age = request.POST["exp_max_age"]
        exp_height = request.POST["exp_height"]
        exp_marital_status = request.POST["exp_marital_status"]
        exp_mother_tounge = request.POST["exp_mother_tounge"]
        exp_eating_habit = request.POST["exp_eating_habit"]
        exp_smoking_habbit = request.POST["exp_smoking_habbit"]
        exp_drinking_habbit = request.POST["exp_drinking_habbit"]
        exp_religion = request.POST["exp_religion"]
        exp_caste = request.POST["exp_caste"]
        exp_subcaste = request.POST["exp_subcaste"]
        exp_star = request.POST["exp_star"]
        exp_dosh = request.POST["exp_dosh"]
        exp_rashi = request.POST["exp_rashi"]
        exp_mangalik = request.POST["exp_mangalik"]
        exp_education = request.POST["exp_education"]
        exp_city = request.POST["exp_city"]

        height = request.POST["height"]
        weight = request.POST["weight"]
        blood_group = request.POST["blood_group"]
        body_type = request.POST["body_type"]
        complexion = request.POST["complexion"]
        smoke_habbit = request.POST["smoke_habbit"]
        drink_habbit = request.POST["drink_habbit"]
        physical_detail_updated_at = request.POST["physical_detail_updated_at"]

        photo_id = request.POST["photo_id"]
        status = request.POST["status"]
        created_at = request.POST["created_at"]
        updated_at = request.POST["updated_at"]
        updated_by = request.POST["updated_by"]


        c=Customer(profile_photo=profile_photo,primary_contact=primary_contact,alternate_contact=alternate_contact,dob=dob,age=age,
            mother_tounge=mother_tounge,location=location,gender=gender,marital_status=marital_status,about_profile=about_profile,
            main_origin=main_origin,otp=otp,update_at=update_at)
        c.save()



        fi = Family_info(total_member_in_family=total_member_in_family,relationship=relationship,married_status=married_status,
                         proffession=profession,family_type=family_type,education=education,update_at=update_at)
        fi.save()



        add = Address(citizenship=citizenship, address_type=address_type,address=address, city=city,
                      pincode=pincode, state=state,country=country,update_at=update_at)
        add.save()


        rel = Religious(religion=religion, caste=caste, subcaste=subcaste,star=star,rashi=rashi,
                        dosh=dosh, manglik=manglik,religious_update_at=religious_update_at)
        rel.save()


        edu = Professional_detail(heighst_education=heighst_education,heighst_educatio_stream=heighst_educatio_stream,
                                  profession=profession,office_address=office_address, annual_income=annual_income,
                                  professional_detail_update_at=professional_detail_update_at)
        edu.save()


        ce = Customer_expectation(exp_min_age=exp_min_age, exp_max_age=exp_max_age, exp_height=exp_height,
                                  exp_marital_status=exp_marital_status, exp_mother_tounge=exp_mother_tounge,
                                  exp_eating_habit=exp_eating_habit, exp_smoking_habbit=exp_smoking_habbit,
                                  exp_drinking_habbit=exp_drinking_habbit,exp_religion=exp_religion,
                                  exp_caste=exp_caste, exp_subcaste=exp_subcaste,exp_star=exp_star,exp_dosh=exp_dosh,
                                  exp_rashi=exp_rashi, exp_mangalik=exp_mangalik,exp_education=exp_education, exp_city=exp_city)

        ce.save()



        pd=Physical_details(height =height,weight =weight,blood_group =blood_group,complexion=complexion,
        body_type =body_type,smoke_habbit =smoke_habbit,drink_habbit=drink_habbit,physical_detail_updated_at=physical_detail_updated_at)
        pd.save()



        PI=Photo_id(photo_id =photo_id, status =status, created_at =created_at, updated_at =updated_at, updated_by = updated_by)
        PI.save()

        # customer = request.POST["customer"]
        # created_at =request.POST["created_at"]

        IG=Image_gallary(customer =Customer, created_at = created_at)
        IG.save()
        return render(request, 'view_profile.html')
    return render(request, 'edit_profile.html')


def view_profile(request):
    data=Customer.objects.all()
    return render(request, "view_profile.html",{"data":data})

def viewed_profile(request):
    return render(request, "viewed_profile.html")

def viewed_not_contacted(request):
    return render(request, "viewed-not_contacted.html")

def members(request):
    return render(request, "members.html")

def shortlisted(request):
    return render(request, "shortlisted.html")

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def matches(request):
    return render(request, "matches.html")

def profile(request):
    return render(request, "profile.html")
def search(request):
    return render(request, "search.html")
def search_id(request):
    return render(request, "search_id.html")
def faq(request):
    return render(request, "faq.html")
def shortcodes(request):
    return render(request, "shortcodes.html")
def contact(request):
    return render(request, "contact.html")
def privacy(request):
    return render(request, "privacy.html")
def terms(request):
    return render(request, "terms.html")
def services(request):
    return render(request, "services.html")
def inbox(request):
    return render(request, "inbox.html")


def list(request):
    data=Customer.objects.all()

    return render(request,"list.html",{'data':data})



def insert(request):
    if request.method == "POST":
        # primary_contact=request.POST["primary_contact"]
        # alternate_contact=request.POST["alternate_contact"]
        # dob=request.POST["dob"]
        # mother_tounge=request.POST["mother_tounge"]
        # location=request.POST["location"]
        # gender=request.POST["gender"]
        # marital_status=request.POST["marital_status"]
        # about_profile=request.POST["about_profile"]
        # main_origin=request.POST["main_origin"]

        # customer=Customer(primary_contact=primary_contact,alternate_contact=alternate_contact,dob=dob,
        #     mother_tounge=mother_tounge,location=location,gender=gender,marital_status=marital_status,about_profile=about_profile,
        #     main_origin=main_origin)
        # customer.save()

        total_member_in_family = request.POST['total_member']
        relationship = request.POST['relationship']
        married_status = request.POST['married_status']
        family_type = request.POST['family_type']
        education = request.POST['education']

        fi = Family_info(total_member_in_family=total_member_in_family, relationship=relationship,
                         married_status=married_status,
                         family_type=family_type, education=education)
        fi.save()

    return redirect("/view_profile")
    # return render(request, 'edit_profile.html')
    # citizenship = request.POST["citizenship"]
    # address_type = request.POST["address_type"]
    # address = request.POST["address"]
    # city = request.POST["city"]
    # pincode = request.POST["pincode"]
    # state = request.POST["state"]
    # country = request.POST["country"]
    # address_update_at = request.POST["address_update_at"]

    # religion = request.POST["religion"]
    # caste = request.POST["caste"]
    # subcaste = request.POST["subcaste"]
    # star = request.POST["star"]
    # rashi = request.POST["rashi"]
    # dosh = request.POST["dosh"]
    # manglik = request.POST["manglik"]
    # religious_update_at = request.POST["religious_update_at"]

    # heighst_education = request.POST["heighst_education"]
    # heighst_educatio_stream = request.POST["heighst_educatio_stream"]
    # profession = request.POST["profession"]
    # office_address = request.POST["office_address"]
    # annual_income = request.POST["annual_income"]
    # professional_detail_update_at = request.POST["professional_detail_update_at"]

    # exp_min_age = request.POST["exp_min_age"]
    # exp_max_age = request.POST["exp_max_age"]
    # exp_height = request.POST["exp_height"]
    # exp_marital_status = request.POST["exp_marital_status"]
    # exp_mother_tounge = request.POST["exp_mother_tounge"]
    # exp_eating_habit = request.POST["exp_eating_habit"]
    # exp_smoking_habbit = request.POST["exp_smoking_habbit"]
    # exp_drinking_habbit = request.POST["exp_drinking_habbit"]
    # exp_religion = request.POST["exp_religion"]
    # exp_caste = request.POST["exp_caste"]
    # exp_subcaste = request.POST["exp_subcaste"]
    # exp_star = request.POST["exp_star"]
    # exp_dosh = request.POST["exp_dosh"]
    # exp_rashi = request.POST["exp_rashi"]
    # exp_mangalik = request.POST["exp_mangalik"]
    # exp_education = request.POST["exp_education"]
    # exp_city = request.POST["exp_city"]

    # height = request.POST["height"]
    # weight = request.POST["weight"]
    # blood_group = request.POST["blood_group"]
    # body_type = request.POST["body_type"]
    # complexion = request.POST["complexion"]
    # smoke_habbit = request.POST["smoke_habbit"]
    # drink_habbit = request.POST["drink_habbit"]
    # physical_detail_updated_at = request.POST["physical_detail_updated_at"]

    # request.session['id']=customer.id

    # add = Address(c=c,citizenship=citizenship, address_type=address_type,address=address, city=city,
    #               pincode=pincode, state=state,country=country,address_update_at=address_update_at,fi_id=fi.id)
    # add.save()

    # rel = Religious(c=c,religion=religion, caste=caste, subcaste=subcaste,star=star,rashi=rashi,
    #                 dosh=dosh, manglik=manglik,religious_update_at=religious_update_at)
    # rel.save()

    # edu = Professional_detail(c=c,heighst_education=heighst_education,heighst_educatio_stream=heighst_educatio_stream,
    #                           profession=profession,office_address=office_address, annual_income=annual_income,
    #                           professional_detail_update_at=professional_detail_update_at)
    # edu.save()

    # ce = Customer_expectation(c=c,exp_min_age=exp_min_age, exp_max_age=exp_max_age, exp_height=exp_height,
    #                           exp_marital_status=exp_marital_status, exp_mother_tounge=exp_mother_tounge,
    #                           exp_eating_habit=exp_eating_habit, exp_smoking_habbit=exp_smoking_habbit,
    #                           exp_drinking_habbit=exp_drinking_habbit,exp_religion=exp_religion,
    #                           exp_caste=exp_caste, exp_subcaste=exp_subcaste,exp_star=exp_star,exp_dosh=exp_dosh,
    #                           exp_rashi=exp_rashi, exp_mangalik=exp_mangalik,exp_education=exp_education, exp_city=exp_city)

    # ce.save()

    # pd=Physical_details(c=c,height =height,weight =weight,blood_group =blood_group,complexion=complexion,
    # body_type =body_type,smoke_habbit =smoke_habbit,drink_habbit=drink_habbit,physical_detail_updated_at=physical_detail_updated_at)
    # pd.save()


def update(request):
    id = request.GET["id"]
    data=Customer.objects.all().filter(id=id)

    return render(request,"update.html",{'data':data})




def update_data(request):
    if request.method == "POST":
        id = request.POST["id"]
        primary_contact=request.POST["primary_contact"]
        alternate_contact=request.POST["alternate_contact"]
        dob=request.POST["dob"]
        mother_tounge=request.POST["mother_tounge"]
        location=request.POST["location"]
        gender=request.POST["gender"]
        marital_status=request.POST["marital_status"]
        about_profile=request.POST["about_profile"]
        main_origin=request.POST["main_origin"]

        Customer.objects.filter(id=id).update(id=id,primary_contact=primary_contact,alternate_contact=alternate_contact,dob=dob,
            mother_tounge=mother_tounge,location=location,gender=gender,marital_status=marital_status,about_profile=about_profile,
            main_origin=main_origin)


        total_member_in_family = request.POST['total_member']
        relationship = request.POST['relationship']
        married_status = request.POST['married_status']
        family_type = request.POST['family_type']
        education = request.POST['education']

        fi = Family_info(total_member_in_family=total_member_in_family, relationship=relationship,
                         married_status=married_status,
                         family_type=family_type, education=education)
        fi.save()

        return redirect("/view_profile")
    else:
        return HttpResponse("Registration fail")
    # return render(request, 'edit_profile.html')
    # citizenship = request.POST["citizenship"]
    # address_type = request.POST["address_type"]
    # address = request.POST["address"]
    # city = request.POST["city"]
    # pincode = request.POST["pincode"]
    # state = request.POST["state"]
    # country = request.POST["country"]
    # address_update_at = request.POST["address_update_at"]

    # religion = request.POST["religion"]
    # caste = request.POST["caste"]
    # subcaste = request.POST["subcaste"]
    # star = request.POST["star"]
    # rashi = request.POST["rashi"]
    # dosh = request.POST["dosh"]
    # manglik = request.POST["manglik"]
    # religious_update_at = request.POST["religious_update_at"]

    # heighst_education = request.POST["heighst_education"]
    # heighst_educatio_stream = request.POST["heighst_educatio_stream"]
    # profession = request.POST["profession"]
    # office_address = request.POST["office_address"]
    # annual_income = request.POST["annual_income"]
    # professional_detail_update_at = request.POST["professional_detail_update_at"]

    # exp_min_age = request.POST["exp_min_age"]
    # exp_max_age = request.POST["exp_max_age"]
    # exp_height = request.POST["exp_height"]
    # exp_marital_status = request.POST["exp_marital_status"]
    # exp_mother_tounge = request.POST["exp_mother_tounge"]
    # exp_eating_habit = request.POST["exp_eating_habit"]
    # exp_smoking_habbit = request.POST["exp_smoking_habbit"]
    # exp_drinking_habbit = request.POST["exp_drinking_habbit"]
    # exp_religion = request.POST["exp_religion"]
    # exp_caste = request.POST["exp_caste"]
    # exp_subcaste = request.POST["exp_subcaste"]
    # exp_star = request.POST["exp_star"]
    # exp_dosh = request.POST["exp_dosh"]
    # exp_rashi = request.POST["exp_rashi"]
    # exp_mangalik = request.POST["exp_mangalik"]
    # exp_education = request.POST["exp_education"]
    # exp_city = request.POST["exp_city"]

    # height = request.POST["height"]
    # weight = request.POST["weight"]
    # blood_group = request.POST["blood_group"]
    # body_type = request.POST["body_type"]
    # complexion = request.POST["complexion"]
    # smoke_habbit = request.POST["smoke_habbit"]
    # drink_habbit = request.POST["drink_habbit"]
    # physical_detail_updated_at = request.POST["physical_detail_updated_at"]

    # request.session['id']=customer.id

    # add = Address(c=c,citizenship=citizenship, address_type=address_type,address=address, city=city,
    #               pincode=pincode, state=state,country=country,address_update_at=address_update_at,fi_id=fi.id)
    # add.save()

    # rel = Religious(c=c,religion=religion, caste=caste, subcaste=subcaste,star=star,rashi=rashi,
    #                 dosh=dosh, manglik=manglik,religious_update_at=religious_update_at)
    # rel.save()

    # edu = Professional_detail(c=c,heighst_education=heighst_education,heighst_educatio_stream=heighst_educatio_stream,
    #                           profession=profession,office_address=office_address, annual_income=annual_income,
    #                           professional_detail_update_at=professional_detail_update_at)
    # edu.save()

    # ce = Customer_expectation(c=c,exp_min_age=exp_min_age, exp_max_age=exp_max_age, exp_height=exp_height,
    #                           exp_marital_status=exp_marital_status, exp_mother_tounge=exp_mother_tounge,
    #                           exp_eating_habit=exp_eating_habit, exp_smoking_habbit=exp_smoking_habbit,
    #                           exp_drinking_habbit=exp_drinking_habbit,exp_religion=exp_religion,
    #                           exp_caste=exp_caste, exp_subcaste=exp_subcaste,exp_star=exp_star,exp_dosh=exp_dosh,
    #                           exp_rashi=exp_rashi, exp_mangalik=exp_mangalik,exp_education=exp_education, exp_city=exp_city)

    # ce.save()

    # pd=Physical_details(c=c,height =height,weight =weight,blood_group =blood_group,complexion=complexion,
    # body_type =body_type,smoke_habbit =smoke_habbit,drink_habbit=drink_habbit,physical_detail_updated_at=physical_detail_updated_at)
    # pd.save()


def show_data(request):
    data=Customer.objects.all()
    print(data.values())
    return render(request,"show_data.html",{'data':data})

def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return render(request, "show_data.html")
