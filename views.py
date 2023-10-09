from django.shortcuts import render, HttpResponse
from datetime import datetime
from my_app.models import Contact
from my_app.models import Registration
from django.contrib import messages
# Create your views here.


def index(request):
    context = {
        'variable': "this is sent"
    }
    return render(request, 'index.html', context)
   # return HttpResponse("this is home page")


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")


def jobs(request):
    return render(request, 'jobs.html')
    # return HttpResponse("this is job page")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        adharcard = request.POST.get('adharcard')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        c = Contact(name=name, email=email, adharcard=adharcard,
                    phone=phone, desc=desc, date=datetime.today())
        c.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")


def registration(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        surname = request.POST.get("surname")
        birthdate = request.POST.get("birthdate")
        adharcard = request.POST.get("adharcard")
        passport = request.POST.get("passport")
        martial = request.POST.get("martial")
        email = request.POST.get("email")
        address = request.POST.get("address")
        residential = request.POST.get("residential")
        phonenumber = request.POST.get("phonenumber")
        occupation = request.POST.get("occupation")
        commencement = request.POST.get("commencement")
        income = request.POST.get("income")
        registered = request.POST.get("registered")
        r = Registration(firstname=firstname, surname=surname, birthdate=birthdate, adharcard=adharcard, passport=passport, martial=martial,
                         email=email, address=address, residential=residential, phonenumber=phonenumber, occupation=occupation, commencement=commencement,
                         income=income, registered=registered)
        r.save()
        messages.success(
            request, 'Your have successfully registered wait for response!')

    return render(request, 'registration.html')
    # return HttpResponse("fill the registration form")


def signin(request):
    return render(request, 'signin.html')


def login(request):
    return render(request, "login.html")
def home(request):
    return render(request,"home.html")
