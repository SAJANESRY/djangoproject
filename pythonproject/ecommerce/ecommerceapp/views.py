from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def aboutview(request):
    return render(request,'About.html')
def registrationview(request):
    return render(request,"registration.html")
def loginview(request):
    return render(request,"login.html")
