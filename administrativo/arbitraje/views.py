#!/usr/bin/python -u
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404,HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext, loader
from congresos.forms import TrabajosForm,TrabajosFormGuardar,TrabajosEditar,TrabajosFormGuardarArbitro
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from actores.models import Directorios,Bancoaudiovisuals,Bibliotecas
from congresos.models import Eventos,Trabajoscongresos,participacioEvento
from linea.models import Objetivoespecificos,Fundamentos,Accionesgenerales,Accionesespecificas
from django.contrib.auth.models import User
from perfil.models import PerfilPublico,ModulosPublicos,PerfilModulos
from plantillas.models import *
from mapas.models import Colaboradorespersonas
from datetime import *
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.db.models import Q
from django.conf import settings
from arbitraje.models import *
from arbitraje.forms import CambiarEstatusForm

def CambiarEstatus(request,id):
    _username = request.user.username
    try:
       id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
       id_usuario = None
    try:
       id_persona = PerfilPublico.objects.get(user=id_usuario.id)
    except PerfilPublico.DoesNotExist:
       id_persona = None
    try:
       persona = Directorios.objects.get(pk=id_persona.persona.id)
    except Directorios.DoesNotExist:
       persona = None
    try:
       arbitro = TrabajosArbitros.objects.get(pk=id)
    except TrabajosArbitros.DoesNotExist:
       arbitro = None 
    if request.method == 'POST':
       if arbitro:
          estatus = CambiarEstatusForm(request.POST, instance = arbitro)
          estatus.save()
          return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(arbitro.trabajos.id))
       else:
          return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(arbitro.trabajos.id))
    else:
       return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(arbitro.trabajos.id))
	   
def Historial(request,id):
    _username = request.user.username
    try:
       id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
       id_usuario = None
    try:
       id_persona = PerfilPublico.objects.get(user=id_usuario.id)
    except PerfilPublico.DoesNotExist:
       id_persona = None
    try:
       persona = Directorios.objects.get(pk=id_persona.persona.id)
    except Directorios.DoesNotExist:
       persona = None
    try:
       trabajos = Trabajoscongresos.objects.get(pk=id)
    except Trabajoscongresos.DoesNotExist:
       trabajos = None
    try:
       historial = HistorialModificacionesTrabajos.objects.filter(trabajos=trabajos)
    except HistorialModificacionesTrabajos.DoesNotExist:
       historial = None 
    return render_to_response("congresos/trabajos/historial.html",{'persona':persona,'historial':historial,'trabajos':trabajos}, context_instance=RequestContext(request)) 
