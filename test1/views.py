from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("WELCOME TO TECHNOLOGY")

def akos (request):
    return render( request,'fixed/apkos.html')

# Create your views here.
