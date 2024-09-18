from socket import fromshare
from django import forms 
from .models import Servicio

class ServicioForm(forms.ModelForm):
  class Meta:
        model=Servicio
       #fields='__all__'
        fields=('DNI','nom','Ap','Am',"Dire","Foto","Fecha y hora")
        labels ={
            "DNI": "DNI" ,
            'nom': 'nombre:',
            "Ap": "Apellido paterno" ,
            "Am": "Apellido materno" , 
            "Dire": "Direccion",
            "Foto":"Foto del cliente",
            "Fecha y hora" : "Fecha y hora",
          #  "nummac" : "numero de macc " ,
           
                   
        
        }
        
    
  def __init__(self, *args, **kwargs):
        super(ServicioForm,self).__init__(*args,**kwargs)
        self.fields['descripcion'].empty_label="Selecciona"
        self.fields['nom'].required=True
        self.fields['fechan'].required=False
        