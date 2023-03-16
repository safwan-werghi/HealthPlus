from django.shortcuts import render
from django.db.models import Q
from .models import doctor
from django.contrib.postgres.search import SearchQuery , SearchVector , SearchRank ,SearchHeadline


from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.models import User, Group

from django.contrib.auth.decorators import login_required

from .forms import PatientRegisterForm 

# Create your views here.

def index(request):
    return render(request,"main/home.html")



def search_results_view(request):
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
        
        data = doctor.objects.annotate(rank=SearchRank(vector,query)).annotate(headline=search_headline).filter(rank__gte=0.001).order_by('-rank').filter(location=loc)
        
    else :
        data = None
        
        
    context = { 'data' : data }
    return render(request,"main/search_results.html",context)
        

		
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = PatientRegisterForm()
        
    return render(request,'registration/sign_up.html',{"form":form})
