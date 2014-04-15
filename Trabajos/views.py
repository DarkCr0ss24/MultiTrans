from django.shortcuts import render_to_response
from Trabajos.models import TrabajoSencillo, Proyecto
from Utilidades.aside import UltimosTrabajos, UltimosProyectos
# Create your views here.

def mostrarTrabajos(request):
	return render_to_response('trabajos.html',{"trabajos":TrabajoSencillo.objects.all(),
											   "UltimosTrabajos":UltimosTrabajos(),
											   "UltimosProyectos":UltimosProyectos()})

def mostrarProyectos(request):
	return render_to_response('proyectos.html',{"trabajos":Proyecto.objects.all(), 
												"UltimosTrabajos":UltimosTrabajos(),
												"UltimosProyectos":UltimosProyectos()})

def mostrarTrabajo(request, titulo):
	# Trabajo = TrabajoSencillo.objects.get(id=trabajo)
	trabajo = titulo.split("-")
	trabajo = " ".join(trabajo)
	for t in TrabajoSencillo.objects.all():
		if t.Titulo.lower() == trabajo.lower():
			return render_to_response('trabajo.html',{"trabajo":t,
													  "UltimosTrabajos":UltimosTrabajos(),
													  "UltimosProyectos":UltimosProyectos()})

def mostrarProyecto(request, titulo):
	trabajo = titulo.split("-")
	trabajo = " ".join(trabajo)
	for t in Proyecto.objects.all():
		if t.Titulo.lower() == trabajo.lower():
			return render_to_response('proyecto.html',{"trabajo":t, 
													   "UltimosTrabajos":UltimosTrabajos(),
													   "UltimosProyectos":UltimosProyectos()})