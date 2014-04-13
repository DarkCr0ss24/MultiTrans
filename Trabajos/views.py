from django.shortcuts import render_to_response
from Trabajos.models import TrabajoSencillo, Proyecto
# Create your views here.

def mostrarTrabajos(request):
	return render_to_response('trabajos.html',{"trabajos":TrabajoSencillo.objects.all()})

def mostrarProyectos(request):
	return render_to_response('trabajos.html',{"trabajos":Proyecto.objects.all()})

def mostrarTrabajo(request, titulo):
	# Trabajo = TrabajoSencillo.objects.get(id=trabajo)
	trabajo = titulo.split("-")
	trabajo = " ".join(trabajo)
	for t in TrabajoSencillo.objects.all():
		if t.Titulo.lower() == trabajo.lower():
			return render_to_response('trabajo.html',{"trabajo":t})