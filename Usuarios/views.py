from django.shortcuts import render_to_response
from Usuarios.models import Usuario
from Utilidades.aside import UltimosTrabajos, UltimosProyectos
# Create your views here.

def mostrarUsuarios(request):
	return render_to_response('usuarios.html',{"usuarios":Usuario.objects.all(),
											   "UltimosTrabajos":UltimosTrabajos(),
											   "UltimosProyectos":UltimosProyectos()})

def mostrarUsuario(request, nombre):
	for usuario in Usuario.objects.all():
		if usuario.nombre.lower() == nombre.lower():
			return render_to_response("usuario.html",{"usuario":usuario,
													  "UltimosTrabajos":UltimosTrabajos(),
													  "UltimosProyectos":UltimosProyectos()})
