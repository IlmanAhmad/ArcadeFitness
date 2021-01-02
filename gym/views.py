from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def home(request):
    """redirects to home page"""
    
    return render(request, 'gym/home.html')

def fitnesscalc(request):
    """redirects to fitness calculator page"""
    
    return render(request, 'gym/fitnesscalc.html')

def bmicalc(request):
    """calculation logic of bmi calculator"""
    if request.method == "POST":
        gender = request.POST.get('gender', '')
        age = int(request.POST.get('age', ''))
        if age >= 2 and age <=102:
            height = int(request.POST.get('height', ''))/100
            weight = int(request.POST.get('weight', ''))
            bmi_calc = weight/height**2
            bmi = "{:.2f}".format(bmi_calc)
            if bmi_calc < 19:
                bmiindex = "Under weight"
            elif bmi_calc >=19 and bmi_calc <=24:
                bmiindex = "Normal"
            elif bmi_calc >24 and bmi_calc <=29:
                bmiindex = "Overweight"
            elif bmi_calc >29 and bmi_calc <=39:
                bmiindex = "Obese"
            elif bmi_calc >39:
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
