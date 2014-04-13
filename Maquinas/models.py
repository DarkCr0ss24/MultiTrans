from django.db import models

# Create your models here.
class Maquina(models.Model):   # Modelo que guarda las diferentes maquinas que se usan para los trabajos
	nombre = models.CharField(max_length = 100)   # nombre de la maquina

	def __str__(self):
		return self.nombre   # retorna el nombre de la maquina