from django.urls import path
from gym import views

app_name = 'gym'

urlpatterns = [
    path('', views.home, name='home'),
    path('fitnesscalc/', views.fitnesscalc, name='fitnesscalc'),
    path('dietplan/', views.dietplan, name='dietplan'),
    path('bmicalc/', views.bmicalc, name='bmicalc'),
    path('calcalc/', views.calcalc, name='calcalc'),
    path('contactus/', views.contactus, name='contactus'),
    path('handlelogin/', views.handlelogin, name='handlelogin'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.handlelogout, name='logout'),
    path('data/', views.dataextract, name='data'),
    path('aboutus/', views.aboutus, name='aboutus'),
    
]
