from django.shortcuts import render, redirect
from django.http import request
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def login(request):
    if request.method == 'POST': 
        username = request.POST[username]
        password = request.POST[password]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user )
            return redirect('/home')
        else:
            return HttpResponse('Login error')
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
            return redirect('/login')
        else:
            return HttpResponse('password not matched.')
        
    return render(request, 'signup.html')


