from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from .models import Servicio
from .forms import ServicioForm


# Create your views here

def listaServicio(request):
    servicio=servicio.objects.all()
    return render(request,"Crud/listado.html",{'servicio':servicio})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editar(request,id=0):
      if request.method=="GET":
        if id==0:
            formulario=ServicioForm()   
        else:
            servicioid=servicio.objects.get(pk=id)
            formulario=servicioForm(instance=servicioid)
        return render(request,'Crud/Crear.html',{'formulario':formulario})
      else:
        if id==0:
            formulario=servicioForm(request.POST or None, request.FILES or None)
        else:
            servicioid=Jugador.objects.get(pk=id)
            formulario=servicoForm(request.POST or None, request.FILES or None ,instance=servicioid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('lista')
        
def eliminar(request, id):
    bc=servicio.objects.get(id=id)
    bc.delete()
    return redirect('lista')
        