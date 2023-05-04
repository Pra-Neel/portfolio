from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth.models import User
import custom_auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')

