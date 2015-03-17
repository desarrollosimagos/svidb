# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('pagina/index.html')

def plataforma(request):
    return render_to_response('pagina/plataforma.html')

def colaboradores(request):
    return render_to_response('pagina/colaboradores.html')

def construccion(request):
    return render_to_response('pagina/construccion.html')
	
def estrategias(request):
    return render_to_response('pagina/estrategias.html')

def error(request):
    return render_to_response('503.html')
