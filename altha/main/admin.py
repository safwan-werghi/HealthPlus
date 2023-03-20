from django.contrib import admin
from .models import doctor  , appointment ,CustomUser
# Register your models here.

admin.site.register(doctor)
#admin.site.register(patient)
admin.site.register(appointment)
admin.site.register(CustomUser)
