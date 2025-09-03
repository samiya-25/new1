from django.shortcuts import render
from django.http import HttpResponse
from home.models import Home
from home.models import About
from staff.models import Staff

def HomePage(request):
    HomePage_data=Home.objects.all()
    HomePage_data_render={
        'home':HomePage_data,
    }
    return render(request,'index.html',HomePage_data_render)

def AboutPage(request):
    AboutPage_data=About.objects.all()
    AboutPage_data_render={
        'about':AboutPage_data,
    }
    return render(request,'about.html',AboutPage_data_render)

def StaffPage(request):
    StaffPage_data=Staff.objects.all()
    StaffPage_data_render={
        'staff':StaffPage_data,
    }
    return render(request,'staff.html',StaffPage_data_render)