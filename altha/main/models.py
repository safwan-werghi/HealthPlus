from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin 
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractBaseUser):#PermissionsMixin
    username = None
    first_name = models.CharField(max_length=200,blank=False)
    last_name = models.CharField(max_length=200,blank=False)
    email = models.EmailField(unique=True,blank=False)
    CHOICES = (('male', 'male'),('female','female'))
    gender = models.CharField(max_length=6,choices=CHOICES,blank=False)
    birthdate = models.DateField(blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],max_length=17,blank=False,unique=True,null=False) # Validators should be a list
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_patient = models.BooleanField('patient status',default=False)
    is_doctor = models.BooleanField('doctor status',default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','gender','birthdate','phone_number']

    objects = CustomUserManager()
	
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    #@property
    #def is_patient(self):
    #    return self.is_patient
    
    #@property
    #def is_doctor(self):
    #    return self.is_doctor


    
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


class doctor(models.Model):
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
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    landline_number = models.CharField(validators=[phone_regex],max_length=17,blank=False,unique=True,null=False) # Validators should be a list
    landline_number = models.CharField(validators=[phone_regex],max_length=17,blank=True,unique=True,null=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/",blank=True,null=True)
    is_verified = models.BooleanField('doctor confirmation', default=False)
    is_doctor = True
    CustomUser = models.OneToOneField(CustomUser,primary_key=True,on_delete=models.CASCADE)
    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
      if created and CustomUser.is_doctor == True : 
          doctor.objects.create(CustomUser=instance)

    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, **kwargs):
	    if CustomUser.is_doctor == True : 
              instance.doctor.save()
    class Meta:
       verbose_name = "doctor"




#class patient(models.Model):
#    is_patient = True
#    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#    class Meta:
#       verbose_name = "patient"
#    @receiver(post_save, sender=user)
#    def create_user_profile(sender, instance, created, **kwargs):
#        if created and is_patient == True:
#            patient.objects.create(user=instance)
#
#    @receiver(post_save, sender=user)
#    def save_user_profile(sender, instance, **kwargs):
#	    if user.is_patient == True:
#             instance.doctor.save()
#    class Meta:
#       verbose_name = "doctor"


class appointment(models.Model):
    doctor = models.ForeignKey(doctor,null=False,on_delete=models.CASCADE)#not sure about null 
    patient = models.ForeignKey(CustomUser,null=False,on_delete=models.CASCADE)#not sure about null
    appointment_date = models.DateField()
    first_time_visit = models.BooleanField('first time visit', default=False)
    additional_info = models.CharField(max_length=100,blank=True,null=True)
    is_confirmed = models.BooleanField('doctor confirmation', default=False)
    is_rejected = models.BooleanField('doctor unavailable', default=False)
    class Meta:
       verbose_name = "appointment"
