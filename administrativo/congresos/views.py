#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response, get_object_or_404,HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext, loader
from congresos.forms import TrabajosForm,TrabajosFormGuardar,TrabajosEditar,TrabajosFormGuardarArbitro,EstatusPublicacion
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
from arbitraje.forms import *


def no_esta_logueado(user):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
        return True
    return False

def accesoValidacion():
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
    return persona
		
		
def ver_eventos(request,id):
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
       eventos_activos = Eventos.objects.get(pk= id)
    except Eventos.DoesNotExist:
       eventos_activos = None

    try:
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=38)
    except Categorias.DoesNotExist:
        sub = None
	   
    try:
        estatica = TemplatesEventos.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except TemplatesEventos.DoesNotExist:
        estatica = None

    try:
        estaticaid = TemplatesEventos.objects.filter(Q(evento=eventos_activos)).order_by('posicion')
    except TemplatesEventos.DoesNotExist:
        estaticaid = None

    return render_to_response("congresos/ver_eventos.html",{'congreso':eventos_activos,'persona':persona,'estaticaid':estaticaid}, context_instance=RequestContext(request))




def eventoslista(request):
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

    today = datetime.now() #fecha actual
    dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
    try:
       eventos_activos = Eventos.objects.filter(fecha__gt= dateFormat)
    except Eventos.DoesNotExist:
       eventos_activos = None

    try:
       eventos_realizados = Eventos.objects.filter(fecha__lt= dateFormat)
    except Eventos.DoesNotExist:
       eventos_realizados = None

    return render_to_response("congresos/eventoslistas.html",{'eventos_activos':eventos_activos,'realizados':eventos_realizados,'persona':persona}, context_instance=RequestContext(request))

def eventos_list(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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

       today = datetime.now() #fecha actual
       dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
       try:
          eventos_activos = Eventos.objects.filter(fecha__gt= dateFormat)
       except Eventos.DoesNotExist:
          eventos_activos = None
	   
       return render_to_response("congresos/eventos.html",{'eventos_activos':eventos_activos,'persona':persona}, context_instance=RequestContext(request))
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
	   
def eventos_activos_estadisticas(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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

       today = datetime.now() #fecha actual
       dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
       try:
          eventos_activos = Eventos.objects.filter(estatu=3)
       except Eventos.DoesNotExist:
          eventos_activos = None
	   
       return render_to_response("estadisticas/congresos/eventos.html",{'eventos_activos':eventos_activos,'persona':persona,'url':'/panel/estadisticas/eventos/activos/'}, context_instance=RequestContext(request))
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
def eventos_activos_arbitraje(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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

       today = datetime.now() #fecha actual
       dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
       try:
          eventos_activos = Eventos.objects.filter(fecha__gt= dateFormat)
       except Eventos.DoesNotExist:
          eventos_activos = None
		  
       try:
          arbitro =  arbitros.objects.get(arbitro=persona)
       except arbitros.DoesNotExist:
          arbitro = None
       try:
          coordinador2 = coordinador.objects.get(coordinador=persona)
       except coordinador.DoesNotExist:
          coordinador2 = None 
		  
       if arbitro or coordinador2:
          return render_to_response("congresos/trabajos/eventos.html",{'eventos_activos':eventos_activos,'persona':persona,'url':'/panel/arbitraje/eventos/activos/','url2':'/panel/coordinador/eventos/activos/','coordinador2':coordinador2}, context_instance=RequestContext(request))
       else:
          return HttpResponseRedirect("/eventos/listas")
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
def trabajos_eventos_arbitraje(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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
          arbitro =  arbitros.objects.get(Q(arbitro=persona) & Q(evento__id=id))
       except arbitros.DoesNotExist:
          arbitro = None
       try:
          trabajos =  TrabajosArbitros.objects.filter(Q(arbitro=arbitro) & Q(trabajos__evento__id=id)).order_by('-estatu')
       except TrabajosArbitros.DoesNotExist:
          trabajos = None
       if arbitro:
          return render_to_response("congresos/trabajos/lista.html",{'trabajos':trabajos,'persona':persona,'url':'/panel/eventos/trabajos/editar/','url2':'/panel/arbitraje/eventos/activos/filtro/','id':id,'url3':'/panel/arbitraje/eventos/activos/'}, context_instance=RequestContext(request))
       else:
          return HttpResponseRedirect("/eventos/listas")
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
def trabajos_eventos_arbitraje_filtro(request,id,st):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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
          arbitro =  arbitros.objects.get(Q(arbitro=persona) & Q(evento__id=id))
       except arbitros.DoesNotExist:
          arbitro = None
       try:
          trabajos =  TrabajosArbitros.objects.filter(Q(arbitro=arbitro) & Q(trabajos__evento__id=id) & Q(estatu=st)).order_by('-estatu')
       except TrabajosArbitros.DoesNotExist:
          trabajos = None
       if arbitro:
          return render_to_response("congresos/trabajos/lista.html",{'trabajos':trabajos,'persona':persona,'url':'/panel/eventos/trabajos/editar/','url2':'/panel/arbitraje/eventos/activos/filtro/','id':id,'url3':'/panel/arbitraje/eventos/activos/'}, context_instance=RequestContext(request))
       else:
          return HttpResponseRedirect("/eventos/listas")
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
	   
	   
def trabajos_eventos_coordinador(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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
          coordinador2 = coordinador.objects.get(Q(coordinador=persona) & Q(evento__id=id))
       except coordinador.DoesNotExist:
          coordinador2 = None 
		  
       try:
          arbitro = arbitros.objects.filter(evento__id=id)
       except arbitros.DoesNotExist:
          arbitro = None 
		  
       try:
          trabajos =  TrabajosArbitros.objects.filter(Q(trabajos__evento__id=id)).order_by('-estatu','-trabajos__estatu')
       except TrabajosArbitros.DoesNotExist:
          trabajos = None
       if coordinador2:
          return render_to_response("congresos/trabajos/lista.html",{'trabajos':trabajos,'persona':persona,'url':'/panel/eventos/trabajos/editar/','url2':'/panel/coordinador/eventos/activos/filtro/','id':id,'url3':'/panel/coordinador/eventos/activos/','arbitros':arbitro}, context_instance=RequestContext(request))
       else:
          return HttpResponseRedirect("/eventos/listas")
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
	   
	   
def listado_trabajos_publicacion(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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
          trabajos =  Trabajoscongresos.objects.filter(Q(evento__id=id) & Q(estatu=1) & Q(presento=True)).order_by('titulo')
       except Trabajoscongresos.DoesNotExist:
          trabajos = None
       return render_to_response("congresos/publicacion/lista.html",{'trabajos':trabajos,'persona':persona,'url':'/panel/eventos/trabajos/editar/','url2':'/panel/coordinador/eventos/activos/filtro/','id':id,'url3':'/panel/coordinador/eventos/activos/'}, context_instance=RequestContext(request))
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
	   
def listado_trabajos_publicacion2(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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
          trabajos =  Trabajoscongresos.objects.filter(Q(evento__id=id) & Q(estatu=1) & Q(presento=True)).order_by('titulo')
       except Trabajoscongresos.DoesNotExist:
          trabajos = None
       return render_to_response("congresos/publicacion/lista2.html",{'trabajos':trabajos,'persona':persona,'url':'/panel/eventos/trabajos/editar/','url2':'/panel/coordinador/eventos/activos/filtro/','id':id,'url3':'/panel/coordinador/eventos/activos/'}, context_instance=RequestContext(request))
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
	   
	   
def trabajos_eventos_coordinador_filtro_arbitro(request,id,id2):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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
          coordinador2 = coordinador.objects.get(Q(coordinador=persona) & Q(evento__id=id))
       except coordinador.DoesNotExist:
          coordinador2 = None 
		  
       try:
          arbitro = arbitros.objects.filter(evento__id=id)
       except arbitros.DoesNotExist:
          arbitro = None 
		  
       try:
          arbitro2 = arbitros.objects.get(id=id2)
       except arbitros.DoesNotExist:
          arbitro2 = None 
		  
       try:
          trabajos =  TrabajosArbitros.objects.filter(Q(trabajos__evento__id=id) & Q(arbitro__id=id2)).order_by('-estatu','-trabajos__estatu')
       except TrabajosArbitros.DoesNotExist:
          trabajos = None
       if coordinador2:
          return render_to_response("congresos/trabajos/lista.html",{'trabajos':trabajos,'persona':persona,'url':'/panel/eventos/trabajos/editar/','url2':'/panel/coordinador/eventos/activos/filtro/','id':id,'url3':'/panel/coordinador/eventos/activos/','arbitros':arbitro,'arbitro2':arbitro2}, context_instance=RequestContext(request))
       else:
          return HttpResponseRedirect("/eventos/listas")
    else:
       return HttpResponseRedirect("/eventos/listas")
       
def trabajos_eventos_coordinador_filtro(request,id,st):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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
          arbitro = arbitros.objects.filter(evento__id=id)
       except arbitros.DoesNotExist:
          arbitro = None 
		  

       try:
          coordinador2 = coordinador.objects.get(Q(coordinador=persona) & Q(evento__id=id))
       except coordinador.DoesNotExist:
          coordinador2 = None 
		  
       try:
          trabajos =  TrabajosArbitros.objects.filter(Q(trabajos__evento__id=id) & Q(estatu=st)).order_by('-estatu','-trabajos__estatu')
       except TrabajosArbitros.DoesNotExist:
          trabajos = None
       if coordinador2:
          return render_to_response("congresos/trabajos/lista.html",{'trabajos':trabajos,'persona':persona,'url':'/panel/eventos/trabajos/editar/','url2':'/panel/coordinador/eventos/activos/filtro/','id':id,'url3':'/panel/coordinador/eventos/activos/','arbitros':arbitro}, context_instance=RequestContext(request))
       else:
          return HttpResponseRedirect("/eventos/listas")
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
def trabajos_eventos_coordinador_filtro_arbitro2(request,id,st,id2):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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
          coordinador2 = coordinador.objects.get(Q(coordinador=persona) & Q(evento__id=id))
       except coordinador.DoesNotExist:
          coordinador2 = None 
       try:
          arbitro = arbitros.objects.filter(evento__id=id)
       except arbitros.DoesNotExist:
          arbitro = None 
		  
       try:
          arbitro2 = arbitros.objects.get(id=id2)
       except arbitros.DoesNotExist:
          arbitro2 = None 
       try:
          trabajos =  TrabajosArbitros.objects.filter(Q(trabajos__evento__id=id) & Q(estatu=st) & Q(arbitro__id=id2)).order_by('-estatu','-trabajos__estatu')
       except TrabajosArbitros.DoesNotExist:
          trabajos = None
       if coordinador2:
          return render_to_response("congresos/trabajos/lista.html",{'trabajos':trabajos,'persona':persona,'url':'/panel/eventos/trabajos/editar/','url2':'/panel/coordinador/eventos/activos/filtro/','id':id,'url3':'/panel/coordinador/eventos/activos/','arbitros':arbitro,'arbitro2':arbitro2}, context_instance=RequestContext(request))
       else:
          return HttpResponseRedirect("/eventos/listas")
    else:
       return HttpResponseRedirect("/eventos/listas")
	   
def eventos_activos_estadisticas2(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if _username:
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
          eventos_activos = Eventos.objects.get(pk=id)
       except Eventos.DoesNotExist:
          eventos_activos = None
	   
       return render_to_response("estadisticas/congresos/eventos2.html",{'eventos_activos':eventos_activos,'persona':persona}, context_instance=RequestContext(request))
    else:
       return HttpResponseRedirect("/eventos/listas")
	
def ver_congresos(request,id):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
    try:
       id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
       id_usuario = None
    print id_usuario
    try:
       id_persona = PerfilPublico.objects.get(user=id_usuario.id)
    except PerfilPublico.DoesNotExist:
       id_persona = None
    print id_persona
    try:
       persona = Directorios.objects.get(pk=id_persona.persona.id)
    except Directorios.DoesNotExist:
       persona = None
    print persona
    try:
       eventos_activos = Eventos.objects.get(pk= id)
    except Eventos.DoesNotExist:
       eventos_activos = None
    try:
       trabajos = Trabajoscongresos.objects.filter(evento= eventos_activos).filter(directorio=persona)
    except Trabajoscongresos.DoesNotExist:
       trabajos = None
    try:
       participa = participacioEvento.objects.filter(evento=id).filter(directorio=id_persona.persona.id)
    except participacioEvento.DoesNotExist:
       participa = None
	   
    today = datetime.now() #fecha actual
    dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
	
    if eventos_activos.fechaInicioInscripcion : 
       fecha1 = eventos_activos.fechaInicioInscripcion
       fecha11 = fecha1.strftime("%Y-%m-%d")
    else :
       fecha1 = None
	   
    if fecha11 >= dateFormat :
       activoins = True
    else:
       activoins = False
	   
    if eventos_activos.fechaInicioInscripcion : 
       fecha2 = eventos_activos.fechaFinInscripcion
       fecha22 = fecha2.strftime("%Y-%m-%d")
    else :
       fecha2 = None
	   
    if fecha22 >= dateFormat :
       activopos = True
    else:
       activopos = False
	   
    return render_to_response("congresos/ver_congresos.html",{'trabajos':trabajos,'congreso':eventos_activos,'persona':persona,'participa':participa,'activoins':activoins,'activopos':activopos}, context_instance=RequestContext(request))
	

def ver_todos_trabajos(request):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
    try:
       id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
       id_usuario = None
    print id_usuario
    try:
       id_persona = PerfilPublico.objects.get(user=id_usuario.id)
    except PerfilPublico.DoesNotExist:
       id_persona = None
    print id_persona
    try:
       persona = Directorios.objects.get(pk=id_persona.persona.id)
    except Directorios.DoesNotExist:
       persona = None
    try:
       trabajos = Trabajoscongresos.objects.filter(Q(coautores=persona) | Q(directorio=persona)).filter(estatu=0).order_by('evento')
    except Trabajoscongresos.DoesNotExist:
       trabajos = None
    try:
       parti = participacioEvento.objects.filter(directorio=persona).order_by('evento')
    except participacioEvento.DoesNotExist:
       parti = None

    try:
       constr = Colaboradorespersonas.objects.filter(persona=persona).filter(estatu=0).order_by('tipoColaboracion')
    except Colaboradorespersonas.DoesNotExist:
       constr = None
    try:
       banco = Bancoaudiovisuals.objects.filter(directorio=persona).filter(Q(estatu=1) | Q(estatu=2))
    except Bancoaudiovisuals.DoesNotExist:
       banco = None
    try:
        biblioteca = Bibliotecas.objects.filter(directorio=persona).filter(estatu=0).order_by('titulo')
    except Bibliotecas.DoesNotExist:
        biblioteca = None
	   
    return render_to_response("congresos/ver_congresos_todos.html",{'trabajos':trabajos,'persona':persona,'banco':banco,'constr':constr,'parti':parti,'biblioteca':biblioteca}, context_instance=RequestContext(request))


def seleccionfundamentos(request,id):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
    try:
       id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
       id_usuario = None
    print id_usuario
    try:
       id_persona = PerfilPublico.objects.get(user=id_usuario.id)
    except PerfilPublico.DoesNotExist:
       id_persona = None
    print id_persona
    try:
       persona = Directorios.objects.get(pk=id_persona.persona.id)
    except Directorios.DoesNotExist:
       persona = None
    try:
       eventos_activos = Eventos.objects.get(pk= id)
    except Eventos.DoesNotExist:
       eventos_activos = None
    fundada = Fundamentos.objects.all().order_by('tipo__tipo','numero')
    return render_to_response("congresos/fundamentos.html",{'funda':fundada,'congreso':eventos_activos,'persona':persona}, context_instance=RequestContext(request))
		
		
def objetivosespecificos(request,id,fund):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
    try:
       id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
       id_usuario = None
    print id_usuario
    try:
       id_persona = PerfilPublico.objects.get(user=id_usuario.id)
    except PerfilPublico.DoesNotExist:
       id_persona = None
    print id_persona
    try:
       persona = Directorios.objects.get(pk=id_persona.persona.id)
    except Directorios.DoesNotExist:
       persona = None
    try:
       eventos_activos = Eventos.objects.get(pk= id)
    except Eventos.DoesNotExist:
       eventos_activos = None
    objespicific = Objetivoespecificos.objects.filter(fundamento=fund).order_by('numero')
    return render_to_response("congresos/objetivos.html",{'objespicific':objespicific,'congreso':eventos_activos,'persona':persona}, context_instance=RequestContext(request))	
	
def accionesgenerales(request,id,acc):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
    try:
       id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
       id_usuario = None
    print id_usuario
    try:
       id_persona = PerfilPublico.objects.get(user=id_usuario.id)
    except PerfilPublico.DoesNotExist:
       id_persona = None
    print id_persona
    try:
       persona = Directorios.objects.get(pk=id_persona.persona.id)
    except Directorios.DoesNotExist:
       persona = None
    try:
       eventos_activos = Eventos.objects.get(pk= id)
    except Eventos.DoesNotExist:
       eventos_activos = None
    accgen = Accionesgenerales.objects.filter(objetivoespecifico=acc)
    return render_to_response("congresos/accionesgenerales.html",{'accgen':accgen,'congreso':eventos_activos,'persona':persona}, context_instance=RequestContext(request))		
		
def accionesespecificas(request,id,ace):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
    try:
       id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
       id_usuario = None
    print id_usuario
    try:
       id_persona = PerfilPublico.objects.get(user=id_usuario.id)
    except PerfilPublico.DoesNotExist:
       id_persona = None
    print id_persona
    try:
       persona = Directorios.objects.get(pk=id_persona.persona.id)
    except Directorios.DoesNotExist:
       persona = None
    try:
       eventos_activos = Eventos.objects.get(pk= id)
    except Eventos.DoesNotExist:
       eventos_activos = None
    accespe = Accionesespecificas.objects.filter(accionesgenerale=ace)
    return render_to_response("congresos/accionesespecificas.html",{'accespe':accespe,'congreso':eventos_activos,'persona':persona}, context_instance=RequestContext(request))		
		

def form_trabajos(request,id):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
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
       eventos_activos = Eventos.objects.get(pk= id)
    except Eventos.DoesNotExist:
       eventos_activos = None
    #try:
    #   objetivos = Accionesespecificas.objects.get(pk= item)
    #except Accionesespecificas.DoesNotExist:
    #   objetivos=None
	   

    if request.method == 'POST':
       trabajos_post = TrabajosFormGuardar(request.POST)
       if trabajos_post.is_valid():
          trabajo = trabajos_post.save()
          id = trabajo.id
          subject, from_email, to = 'SVIDB Registro de Resumen', settings.EMAIL_HOST_USER, persona.correo
          text_content = 'SVIDB Registro de Resumen'
          d= settings.URL_SET_SITE
          ctx_dict = {'nombre': persona.nombre, 'apellido':persona.apellido,'d': id,'congreso':eventos_activos.nombre,'titulo':trabajo.titulo,'modalidad':trabajo.modalidad.nombre}
          html_content= render_to_string('correos/plantillas/eventos/resumen.txt',ctx_dict)
          msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
          msg.attach_alternative(html_content, "text/html")
          try:
              msg.send()
          except Exception, e:
              error = True
          return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(id))
          #return render_to_response("congresos/exito.html",{'eventos_activos':eventos_activos}, context_instance=RequestContext(request))    
       else:
          trabajos = TrabajosFormGuardar(request.POST)
          return render_to_response("congresos/registro_trabajos.html",{'formulario':trabajos,'persona':persona,'eventos_activos':eventos_activos}, context_instance=RequestContext(request))    
    else:
       trabajos = TrabajosFormGuardar()
       return render_to_response("congresos/registro_trabajos.html",{'formulario':trabajos,'persona':persona,'eventos_activos':eventos_activos}, context_instance=RequestContext(request))
	   

def form_editar(request,id):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
    
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
       Trabajoscong = Trabajoscongresos.objects.get(pk= id)
    except Trabajoscongresos.DoesNotExist:
       Trabajoscong = None
    tituloAntes = Trabajoscong.titulo
    resumenAntes = Trabajoscong.resumen
    modalidadAntes = Trabajoscong.modalidad
    accespecifiAntes = Trabajoscong.accespecifi
    tematicasAntes = Trabajoscong.tematicas   
    autor = None
    arbitro = None
    trabajosArbitrajes = None
    formEstatus = None
    coordinador2 = None
    asignado = None
    formPublicacion = None
    if Trabajoscong.directorio == persona :
       autor = True
       try:
          asignado = TrabajosArbitros.objects.get(trabajos=Trabajoscong)
       except TrabajosArbitros.DoesNotExist:
          asignado = None 
    else:
       try:
          asignado = TrabajosArbitros.objects.get(trabajos=Trabajoscong)
       except TrabajosArbitros.DoesNotExist:
          asignado = None 
       try:
          arbitro = TrabajosArbitros.objects.get(Q(arbitro__arbitro=persona) & Q(trabajos=Trabajoscong))
       except TrabajosArbitros.DoesNotExist:
          arbitro = None 
       try:
          coordinador2 = coordinador.objects.get(coordinador=persona)
       except coordinador.DoesNotExist:
          coordinador2 = None 
		  
       if arbitro and coordinador2 :
          formEstatus =  CambiarEstatusForm(instance = asignado)
          formPublicacion = EstatusPublicacion(instance = Trabajoscong)
       else:
          if arbitro:
             formEstatus =  CambiarEstatusForm(instance = asignado)
          if coordinador2:
             formEstatus =  CambiarEstatusForm(instance = asignado)
             formPublicacion = EstatusPublicacion(instance = Trabajoscong)
    if autor or arbitro or coordinador2:
       acceso = True
    else:
       return HttpResponseRedirect("/perfil")

    try:
       mensajes = MensajeTrabajosArbitraje.objects.filter(trabajos=Trabajoscong)
    except MensajeTrabajosArbitraje.DoesNotExist:
       mensajes = None
    if request.method == 'POST':
       if arbitro or coordinador2:
          trabajos = TrabajosFormGuardarArbitro(request.POST, instance = Trabajoscong)
       else:
          trabajos = TrabajosFormGuardar(request.POST, instance = Trabajoscong)
       if trabajos.is_valid():
          trabajoDespues = trabajos.save()
          #variables del Historial
          if tituloAntes == trabajoDespues.titulo:
             cambios = HistorialModificacionesTrabajos(userupdate=id_persona,campo='Titulo',modificacion=tituloAntes,trabajos=Trabajoscong)
             cambios.save()
          else:
             cambios = HistorialModificacionesTrabajos(userupdate=id_persona,campo='Titulo',modificacion=tituloAntes,trabajos=Trabajoscong)
             cambios.save()
			 
          if resumenAntes == trabajoDespues.resumen:
             noCambios = True
          else:
             cambios = HistorialModificacionesTrabajos(userupdate=id_persona,campo='Resumen',modificacion=resumenAntes,trabajos=Trabajoscong)
             cambios.save()
			 
          if modalidadAntes == trabajoDespues.modalidad:
             noCambios = True
          else:
             cambios = HistorialModificacionesTrabajos(userupdate=id_persona,campo='Modalidad',modificacion=str(modalidadAntes),trabajos=Trabajoscong)
             cambios.save()
			 
          if accespecifiAntes == trabajoDespues.accespecifi:
             noCambios = True
          else:
             cambios = HistorialModificacionesTrabajos(userupdate=id_persona,campo='Acción Especifica',modificacion= str(accespecifiAntes),trabajos=Trabajoscong)
             cambios.save()
			 
          if tematicasAntes == trabajoDespues.tematicas:
             noCambios = True
          else:
             cambios = HistorialModificacionesTrabajos(userupdate=id_persona,campo='Tematica',modificacion= str(tematicasAntes),trabajos=Trabajoscong)
             cambios.save()
          if arbitro or coordinador2:
#             trabajos = TrabajosFormGuardarArbitro(instance = Trabajoscong)
             formEstatus =  CambiarEstatusForm(instance = asignado)
             formPublicacion = EstatusPublicacion(instance = Trabajoscong)
#          else:
#             trabajos = TrabajosFormGuardar(instance=Trabajoscong)
          try:
              historial = HistorialModificacionesTrabajos.objects.filter(trabajos=Trabajoscong).order_by('-update')[:10]
          except HistorialModificacionesTrabajos.DoesNotExist:
              historial = None
          return render_to_response("congresos/editar.html",{'formulario':trabajos,'trab':Trabajoscong,'persona':persona,'mensajes':mensajes,'arbitro':arbitro,'historial':historial,'trabajosArbitrajes':trabajosArbitrajes,'formEstatus':formEstatus,'asignado':asignado,'coordinador2':coordinador2,'formPublicacion':formPublicacion,'error':'no'}, context_instance=RequestContext(request)) 
       else:
          if arbitro or coordinador2:
#             trabajos = TrabajosFormGuardarArbitro(instance = Trabajoscong)
             formEstatus =  CambiarEstatusForm(instance = asignado)
             formPublicacion = EstatusPublicacion(instance = Trabajoscong)
#          else:
#             trabajos = TrabajosFormGuardar(instance=Trabajoscong)
          try:
              historial = HistorialModificacionesTrabajos.objects.filter(trabajos=Trabajoscong).order_by('-update')[:10]
          except HistorialModificacionesTrabajos.DoesNotExist:
              historial = None
          return render_to_response("congresos/editar.html",{'formulario':trabajos,'trab':Trabajoscong,'persona':persona,'mensajes':mensajes,'arbitro':arbitro,'historial':historial,'trabajosArbitrajes':trabajosArbitrajes,'formEstatus':formEstatus,'asignado':asignado,'coordinador2':coordinador2,'formPublicacion':formPublicacion,'error':'si'}, context_instance=RequestContext(request))
    else:
       if arbitro or coordinador2:
          trabajos = TrabajosFormGuardarArbitro(instance = Trabajoscong)
          formEstatus =  CambiarEstatusForm(instance = asignado)
          formPublicacion = EstatusPublicacion(instance = Trabajoscong)
       else:
          trabajos = TrabajosFormGuardar(instance=Trabajoscong)
       try:
           historial = HistorialModificacionesTrabajos.objects.filter(trabajos=Trabajoscong).order_by('-update')[:10]
       except HistorialModificacionesTrabajos.DoesNotExist:
           historial = None
       return render_to_response("congresos/editar.html",{'formulario':trabajos,'trab':Trabajoscong,'persona':persona,'mensajes':mensajes,'arbitro':arbitro,'historial':historial,'trabajosArbitrajes':trabajosArbitrajes,'formEstatus':formEstatus,'asignado':asignado,'coordinador2':coordinador2,'formPublicacion':formPublicacion}, context_instance=RequestContext(request))
	   
def mensajesArbitraje(request,id):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
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
       Trabajoscong = Trabajoscongresos.objects.get(pk= id)
    except Trabajoscongresos.DoesNotExist:
       Trabajoscong = None
    try:
       arbitro = TrabajosArbitros.objects.get(Q(arbitro__arbitro=persona) & Q(trabajos=Trabajoscong))
    except TrabajosArbitros.DoesNotExist:
       arbitro = None
    try:
       coordinador2 = coordinador.objects.get(coordinador=persona)
    except coordinador.DoesNotExist:
       coordinador2 = None
	    
    if request.method == 'POST':
       if Trabajoscong:
          mensajes = MensajeTrabajosArbitraje(userupdate=id_persona,mensaje=request.POST['mensajes'],trabajos=Trabajoscong)
          mensajes.save()
          text_content = 'SVIDB - Nuevo mensaje de Arbitraje'
          d= settings.URL_SET_SITE
          if arbitro:
             subject, from_email, to = 'SVIDB - Nuevo mensaje de Arbitraje', settings.EMAIL_HOST_USER, mensajes.trabajos.directorio.correo
             ctx_dict = {'sexo':publicacion.directorio.sexo,'nombre': mensajes.trabajos.directorio.nombre, 'apellido':mensajes.trabajos.directorio.apellido,'d':d,'congreso':mensajes.trabajos.evento.nombre,'titulo':mensajes.trabajos.titulo,'mensajes':mensajes.mensaje,'id':mensajes.trabajos.id}
             html_content= render_to_string('correos/plantillas/eventos/mensaje.txt',ctx_dict)
             msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
             msg.attach_alternative(html_content, "text/html")
             msg.send()
          else:
             try:
               arbitro2 = TrabajosArbitros.objects.get(trabajos=Trabajoscong)
             except TrabajosArbitros.DoesNotExist:
               arbitro2 = None 
             if arbitro2:
                subject, from_email, to = 'SVIDB - Nuevo mensaje de Arbitraje', settings.EMAIL_HOST_USER, arbitro2.arbitro.arbitro.correo
                ctx_dict = {'nombre': arbitro2.arbitro.arbitro.nombre, 'apellido':arbitro2.arbitro.arbitro.apellido,'d':d,'congreso':mensajes.trabajos.evento.nombre,'titulo':mensajes.trabajos.titulo,'mensajes':mensajes.mensaje,'id':mensajes.trabajos.id}
                html_content= render_to_string('correos/plantillas/eventos/mensaje.txt',ctx_dict)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
          return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(id))
       else:
          return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(id))
    else:
       return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(id))
    

def patrticipacion(request,id):
    _username = request.user.username
    if _username:
       login = True
    else:
       return HttpResponseRedirect("/perfil")
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
       evento = Eventos.objects.get(pk= id)
    except Eventos.DoesNotExist:
       evento = None  
    try:
       registro = participacioEvento(directorio=persona,evento=evento,estatu=2) 
       registro.save()
       op=True
    except Eventos.DoesNotExist:
       op=False
    return render_to_response("congresos/parti.html",{'op':op}, context_instance=RequestContext(request))
	
	
def CambiarEstatusPublicacion(request,id):
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
       publicacion = Trabajoscongresos.objects.get(pk=id)
    except Trabajoscongresos.DoesNotExist:
       publicacion = None 
    if request.method == 'POST':
       if publicacion:
          estatus = EstatusPublicacion(request.POST, instance = publicacion)
          estatus.save()
          text_content = 'SVIDB - Nuevo mensaje de Arbitraje'
          d= settings.URL_SET_SITE
          if publicacion.estatu == 1:
             subject, from_email, to = 'SVIDB - Nuevo mensaje de Arbitraje', settings.EMAIL_HOST_USER, publicacion.directorio.correo
             ctx_dict = {'nombre': publicacion.directorio.nombre, 'apellido':publicacion.directorio.apellido,'d':d,'congreso':publicacion.evento.nombre,'titulo':publicacion.titulo,'mensajes':'Su Trabajo ha sido Aprobado','id':publicacion.id}
             html_content= render_to_string('correos/plantillas/eventos/mensaje2.txt',ctx_dict)
             msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
             msg.attach_alternative(html_content, "text/html")
             msg.send()
          if publicacion.estatu == 2:
             subject, from_email, to = 'SVIDB - Nuevo mensaje de Arbitraje', settings.EMAIL_HOST_USER, publicacion.directorio.correo
             ctx_dict = {'sexo':publicacion.directorio.sexo,'nombre': publicacion.directorio.nombre, 'apellido':publicacion.directorio.apellido,'d':d,'congreso':publicacion.evento.nombre,'titulo':publicacion.titulo,'mensajes':'Su Trabajo ha sido Aprobado','id':publicacion.id}
             html_content= render_to_string('correos/plantillas/eventos/mensaje3.txt',ctx_dict)
             msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
             msg.attach_alternative(html_content, "text/html")
             msg.send()
          return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(publicacion.id))
       else:
          return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(publicacion.id))
    else:
       return HttpResponseRedirect("/panel/eventos/trabajos/editar/" + str(publicacion.id))
	   
def previsualizarTrabajos(request,id):
    _username = request.user.username
    if _username : 
       try:
           publicacion = Trabajoscongresos.objects.get(pk=id)
       except Trabajoscongresos.DoesNotExist:
           publicacion = None 
       if publicacion:
          return render_to_response("congresos/trabajos/preview.html",{'publicacion':publicacion}, context_instance=RequestContext(request))
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")


def ListadoInscritos(request,id):
    _username = request.user.username
    if _username :
       try:
           eventos = Eventos.objects.get(pk= id)
       except Eventos.DoesNotExist:
           eventos = None 
       try:
           listados = participacioEvento.objects.filter(Q(evento=eventos) & Q(estatu=3))
       except participacioEvento.DoesNotExist:
           listados = None 
       if listados:
          return render_to_response("congresos/trabajos/listados.html",{'listados':listados,'eventos':eventos}, context_instance=RequestContext(request))
       else:
          return HttpResponseRedirect("/perfil")
    else:
       return HttpResponseRedirect("/perfil")


