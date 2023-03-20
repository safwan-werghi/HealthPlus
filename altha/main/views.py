from django.shortcuts import render , redirect
from django.db.models import Q
from .models import doctor , appointment ,CustomUser
from django.contrib.postgres.search import SearchQuery , SearchVector , SearchRank ,SearchHeadline
from itertools import chain 

from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.models import User, Group

from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm , DoctorRegisterForm ,TakeAppointmentForm

# Create your views here.

def home(request):
    return render(request,"main/home.html")



def search_results_view(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        #loc = str(request.GET.get('loc'))
        data = []
        data1 = []
        data2 = []
        query = SearchQuery(q)
        vector1 = SearchVector('first_name', 'last_name')
        vector2 = SearchVector('specialty','bio')
        #search_headline = SearchHeadline('bio',query)   
        #data2 = doctor.objects.annotate(rank=SearchRank(vector,query)).annotate(headline=search_headline).filter(rank__gte=0.001).order_by('-rank')
        if q :
            #data =  doctor.objects.filter(first_name__search=q)
            #data = doctor.objects.annotate(search=vector).filter(search=query)
            #data = doctor.objects.annotate(rank=SearchRank(vector,query)).filter(rank__gte=0.001).order_by('-rank')
            data1 = CustomUser.objects.annotate(rank=SearchRank(vector1,query)).filter(rank__gte=0.001).order_by('-rank').filter(is_doctor=True)
            data2 = doctor.objects.annotate(rank=SearchRank(vector2,query)).filter(rank__gte=0.001).order_by('-rank')
            data = list(chain(data1,data2))
        else :
            data = None
   
        context = { 'data' : data }
        return render(request,"main/search_results.html",context)
        #the section about the 'take appointment' button 
        doctor_id = request.POST.get("doctor_id")
    elif request.method == 'POST'and doctor_id:
        context = { 'doctor_id': doctor_id }
        return render(request,"main/take_appointment.html",context)
		
        
        
        
        
    
        

		
def sign_up(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
           user = form.save()
           user.is_patient = True
           user.save()
           login(request,user)
           return redirect('home')
    else:
        form = UserRegisterForm()
        
    return render(request,'registration/sign_up.html',{'form':form})
    
    
    

def doctor_sign_up(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        doctor_form = DoctorRegisterForm(request.POST)
        if user_form.is_valid() and doctor_form.is_valid():
            user = user_form.save()
            user.is_doctor = True
            user.save()
            doctor = doctor_form.save(commit=False)
            doctor.CustomUser = user
            doctor.save()
            login(request,user)
            return redirect('home')
    else:
        user_form = UserRegisterForm()
        doctor_form = DoctorRegisterForm()
        
    return render(request,'registration/doctor_sign_up.html',{"user_form":user_form,"doctor_form":doctor_form})    
    
    
    


def custom_logout(request):
	if request.method == 'POST':
		logout(request)
		return redirect("home")
	return render(request,"registration/logout.html",{})


def take_appointment(request):
    from .models import doctor , appointment ,CustomUser
    if request.method == 'POST':
        form = TakeAppointmentForm(request.POST)
        doctor_email = request.POST.get('doctor_email')
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = CustomUser.objects.get(email=doctor_email)
            appointment.patient = request.user
            appointment.save()
            return redirect('home')
    else:
        form = TakeAppointmentForm()
    data = []
    data = appointment.objects.all().filter(patient=request.user) 
    context = {"form":form ,"data":data }
    return render(request,'main/take_appointment.html',context)  



	












