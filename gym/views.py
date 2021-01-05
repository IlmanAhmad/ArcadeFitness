from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages, sessions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from gym.models import Contact
import pandas as pd


# Create your views here.
def home(request):
    """redirects to home page"""

    return render(request, 'gym/home.html')

def loginpage(request):
    """redirects to login page"""

    return render(request, 'gym/login.html')

def handlelogin(request):
    """login authentication"""
    if request.method == "POST":
        user_name = request.POST.get('name', '')
        password = request.POST.get('password', '')

        user = authenticate(username=user_name, password=password)
        if user is not None:
            request.session['name'] = request.POST.get('name', '')
            login(request, user)
            messages.success(
                request, "Your login request is successfull.")
            return redirect("gym:home")
        else:
            messages.error(
                request, "Invalid credentials, Please try again.")
            return redirect("gym:login")
    


    return render(request, 'gym/login.html')

@login_required
def handlelogout(request):
    """redirects to home page post logout"""
    logout(request)
    messages.success(request, "Your have successfully logged out")
    return redirect("gym:home")



def contactus(request):
    """redirects to home page post submitting contact us request"""
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        area = request.POST.get('area', '')

        contact = Contact(name=name, email=email, phone=phone, area=area)
        contact.save()
        messages.success(
            request, "Your request has been submitted. We'll contact with you soon.")
        return redirect("gym:home")
    else:
        return HttpResponse("404-Bad request")

@staff_member_required
def dataextract(request):
    """ contact us form data extract utility"""
    contactdata = Contact.objects.all()
    for i in range(len(contactdata)):
        df = pd.DataFrame(contactdata.values()) # Creating a dataframe for final audit datasheet
        df.to_excel('./data.xlsx', index=False) # Writing data into excel output
    
    return redirect("gym:home")



def fitnesscalc(request):
    """redirects to fitness calculator page"""

    return render(request, 'gym/fitnesscalc.html')


def calcalc(request):
    """calculation logic of calorie calculator"""
    if request.method == "POST":
        gender = request.POST.get('gender', '')
        age = int(request.POST.get('age', ''))
        height = int(request.POST.get('height', ''))
        weight = int(request.POST.get('weight', ''))
        cactivity = float(request.POST.get('cactivity', ''))

        if gender == 'male':
            bmr = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
            calculatedcalorie = bmr * cactivity
            calorie = "{:.2f}".format(calculatedcalorie)
            params = {'calorie': calorie}
            return render(request, 'gym/fitnesscalc.html', params)
        else:
            bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
            calculatedcalorie = bmr * cactivity
            calorie = "{:.2f}".format(calculatedcalorie)
            params = {'calorie': calorie}
            print(bmr, calorie)
            return render(request, 'gym/fitnesscalc.html', params)
    else:
        return HttpResponse("404-Bad request")


def bmicalc(request):
    """calculation logic of bmi calculator"""
    if request.method == "POST":
        gender = request.POST.get('gender', '')
        age = int(request.POST.get('age', ''))
        if age >= 2 and age <= 102:
            height = int(request.POST.get('height', ''))/100
            weight = int(request.POST.get('weight', ''))
            bmi_calc = weight/height**2
            bmi = "{:.2f}".format(bmi_calc)
            if bmi_calc < 19:
                bmiindex = "Under weight"
            elif bmi_calc >= 19 and bmi_calc <= 24:
                bmiindex = "Normal"
            elif bmi_calc > 24 and bmi_calc <= 29:
                bmiindex = "Overweight"
            elif bmi_calc > 29 and bmi_calc <= 39:
                bmiindex = "Obese"
            elif bmi_calc > 39:
                bmiindex = "Extremely Obese"

            params = {'bmi': bmi, 'bmiindex': bmiindex}

            return render(request, 'gym/fitnesscalc.html', params)
        else:
            errormessage = "Please enter age between 2 and 102"
            params = {'errormessage': errormessage}
            return render(request, 'gym/fitnesscalc.html', params)

    else:
        return HttpResponse("404-Bad request")


def dietplan(request):
    """redirects to diet plan page"""

    return render(request, 'gym/dietplan.html')
