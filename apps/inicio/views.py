 

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .models import *
from .forms import *

# Create your views here.

def archivos_view (request):
    lista = Archivo.objects.filter() 
    return render(request, 'inicio/archivos.html', locals())

'''Sección de autenticación'''

def login_view (request):
    usu = ""
    cla = ""
    if request.method == 'POST':
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('/')
            else: 
                msj = 'usuario o clave incorrectos'
    
    formulario = login_form()
    
    return render(request, 'inicio/login.html', locals())    

def logout_view (request):
    logout(request)
    return redirect ('/login/')

def registrar_view (request):
    formulario = registrar_form()
    if request.method == 'POST':
        formulario = registrar_form(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['usuario']
            correo = formulario.cleaned_data['correo']
            clave_1 = formulario.cleaned_data['clave_1']
            clave_2 = formulario.cleaned_data['clave_2']
            u = User.objects.create_user(username = usuario, email = correo, password = clave_2)
            u.save()
            return redirect('/login/')
        else:
            return render(request, 'inicio/registrar.html', locals())
    return render(request, 'inicio/registrar.html', locals())

'''Seccion del inicio'''

def  mis_archivos_view (request):
    usuario = User.objects.get(id = request.user.id)
    lista = Archivo.objects.filter(artista = usuario)
    return render(request, 'inicio/mis_archivos.html', locals())

def archivo_editar_view (request):
    return render(request, 'inicio/archivo_editar.html', locals())

def archivo_ver_view (request, id_archivo):
    object = Archivo.objects.get(id = id_archivo)
    return render(request, 'inicio/archivo_ver.html', locals())

def archivo_agregar_view (request):
    usuario = User.objects.get(id = request.user.id) #Usuario logueado en elmomento
    if request.method == 'POST':
        formulario = agregar_archivo_form(request.POST, request.FILES)
        if formulario.is_valid():
            m =formulario.save(commit= False)
            m.artista = usuario
            m.save()
            return redirect('/mis_archivos/')
    else:
        formulario = agregar_archivo_form()
     
    return render(request, 'inicio/archivo_agregar.html', locals())

def archivo_eliminar_view (request):
    return redirect('/mis_archivos/')
