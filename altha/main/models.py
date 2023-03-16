from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=False)
    email = models.EmailField(unique=True,blank=False)
    CHOICES = (('male', 'male'),('female','female'))
    gender = models.CharField(max_length=6,choices=CHOICES,blank=False)
    birthday = models.DateField(blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],max_length=17,blank=True,unique=True) # Validators should be a list
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_patient = models.BooleanField('patient status', default=False)
    is_doctor = models.BooleanField('doctor status', default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','gender','birthday','phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_patient(self):
        return self.is_patient
    
    @property
    def is_doctor(self):
        return self.is_doctor


    
    def create_superuser(self,email,password):
        user = self.create_user(
        email = self.normalize_email(email),
        password = password
            )
        user.is_admin  = True
        user.is_active = True
        user.is_staff  = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class doctor(CustomUser):
    Béja = "Béja"
    Ben_Arous ="Ben Arous" 
    Bizerte = "Bizerte"
    Gabés = "Gabés"
    Gafsa = "Gafsa"
    Jendouba = "Jendouba"
    Kairouan = "Kairouan"
    Kasserine = "Kasserine"
    Kébili = "Kébili"
    Ariana = "Ariana" 
    Manouba = "Manouba"
    Mahdia = "Mahdia"
    Médinine = "Médinine"
    Monastir = "Monastir"
    Nabeul = "Nabeul"
    Sfax = "Sfax" 
    Sidi_Bouzid = "Sidi Bouzid"
    Siliana = "Siliana"
    Sousse = "Sousse"
    Tataouine = "Tataouine"
    Tozeur = "Tozeur"
    Tunis = "Tunis"
    Zaghouan = "Zaghouan"
    le_Kef = "le Kef"
    
    location_choices = [("Béja" ,"Béja"), ("Ben_Arous","Ben Arous"), ("Bizerte","Bizerte"), ("Gabés","Gabés"), ("Gafsa","Gafsa"), ("Jendouba","Jendouba"), ("Kairouan","Kairouan"), ("Kasserine","Kasserine"), ("Kébili","Kébili"), ("Ariana","Ariana"), ("Manouba","Manouba"), ("Mahdia","Mahdia"), ("Médinine","Médinine"),   ("Monastir","Monastir"), ("Nabeul","Nabeul"), ("Sfax","Sfax"), ("Sidi_Bouzid","Sidi Bouzid"), ("Siliana","Siliana"), ("Sousse","Sousse"), ("Tataouine","Tataouine"), ("Tozeur","Tozeur"), ("Tunis","Tunis"), ("Zaghouan","Zaghouan"), ("le_Kef","le Kef"),]
    location = models.CharField(blank=False,choices=location_choices,max_length=20)
    specialty = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
    landline_number = models.IntegerField(blank=True,null=True)
    emergency_line = models.IntegerField(blank=True,null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/")




class patient(CustomUser):
    pass
    


class appointment(models.Model):
    date = models.DateField(blank=False)
    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(patient, on_delete=models.CASCADE)
