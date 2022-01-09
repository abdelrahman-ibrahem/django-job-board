from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse 
from django.http import HttpResponseRedirect
from .models import Job
from .forms import ApplyJob , AddJob , ContactForm , LoginForm , RegisterForm
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import User
from .filters import JobFilter
# Create your views here.

def home(request):
    jobs = Job.objects.all()
    counter = jobs.count()
    return render(request , 'core/index.html' , {
        'jobs':jobs , 'counter':counter 
    })


def job_detail(request , slug):
    job_details = Job.objects.get(slug=slug)
    if request.method == "POST":
        form = ApplyJob(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            print('save')
            #add link to refresh page
            return HttpResponseRedirect(reverse('main:job_page'))
    else:
        form = ApplyJob()
    return render(request , 'core/job_details.html' , {
        'form':form , 'job_detail':job_details
    })



def add_job(request):
    if request.method == 'POST':
        form = AddJob(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:home'))
        else:
            return HttpResponseRedirect(reverse('main:add_job'))
    else:
        print('Error')
        form = AddJob()
    return render(request , 'core/add_job.html' , {
        'form':form
    })


def job_page(request):
    jobs = Job.objects.all()
    counter = Job.objects.count()
    myFilter = JobFilter(request.GET , queryset= jobs)
    jobs = myFilter.qs
    return render(request , 'core/jobs.html' , {
        'jobs':jobs , 'counter':counter ,"myFilter":myFilter
    })







def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
    else:
        contact_form = ContactForm()
    return render(request , 'core/contact.html' , {
        'form':contact_form
    })



def login_page(request):
    if request.user.is_authenticated:
       return HttpResponseRedirect(reverse('main:home'))
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request ,username=username , password=password)
            if user is not None:
                login(request , user)
                return HttpResponseRedirect(reverse('main:home'))    
        else:
            form = LoginForm()
    return render(request , 'core/login.html' , {
        'form':form
    })


def register_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:home'))    
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('main:login'))
        else:
            form = RegisterForm()
    return render(request , 'core/register.html' , {
        'form':form
    })


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:home'))



def profile_page(request):
    return render(request , 'core/profile.html' , {
        
    })