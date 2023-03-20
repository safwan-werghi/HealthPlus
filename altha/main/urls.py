from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home/',views.home,name='home'),
    path("search/", views.search_results_view,name="search_results"),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('logout',views.custom_logout,name='logout'),
    path('doctor_sign_up/',views.doctor_sign_up,name='doctor_sign_up'),
    path('take_appointment',views.take_appointment,name='take_appointment'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #new


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
