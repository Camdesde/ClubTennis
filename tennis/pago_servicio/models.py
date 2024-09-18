from django.db import models
from servicio.models import Servicio


class Pagoservicio(models.Model):
    idpago_servicio=models.AutoField(primary_key=True,verbose_name="idpago_servicio",db_column='idpago_servicio')
    id=models.ForeignKey(Servicio,on_delete=models.CASCADE,verbose_name="id")
    nom= models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    direccion=models.DateField(verbose_name="Direccion")
    fechap=models.DateField(verbose_name="Fecha de Pago")
    importe=models.DecimalField(max_digits=1000, decimal_places=4, verbose_name="importe")
    
    def __str__(self):
        fila=str(self.idpago_servicio)+"-"+str(self.id)+"-"+self.nom
        return fila
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    