#from django.contrib import admin
from django.urls import path #here includes is removed from project urls
from portfolio_app import views #this imports views from custom_auth apps

urlpatterns = [
    path('contact/', views.contact, name = 'contact'),
    
]
