from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from gym.models import Contact


# Create your views here.
def home(request):
    """redirects to home page"""

    return render(request, 'gym/home.html')


def contactus(request):
    """redirects to home page"""
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
