from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
@login_required(login_url='/login/')
def home(request):
    return render(request,'misitioweb.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')
