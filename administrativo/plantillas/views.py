# -*- coding: utf8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from plantillas.models import *


def plataforma(request):
    id = 1
    try:
       plataforma = Templates.objects.get(pk=id)
    except Templates.DoesNotExist:
       plataforma = None
#    print plataforma.descripcion
    return render_to_response("pagina/plataforma.html",{'plataforma':plataforma}, context_instance=RequestContext(request))
	
def construccion(request):
    id = 3
    try:
       construccion = Templates.objects.get(pk=id)
    except Templates.DoesNotExist:
       construccion = None
#    print plataforma.descripcion
    return render_to_response("pagina/construccion.html",{'construccion':construccion}, context_instance=RequestContext(request))
	
def estrategia(request):
    id = 2
    try:
       estrategia = Templates.objects.get(pk=id)
    except Templates.DoesNotExist:
       estrategia = None
#    print plataforma.descripcion
    return render_to_response("pagina/estrategias.html",{'estrategia':estrategia}, context_instance=RequestContext(request))
	
def omg(request):
    id = 4
    try:
       omg = Templates.objects.get(pk=id)
    except Templates.DoesNotExist:
       omg = None
#    print plataforma.descripcion
    return render_to_response("pagina/omg.html",{'omg':omg}, context_instance=RequestContext(request))
	
def recob(request):
    id = 5
    try:
       recob = Templates.objects.get(pk=id)
    except Templates.DoesNotExist:
       recob = None
#    print plataforma.descripcion
    return render_to_response("pagina/recob.html",{'recob':recob}, context_instance=RequestContext(request))
	
def msiidb(request):
    id = 6
    try:
       msiidb = Templates.objects.get(pk=id)
    except Templates.DoesNotExist:
       msiidb = None
#    print plataforma.descripcion
    return render_to_response("pagina/msiidb.html",{'msiidb':msiidb}, context_instance=RequestContext(request))
