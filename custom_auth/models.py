from django.db import models

# Create your models here.

from django.core.validators import EmailValidator

class ContactForm(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(validators=[EmailValidator()])
    message = models.TextField()
