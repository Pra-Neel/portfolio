#from django.contrib import admin
from django.urls import path #here includes is removed from project urls
from custom_auth import views #this imports views from custom_auth apps

urlpatterns = [
    path('login/', views.login, name = 'login' ), #comment ??
    path('signup/', views.signup, name = 'signup'),
    path('home/', views.home, name= 'home'),
    
]
