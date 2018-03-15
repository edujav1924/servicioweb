from django.shortcuts import render
from django.http import HttpResponse

def mivista(request):
    return render(request,'misitioweb.html')
