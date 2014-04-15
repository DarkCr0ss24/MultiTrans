from django.shortcuts import render_to_response
from Utilidades.aside import UltimosTrabajos, UltimosProyectos
# Create your views here.

def Mostrar(request):
	trabajos = UltimosTrabajos()
	proyectos = UltimosProyectos()
	x = {"titulo":"MultiTrans","UltimosTrabajos":trabajos,"UltimosProyectos":proyectos}
	return render_to_response("index.html",x)