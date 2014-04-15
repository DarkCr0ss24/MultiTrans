from Trabajos.models import *

def UltimosTrabajos():
	listaTrabajos = []
	contador = 0
	for i in TrabajoSencillo.objects.all():
		listaTrabajos.append(i)
		contador += 1
		if contador == 4:
			return listaTrabajos
	return TrabajoSencillo.objects.all()


def UltimosProyectos():
	listaProyectos = []
	contador = 0
	for i in Proyecto.objects.all():
		listaProyectos.append(i)
		contador += 1
		if contador == 4:
			return listaProyectos
	return Proyecto.objects.all()