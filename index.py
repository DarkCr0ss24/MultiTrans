from django.shortcuts import render_to_response

# Create your views here.

def Mostrar(request):
	x = {"titulo":"MultiTrans"}
	return render_to_response("index.html",x)