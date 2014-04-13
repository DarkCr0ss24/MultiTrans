from django.db import models

class Usuario(models.Model):   # Modelo para almacenar la informacion de los usuarios
	nombre = models.CharField(max_length=50)   # Se guarda el nombre, nickname o alias del usuario
	correo = models.EmailField(max_length=50)   # Guarda el correo del usuario
	clave = models.CharField(max_length=50)   # Guarda la clave del usuario
	avatar = models.ImageField(upload_to = 'static/Imagenes', blank = True, null = True)   # Guarda la Imagen de perfil del usuario

	def __str__(self):
		return self.nombre   # retorna el nombre del usuario

	class Meta:
		ordering = ["nombre"]   # Ordena los usuarios por su nombre

class Autor(models.Model):   # Modelo para los autores o clientes que hacen una peticion de trabajo
	nombre = models.CharField(max_length = 50)   # Nombre de los autores 
	correo = models.EmailField()   # Almacena el correo de los autores.

	def __str__(self):
		return self.nombre   # retorna el nombre del autor