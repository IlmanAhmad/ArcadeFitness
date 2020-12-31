from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def home(request):
    """redirects to home page"""
    
    return render(request, 'gym/home.html')

def fitnesscalc(request):
    """redirects to fitness calculator page"""
    
    return render(request, 'gym/fitnesscalc.html')

def dietplan(request):
    """redirects to diet plan page"""
    
    return render(request, 'gym/dietplan.html')
