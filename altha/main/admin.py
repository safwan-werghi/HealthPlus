from django.contrib import admin
from .models import doctor  , appointment
# Register your models here.

admin.site.register(doctor)
#admin.site.register(patient)
admin.site.register(appointment)
