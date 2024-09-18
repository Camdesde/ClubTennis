from django.shortcuts import render, redirect
from django.http import HttpResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .forms import PagoServicioForm
from pago_servicio.models import Pagoservicio

# Create your views here

def listapago_servicio(request):
    pago_servicio=Pagoservicio.objects.all()
    return render(request,"crudCuotas/listado.html",{'pago_servicio':pago_servicio})


def inicio(request):
    return render(request,'paginas_base/inicio.html')

def nosotros(request):
    return render(request,'paginas_base/nosotros.html')        

def crear_editar_pago_servicio(request,idpago_servicio=0):
      if request.method=="GET":
        if idPago_servicio==0:
            formulario=PagoServicioForm()   
        else:
            pago_servicioid=Pagoservicio.objects.get(pk=idpago_servicio)
            formulario=PagoServicioForm(instance=pago_servicioid)
        return render(request,'crudCuotas/Crear.html',{'formulario':formulario})
      else:
        if idPago_servicio==0:
            formulario=PagoServicioForm(request.POST or None, request.FILES or None)
        else:
            pago_servicioid=Pagoservicio.objects.get(pk=idpago_servicio)
            formulario=PagoServicioForm(request.POST or None, request.FILES or None ,instance=pago_servicioid)            
        if formulario.is_valid():
            formulario.save()
        return redirect('listapago_servicio')
        
def eliminapago_servicio(request, idpago_servivio):
    bc=Pagoservicio.objects.get(pk=idpago_servicio)
    bc.delete()
    return redirect('listapago_servicio')
        