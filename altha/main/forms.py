from django import forms

from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import patient
#from django import datetime
#from phonenumber_field.formfields import PhoneNumberField


class PatientRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='first name',required=True)
    last_name  = forms.CharField(label='last name',required=True)
    CHOICES = (('male', 'male'),('female','female'))
    gender = forms.ChoiceField(choices=CHOICES,required=True)
    birthday = forms.DateField(required=True)
    phone_number = forms.CharField(max_length=17,required=True)
    class Meta:
        model = patient
        fields = ["first_name","last_name","phone_number","email","birthday","password1","password2"]
