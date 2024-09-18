from socket import fromshare
from django import forms 
from .models import Pagoservicio


class PagoServicioForm(forms.ModelForm):
  class Meta:
        model=Pagoservicio
       #fields='__all__'
        fields=('idpago_servicio','id','nom','direccion','fechap',"importe")
        labels ={
          
            "idPago_servicio": "id pago_servicio",
            "id" : "socio" ,
            'nom': 'nombre y apellido del socio:',
            "direccion":"Mes al que corresponde la cuota",
            "fechap" : "fecha de pago" ,
            "importe" : "valor del pago del servicio" ,

          #  "nummac" : "numero de macc " ,
           
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(PagoservicioForm,self).__init__(*args,**kwargs)
        
       
        self.fields['direccion']
        self.fields['nom'].empty_label="Selecciona"
       # self.fields['nom'].required=True
        self.fields['fechap'].required=False
        