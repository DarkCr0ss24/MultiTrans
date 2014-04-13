from django.shortcuts import render_to_response
from Usuarios.models import Usuario
# Create your views here.

def mostrarUsuarios(request):
	return render_to_response('usuarios.html',{"usuarios":Usuario.objects.all()})

def mostrarUsuario(request, nombre):
	for usuario in Usuario.objects.all():
		if usuario.nombre.lower() == nombre.lower():
			return render_to_response("usuario.html",{"usuario":usuario})
