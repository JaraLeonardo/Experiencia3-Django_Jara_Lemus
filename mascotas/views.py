from django.shortcuts import render, redirect
from .models import *
from .forms import MascotaForm, RegistroUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def principal(request):
    return render(request, 'principal.html')

def productos(request):
    return render(request, 'productos.html')

def quiensomos(request):
    return render (request, 'quiensomos.html')
def feriados(request):
    return render (request, 'feriados.html')

@login_required
def almacen(request):
 
    producto=Producto.objects.all()    #obtenemos todos los obj de la clase Vehiculo
    datos={'mascotitas' : producto}     #creamos diccionario que recibe la colección de objetos
    return render(request, 'almacen.html', datos)   #enviamos parámetro al template



def crear(request):
    if request.method=='POST':
        mascotaform = MascotaForm(request.POST, request.FILES)
        if mascotaform.is_valid():
            mascotaform.save()     #similar al insert en función
            return redirect('almacen')
    else:
        mascotaform=MascotaForm()
    return render(request, 'crear.html',{'mascotaform': mascotaform})

def eliminar(request, id):
    productoEliminado=Producto.objects.get(idproducto=id)  #obtenemos un objeto por su pk
    productoEliminado.delete()
    return redirect('almacen')

def modificar(request,id):
    productos = Producto.objects.get(idproducto=id)         #obtenemos un objeto por su pk
    datos ={
        'form':MascotaForm(instance=productos)
    }
    if request.method=='POST':
        formulario = MascotaForm(data=request.POST, instance=productos)
        if formulario.is_valid:
            formulario.save()
            return redirect ('almacen')
    return render(request, 'modificar.html', datos)

def registrar(request):
    data={
        'form' : RegistroUserForm()
    }
    if request.method == 'POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('principal')
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)

def mostrar(request):
    mascotitas =Producto.objects.all()
    datos={
        'mascotitas' : mascotitas
    }
    return render(request,'mostrar.html',datos)