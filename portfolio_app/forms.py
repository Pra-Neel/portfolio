from django import forms
from portfolio_app.models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta: #this inheritates the models for the forms
        model = Contact
        fields = '__all__'
        
