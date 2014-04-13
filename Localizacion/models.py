from django.db import models
from Trabajos.models import TrabajoSencillo, Proyecto

# Create your models here.
class Distrito(models.Model):   # Modelo que guarda los distritos
	Nombre = models.CharField(max_length = 50)   # nombre del distrito
	Trabajos = models.ManyToManyField(TrabajoSencillo)   # almacena los trabajos que estan localizados en el distrito
	Proyectos = models.ManyToManyField(Proyecto)    # almacena los proyectos que estan localizados en el distrito

	def __str__(self):
		return self.Nombre   # retorna el nombre del distrito


class Provincia(models.Model):   # Modelo que guarda las provincias.
	Nombre = models.CharField(max_length = 50)   # nombre de la provincia
	Distritos = models.ManyToManyField(Distrito)   # Almacena los distritos que estan dentro de el

	def __str__(self):   
		return self.Nombre   # retorna el nombre de la provincia