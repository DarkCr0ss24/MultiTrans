from django.db import models
from Usuarios.models import Autor
from Maquinas.models import Maquina

# Create your models here.
class TrabajoSencillo(models.Model):   # Modelo que se encarga de almacenar los Trabajos sencillos
	Titulo = models.CharField(max_length = 50, null=True, blank=True)   # Titulo del trabajo
	Autor = models.ForeignKey(Autor)   # Autor que hace la petecion de trabajo
	Descripcion = models.TextField()   # descripcion del trabajo
	EquipoNecesario = models.ManyToManyField(Maquina)   # Equipo necesario para llevar a cabo el trabajo
	Localizacion = models.CharField(max_length = 50)   # Lugar donde se va a trabajar
	Fecha = models.DateField(auto_now = True, null=True, blank=True)   # Fecha de la publicacion del trabajo

	def __str__(self):
		return self.Titulo   # retorna el titulo del trabajo

	def titulo(self):
		x = self.Titulo.split()
		return x


class Proyecto(models.Model):  # Modelo encargado de almacenar los diversos proyectos.
	Titulo = models.CharField(max_length = 50)   # Titulo del proyecto
	Autor = models.ForeignKey(Autor)   # Autor del proyecto
	Descripcion = models.TextField()   # Descripcion del proyecto
	EquipoNecesario = models.ManyToManyField(Maquina)   # Equipo necesario para realizar el proyecto
	Localizacion = models.CharField(max_length = 50)   # lugar donde se va a trabajar
	NumeroDeUsuarios = models.IntegerField()   # numero de usuarios necesarios para llevar a cabo el proyecto
	Fecha = models.DateField(auto_now = True, null=True, blank=True)   # Fecha de la publicacion del proyecto

	def __str__(self):
		return self.Titulo  # retorna el titulo del proyecto

	def titulo(self):
		x = self.Titulo.split()
		return x