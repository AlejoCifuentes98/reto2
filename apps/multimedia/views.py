from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .models import *
from .forms import *
# Create your views here.

def archivos_view(request):
    return render(request, 'multimedia/archivos.html', locals())

def login_view(request):
    return render(request, 'multimedia/login.html', locals())
    
def logout_view(request):
    return render(request, 'multimedia/logout.html', locals())

def registrar_view(request):
    return render(request, 'multimedia/registrar.html', locals())