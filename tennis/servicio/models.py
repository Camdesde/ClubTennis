from django.db import models

class Deporte(models.Model):
    descripcion=models.CharField(max_length=50,verbose_name="descripcion")
    
    def __str__(self):
      fila=self.descripcion
      return fila
    
# Create your models here.
class Servicio(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    Dni=models.IntegerField(verbose_name="DNI")
    Nom = models.CharField(max_length=50,verbose_name="Nombre y Apellido")
    Ap=models.DateField(verbose_name="Apellido paterno")
    Am=models.DateField(verbose_name="Apellido materno")
    Dire=models.CharField(max_length=50,verbose_name="Direccion")
    Foto=models.DateField(verbose_name="Foto")
    Fechahora=models.DateField(verbose_name="Fecha y hora")
    
    
    def __str__(self):
        fila=str(self.id)+"-"+str(self.DNI)+"-"+self.nom
        return fila
    


    