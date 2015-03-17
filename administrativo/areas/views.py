# -*- coding: utf8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from actores.models import *
from areas.models import *
from perfil.models import SistemaSolicitudes
from plantillas.models import *
from menu.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from perfil.models import PerfilPublico,ModulosPublicos,PerfilModulos
from congresos.models import Eventos,Trabajoscongresos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from inicio.models import *
from mapas.models import *
from datetime import *

def ficha(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
		
    try:
        id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
        id_usuario = None
		
    try:
        id_persona = PerfilPublico.objects.get(user=id_usuario)
    except PerfilPublico.DoesNotExist:
        id_persona = None
		
    if id_persona == None:
       pp_id= None
    else:
       pp_id=id_persona.persona.id

    try:
        persona =  Directorios.objects.get(id=pp_id)
    except Directorios.DoesNotExist:
        persona = None 

    try:
        areas = Areas.objects.get(id=id)
    except Actores.DoesNotExist:
        areas = None
		
    try:
        redes = RedessocialesAreas.objects.filter(area=areas)
    except Redessociales.DoesNotExist:
        redes = None
		
    try:
        etnias = Etniaareas.objects.filter(area=areas)
    except Etniaareas.DoesNotExist:
        etnias = None
		
		
    try:
        categoria = Categorias.objects.get(id=areas.categoriact.id)
    except Categorias.DoesNotExist:
        categoria = None
		
    try:
        secciones = Secciones.objects.get(id=categoria.seccione.id)
    except Secciones.DoesNotExist:
        secciones = None
		
    try:
        sub = SubTipoCategorias.objects.get(id=areas.subtipoas.id)
    except SubTipoCategorias.DoesNotExist:
        sub = None

    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=secciones) & Q(subseccion=categoria)) | (Q(seccion=secciones) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None

    try:
        contribuciones = Colaboradorespersonas.objects.filter(areas=areas).order_by('update','estatu')
    except Colaboradorespersonas.DoesNotExist:
        contribuciones = None

    return render_to_response('areas/ficha.html', {'areas':areas,'categoria':categoria,'secciones':secciones,'sub':sub,'lateral':lateral,'redes':redes,'etnias':etnias,'persona':persona,'usuario':id_usuario,'contribuciones':contribuciones})
	