from django.shortcuts import render, redirect
from django.http import request
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib import messages



# Create your views here.

def login(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            user_login(request, user )
            messages.success(request, 'Login successfully')
            return redirect('/home')
        else:
            messages.error(request, "Loginerror")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    
    #what is difference between render and redirect??


def signup(request):
    if request.method == 'POST':
        # fullname = request.POST['fullname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
    
        if password == confirm_password:
            user = User.objects.create_user( username=username, email=email, password=password)
            user.save()
            return redirect('/login')
        else:
            messages.error(request, 'Passwords do not matched.')
        
    return render(request, 'signup.html')


def home(request):
    return render(request, 'home.html')


def logout(request):
    user_logout(request)
    messages.success(request, 'User loggedout Successfully')
    return redirect('/login')

