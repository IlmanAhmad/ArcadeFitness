from django.urls import path
from gym import views

app_name = 'gym'

urlpatterns = [
    path('', views.home, name='home'),
    
]
