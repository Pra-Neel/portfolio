from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
from portfolio_app.models import Contact
from portfolio_app.forms import ContactForm
# Create your views here.

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.Post)
    
    if form.is_valid():
      form.save()
    else:
      form = ContactForm()

    return render(request, 'contact.html')