from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from .models import  doctor ,appointment , CustomUser
#from django import datetime
#from phonenumber_field.formfields import PhoneNumberField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label='first name',required=True)
    last_name  = forms.CharField(label='last name',required=True)
    CHOICES = (('male', 'male'),('female','female'))
    gender = forms.ChoiceField(choices=CHOICES,required=True)
    birthdate = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'),label='specify your birthdate',required=True)
    phone_number = forms.CharField(max_length=17,required=True)
    class Meta:
        model = CustomUser
        fields = ["first_name","last_name","phone_number","email","birthdate","password1","password2"]
        
        
#class PatientRegisterForm(ModelForm):
#    email = forms.EmailField(required=True)
#    first_name = forms.CharField(label='first name',required=True)
#    last_name  = forms.CharField(label='last name',required=True)
#    CHOICES = (('male', 'male'),('female','female'))
#    gender = forms.ChoiceField(choices=CHOICES,required=True)
#    birthdate = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'),label='specify your birthdate',required=True)
#    phone_number = forms.CharField(max_length=17,required=True)
#    class Meta:
#        model = patient
#        fields = ["first_name","last_name","phone_number","email","birthdate","password1","password2"]



class DoctorRegisterForm(ModelForm):
    location_choices = [("Béja" ,"Béja"),("Ben_Arous","Ben Arous"), ("Bizerte","Bizerte"), ("Gabés","Gabés"), ("Gafsa","Gafsa"), ("Jendouba","Jendouba"), ("Kairouan","Kairouan"),("Kasserine","Kasserine"),("Kébili","Kébili"), ("Ariana","Ariana"), ("Manouba","Manouba"), ("Mahdia","Mahdia"), ("Médinine","Médinine"),   ("Monastir","Monastir"), ("Nabeul","Nabeul"), ("Sfax","Sfax"), ("Sidi_Bouzid","Sidi Bouzid"), ("Siliana","Siliana"), ("Sousse","Sousse"), ("Tataouine","Tataouine"), ("Tozeur","Tozeur"), ("Tunis","Tunis"), ("Zaghouan","Zaghouan"), ("le_Kef","le Kef"),]
    location = forms.ChoiceField(choices=location_choices,required=True)
    specialty = forms.CharField(max_length=50)
    bio = forms.CharField(max_length=200)
    address = forms.CharField(max_length=50)
    landline_number = forms.IntegerField(required=True)
    emergency_line = forms.IntegerField(required=True)
    profile_picture = forms.ImageField()
    class Meta:
        model = doctor
        fields = ["location","specialty","bio","address","landline_number","emergency_line","profile_picture"]


class TakeAppointmentForm(ModelForm):
	appointment_date = forms.DateField(widget=forms.DateInput(format='%d-%m-%Y'),label='appointment date',required=True)
	first_time_visit =  forms.BooleanField(required=True,initial=False,label='is this your first time visiting ?')
	additional_info = forms.CharField(required=False)
	class Meta:
		model = appointment
		fields = ["appointment_date","first_time_visit","additional_info"]
