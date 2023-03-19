from django.shortcuts import render , redirect
from django.db.models import Q
from .models import doctor , appointment
from django.contrib.postgres.search import SearchQuery , SearchVector , SearchRank ,SearchHeadline


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
        loc = str(request.GET.get('loc'))
        data = []
        query = SearchQuery(q)
        vector = SearchVector('first_name', 'last_name','specialty','bio')
        search_headline = SearchHeadline('bio',query)
        if q :
            #data =  doctor.objects.filter(first_name__search=q)
            #data = doctor.objects.annotate(search=vector).filter(search=query)
            #data = doctor.objects.annotate(rank=SearchRank(vector,query)).filter(rank__gte=0.001).order_by('-rank')
            data = CustomUser.objects.annotate(rank=SearchRank(vector,query)).annotate(headline=search_headline).filter(rank__gte=0.001).order_by('-rank').filter(location=loc).filter(is_doctor=True)
        
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
           user.set(self,is_patient=True)
           login(request,user)
           return redirect('/home')
    else:
        form = UserRegisterForm()
        
    return render(request,'registration/sign_up.html',{'form':form})
    
    
    

def doctor_sign_up(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        doctor_form = DoctorRegisterForm(request.POST)
        if user_form.is_valid() and  doctor_form.is_valid():
            user.set(self,is_doctor=True)
            user = user_form.save()
            doctor = doctor_form.save()
            login(request,user)
            return redirect('/home')
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
    if request.method == 'POST':
        form = TakeAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            appointment.doctor = doctor.CustomUser.objects.get(id=doctor_id)
            appointment.patient = request.user
            appointment.save()
            return redirect('/home')#redirect to view appointments
    else:
        form = TakeAppointmentForm()
    data = appointment.objects.get(patient=request.user)
    context = {"form":form , "data":data}
    return render(request,'main/take_appointment.html',context)  



	












