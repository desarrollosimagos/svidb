#!/usr/bin/python -u
# -*- coding: utf-8 -*-
import hashlib
import random
import re
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render_to_response, get_object_or_404,HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from congresos.models import Eventos,Trabajoscongresos,participacioEvento
from django.contrib.auth.models import User
from perfil.models import PerfilPublico,ModulosPublicos,PerfilModulos
from mogie.acceso import accesoValidacion
from django.db.models import *
from models import *
from forms import *
from actores.forms import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
from django.utils import simplejson
from django.http import HttpResponse


def admin(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username)
    if resultado:
       return render_to_response("mogie/admin/panel.html",{'usuario':resultado,'perfil':perfil},context_instance=RequestContext(request))
    else:
       return render_to_response("mogie/admin/index.html",{'usuario':resultado,'perfil':perfil},context_instance=RequestContext(request))
       
def publico(request):
    today = datetime.now() #fecha actual
    dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
    try:
       eventos_activos = Eventos.objects.filter(fecha__gt= dateFormat)
       eventos_activos = eventos_activos.filter()
    except Eventos.DoesNotExist:
       eventos_activos = None
       
    try:
       patrocinadores = ConfiguracionIndexPatrocinador.objects.filter().order_by('id')
    except ConfiguracionIndexPatrocinador.DoesNotExist:
       patrocinadores = None
       
    try:
       eventos = Eventos.objects.filter(eventpadre=None).order_by('fecha')
    except Eventos.DoesNotExist:
       eventos = None
       
    try:
       comentarios = ComentariosModulo.objects.filter().order_by('-id')[:10]
    except ComentariosModulo.DoesNotExist:
       comentarios = None
       
    try:
       participacion = participacioEvento.objects.filter(evento__eventpadre=None).order_by('-evento')
       participacion = participacion.values('evento__nombre').annotate(Count('evento'))[:10]
    except participacioEvento.DoesNotExist:
       participacion = None
       
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username)
    return render_to_response("mogie/publico/index.html",{'congreso':eventos,'participacion':participacion,'patrocinadores':patrocinadores,'usuario':resultado,'perfil':perfil,'comentarios':comentarios},context_instance=RequestContext(request))
    

def eventos(request,id):  
    try:
       eventos = Eventos.objects.filter(eventpadre=None).order_by('-fecha')
    except Eventos.DoesNotExist:
       eventos = None
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    
    if len(eventos) == 0:
       mesn=None
    else:
        paginator = Paginator(eventos, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)
    
    resultado,perfil = accesoValidacion(_username)
    return render_to_response("mogie/publico/eventos/eventos.html",{'eventos':eventos,'usuario':resultado,'perfil':perfil,'mesn':mesn,'hoy':date.today()},context_instance=RequestContext(request))
    
def eventosActivos(request,id):  
    try:
       eventos = Eventos.objects.filter(eventpadre=None).order_by('-fecha')
       eventos = eventos.filter(estatu=0)
    except Eventos.DoesNotExist:
       eventos = None
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    
    if len(eventos) == 0:
       mesn=None
    else:
        paginator = Paginator(eventos, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)
    
    resultado,perfil = accesoValidacion(_username)
    return render_to_response("mogie/publico/eventos/eventos.html",{'eventos':eventos,'usuario':resultado,'perfil':perfil,'mesn':mesn,'hoy':date.today()},context_instance=RequestContext(request))
    
def eventosProximos(request,id):  
    try:
       eventos = Eventos.objects.filter(eventpadre=None).order_by('-fecha')
       eventos = eventos.filter(estatu=2)
    except Eventos.DoesNotExist:
       eventos = None
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    
    if len(eventos) == 0:
       mesn=None
    else:
        paginator = Paginator(eventos, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)
    
    resultado,perfil = accesoValidacion(_username)
    return render_to_response("mogie/publico/eventos/eventos.html",{'eventos':eventos,'usuario':resultado,'perfil':perfil,'mesn':mesn,'hoy':date.today()},context_instance=RequestContext(request))
    
def eventosRealizados(request,id):  
    try:
       eventos = Eventos.objects.filter(eventpadre=None).order_by('-fecha')
       eventos = eventos.filter(estatu=3)
    except Eventos.DoesNotExist:
       eventos = None
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    
    if len(eventos) == 0:
       mesn=None
    else:
        paginator = Paginator(eventos, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)
    
    resultado,perfil = accesoValidacion(_username)
    return render_to_response("mogie/publico/eventos/eventos.html",{'eventos':eventos,'usuario':resultado,'perfil':perfil,'mesn':mesn,'hoy':date.today()},context_instance=RequestContext(request))
    
def logout(request):
    auth.logout(request)
    # Redirigir a una pagina de exito.
    return HttpResponseRedirect("/mogie")
    
def indexvs2(request):
    return render_to_response("mogie/publico/index2.html",context_instance=RequestContext(request))
    
    
def editarPerfilUsuario(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username)
    if request.method == 'POST':
    	formulario_personas = GuardarDatosDirectorios(request.POST,instance = perfil.persona)
    	if formulario_personas.is_valid():
    		formulario_personas.save()
    		return HttpResponseRedirect("/mogie/perfil")
    	else:
    		formulario_perfil_foto = GuardarFoto(instance = resultado)
    		return render_to_response("mogie/publico/perfil/index.html",{'usuario':resultado,'perfil':perfil,'formulario_extension':formulario_perfil_foto,'formulario_personas':formulario_personas},context_instance=RequestContext(request))
    else:
	    if perfil is None:
	       return HttpResponseRedirect("/mogie")
	    if resultado:
	       formulario_perfil_foto = GuardarFoto(instance = resultado)
	       formulario_personas = GuardarDatosDirectorios(instance = perfil.persona)
	       return render_to_response("mogie/publico/perfil/index.html",{'usuario':resultado,'perfil':perfil,'formulario_extension':formulario_perfil_foto,'formulario_personas':formulario_personas},context_instance=RequestContext(request))
	    else:
	       configurar_perfil = ExtensionPerfilUsuario(perfil=perfil)
	       configurar_perfil.save()
	       resultado,perfil = accesoValidacion(_username)
	       formulario_perfil_foto = GuardarFoto(instance = resultado)
	       formulario_personas = GuardarDatosDirectorios(instance = perfil.persona)
	       return render_to_response("mogie/publico/perfil/index.html",{'usuario':resultado,'perfil':perfil,'formulario_extension':formulario_perfil_foto,'formulario_personas':formulario_personas},context_instance=RequestContext(request))
       
def GuardarPerfil(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if request.method == 'POST':
       resultado,perfil = accesoValidacion(_username)
       formulario_personas = GuardarDatosDirectorios(request.POST,instance = perfil.persona)
       if formulario_personas.is_valid():
          formulario_personas.save()
          return HttpResponseRedirect("/mogie/perfil")
       else:
          return HttpResponseRedirect("/mogie/perfil1")
    else:
       return HttpResponseRedirect("/mogie/perfil")
    
    
def IniciarSesion(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password=password)
       if user is not None and user.is_active:
          # Clave correcta, y el usuario esta marcado "activo"
          auth.login(request, user)
          return HttpResponseRedirect("/mogie")
       else:
          # Mostrar una pagina de error
          return HttpResponseRedirect("/mogie/admin")
    else:
       return HttpResponseRedirect("/mogie/admin")
       
def agregarComentario(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    if request.method == 'POST':
       comentario = request.POST['comentario']
       resultado,perfil = accesoValidacion(_username)
       comentarios = ComentariosModulo(perfil=resultado,comentario=comentario)
       comentarios.save()
       return HttpResponseRedirect("/mogie")
    else:
       return HttpResponseRedirect("/mogie")
       
def agregarFotoPerfil(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username)    
    if request.method == 'POST':
       formulario_perfil_foto = GuardarFoto(request.POST,request.FILES,instance = resultado)
       if formulario_perfil_foto.is_valid():
          formulario_perfil_foto.save()
          return HttpResponseRedirect("/mogie/perfil")
       else:
          return HttpResponseRedirect("/mogie/perfil")
    else:
       return HttpResponseRedirect("/mogie/perfil")
       
def verEvento(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username)  
    
    try:
       eventos = Eventos.objects.get(pk=id)
    except Eventos.DoesNotExist:
       eventos = None   
       
    if resultado:
       return render_to_response('mogie/publico/eventos/index.html',{'eventos':eventos,'cursos':cursos,'resultado':resultado}, context_instance=RequestContext(request))
    else:
       return render_to_response('mogie/publico/eventos/index.html',{'eventos':eventos,'cursos':cursos}, context_instance=RequestContext(request))
       
       
def detalleEvento(request,id):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    if not resultado:
       return HttpResponseRedirect("/mogie") 
    try:
       eventos = Eventos.objects.get(pk=id)
    except Eventos.DoesNotExist:
       eventos = None  
       
    try:
       trabajosAutor = Trabajoscongresos.objects.filter(Q(directorio=perfil.persona) & Q(evento=eventos))
    except Trabajoscongresos.DoesNotExist:
       trabajosAutor = None
       
    try:
       trabajoscoautor = RelacionPersonasTrabajos.objects.filter(Q(personas=perfil.persona) & Q(trabajo__evento=eventos))
    except RelacionPersonasTrabajos.DoesNotExist:
       trabajoscoautor = None
    
    try:
       participacion = participacioEvento.objects.get(Q(evento=eventos) & Q(directorio=perfil.persona))
    except participacioEvento.DoesNotExist:
       participacion = None    
       
    try:
       cursos = Eventos.objects.filter(eventpadre__pk=id)
    except Eventos.DoesNotExist:
       cursos = None 
    if resultado:
       return render_to_response('mogie/publico/eventos/detalle.html',{'eventos':eventos,'cursos':cursos,'resultado':resultado,'hoy':date.today(),'perfil':perfil,'participacion':participacion,'trabajosAutor':trabajosAutor,'trabajoscoautor':trabajoscoautor}, context_instance=RequestContext(request))
    else:
       return render_to_response('mogie/publico/eventos/detalle.html',{'eventos':eventos}, context_instance=RequestContext(request))    



def postulacionResumenes(request,evento,modalidad):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    if not resultado:
       return HttpResponseRedirect("/mogie")
    
    try:
       eventos = Eventos.objects.get(pk=evento)
    except Eventos.DoesNotExist:
       eventos = None
     
    if request.method == 'POST':
       registrarResumen = DatosResumen(request.POST)
       if registrarResumen.is_valid():
          trabajos = registrarResumen.save()
          trabajos.estatu = 5
          trabajos.save()
          return HttpResponseRedirect("/mogie/eventos/resumen/" + str(trabajos.id))
       else:
          return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'eventos':eventos,'modalidad':modalidad,'resultado':resultado,'perfil':perfil}, context_instance=RequestContext(request))
    else:
       return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'eventos':eventos,'modalidad':modalidad,'resultado':resultado,'perfil':perfil}, context_instance=RequestContext(request))
       
def SegundoPasoPostulacion(request,trabajo):

    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    if not resultado:
       return HttpResponseRedirect("/mogie")
       
    try:
       trabajos = Trabajoscongresos.objects.get(pk=trabajo)
    except Trabajoscongresos.DoesNotExist:
       trabajos = None
    
    if trabajos.estatu <> 5:
       return HttpResponseRedirect("/mogie/eventos/resumen/previsual/"+trabajo)
    
    try:
       coautores = RelacionPersonasTrabajos.objects.filter(trabajo=trabajos)
    except RelacionPersonasTrabajos.DoesNotExist:
       coautores = None
       
    try:
       instituciones = RelacionActoresTrabajos.objects.filter(trabajo=trabajos)
    except RelacionActoresTrabajos.DoesNotExist:
       instituciones = None
    
    if request.method == 'POST':
       EditarResumen = DatosResumen1(request.POST,instance=trabajos)
       if EditarResumen.is_valid():
          trabajos = EditarResumen.save()
          return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'trabajo':trabajos,'resultado':resultado,'perfil':perfil,'coautores':coautores,'instituciones':instituciones,'paso':0,'formulario1':EditarResumen,'error':0}, context_instance=RequestContext(request))
       else:
          return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'trabajo':trabajos,'resultado':resultado,'perfil':perfil,'coautores':coautores,'instituciones':instituciones,'paso':0,'formulario1':EditarResumen,'error':1}, context_instance=RequestContext(request))
    else:
       EditarResumen = DatosResumen1(instance=trabajos)
       return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'trabajo':trabajos,'resultado':resultado,'perfil':perfil,'coautores':coautores,'instituciones':instituciones,'paso':1,'formulario1':EditarResumen}, context_instance=RequestContext(request))
       
       
def TercerPasoPostulacion(request,trabajo):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    if not resultado:
       return HttpResponseRedirect("/mogie")
       
    try:
       trabajos = Trabajoscongresos.objects.get(pk=trabajo)
    except Trabajoscongresos.DoesNotExist:
       trabajos = None
       
    if trabajos.estatu <> 5:
       return HttpResponseRedirect("/mogie/eventos/resumen/previsual/"+trabajo)
       
    try:
       instituciones = RelacionActoresTrabajos.objects.filter(trabajo=trabajos).order_by('orden')
    except RelacionActoresTrabajos.DoesNotExist:
       instituciones = None
       
    try:
       institucionesPosicion = RelacionActoresTrabajos.objects.filter(trabajo=trabajos).order_by('-orden')[:1]
    except RelacionActoresTrabajos.DoesNotExist:
       institucionesPosicion = None
       
    if not institucionesPosicion:
       posicion2 = 1
    else:
       for p in institucionesPosicion:
           porden = p.orden
       posicion2 = porden + 1
       
    try:
       coautoresPosicion = RelacionPersonasTrabajos.objects.filter(trabajo=trabajos).order_by('-orden')[:1]
    except RelacionPersonasTrabajos.DoesNotExist:
       coautoresPosicion = None
       
    if not coautoresPosicion:
       posicion = 1
    else:
       for p in coautoresPosicion:
           porden = p.orden
       posicion = porden + 1

    
    if request.method == 'POST':
       AddCoautores = DatosResumenCoautores(request.POST)
       EditarResumen = DatosResumen1(instance=trabajos)
       
       if AddCoautores.is_valid():
          #guardar coautor
          coautores = AddCoautores.save()
          coautores.orden = posicion
          coautores.save()
          
          #verificar cedula         
          try:
             personasCo = Directorios.objects.get(Q(tipodoci=request.POST['tipodoci']) & Q(documentoidentidad=request.POST['documentoidentidad']))
          except Directorios.DoesNotExist:
             personasCo = None
          #si la institucion existe
          if personasCo:
             #se hace un recorrido
             coautores.personas =  personasCo
             coautores.save()
          else:
             #sino se crea el registro
             personasCo = Directorios(tipodoci=request.POST['tipodoci'],documentoidentidad=request.POST['documentoidentidad'],nombre=request.POST['nombre'],apellido=request.POST['apellido'])
             personasCo.save()
             #se agregar a coautores                
             coautores.personas =  personasCo
             coautores.save()
          
          #consultar si la institucion mencionada esta registrada en actores colectivos
          try:
             institucionesid = Actores.objects.filter(nombre_completo=coautores.institucionestxt)[:1]
          except Actores.DoesNotExist:
             institucionesid = None
          #si la institucion existe
          if institucionesid:
             #se hace un recorrido
             for i in institucionesid:
                #se verifica si existe el registro en un actores historicos
                try:
                   historicoid = ActoresHistorico.objects.get(actores=i)
                except ActoresHistorico.DoesNotExist:
                   historicoid = None
                #si existe el registro   
                if not historicoid:
                   #sino se crea el registro
                   historico = ActoresHistorico(actores=i,telefono=i.telefono,fax=i.fax,address=i.address,geolocation=i.geolocation,rif=i.rif,siglas=i.siglas,nombre=i.nombre,nombre_completo=i.nombre_completo,direccion=i.direccion,pai=i.pai,estado=i.estado,municipio=i.municipio,parroquia=i.parroquia,correo=i.correo,estatu=2)
                   historico.save()
                   #se agregar a coautores                
                   coautores.instituciones =  historico
                   coautores.save()
                   try:
                      instituto = RelacionActoresTrabajos.objects.get(Q(trabajo=trabajos) & Q(instituciones=historico))
                   except RelacionActoresTrabajos.DoesNotExist:
                      instituto = None
                   if not instituto:
                      #se agrega a instituciones
                      institucionesreg = RelacionActoresTrabajos(trabajo=trabajos,instituciones=historico,orden=posicion2)
                      institucionesreg.save()
                      institucionesreg.orden = posicion2
                      institucionesreg.save()
                   
                else:                
                   #se agrega a coautores
                   coautores.instituciones =  historicoid
                   coautores.save()
                   try:
                      instituto = RelacionActoresTrabajos.objects.get(Q(trabajo=trabajos) & Q(instituciones=historicoid))
                   except RelacionActoresTrabajos.DoesNotExist:
                      instituto = None
                   if not instituto:
                      #se agrega a instituciones
                      institucionesreg = RelacionActoresTrabajos(trabajo=trabajos,instituciones=historicoid,orden=posicion2)
                      institucionesreg.save()
                      institucionesreg.orden = posicion2
                      institucionesreg.save()                 

          
          try:
             coautores = RelacionPersonasTrabajos.objects.filter(trabajo=trabajos).order_by('orden')
          except RelacionPersonasTrabajos.DoesNotExist:
             coautores = None
             
          return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'trabajo':trabajos,'resultado':resultado,'perfil':perfil,'coautores':coautores,'instituciones':instituciones,'paso':1,'formulario1':EditarResumen,'formulario2':AddCoautores}, context_instance=RequestContext(request)) 
       else:
       
          try:
             coautores = RelacionPersonasTrabajos.objects.filter(trabajo=trabajos).order_by('orden')
          except RelacionPersonasTrabajos.DoesNotExist:            
             coautores = None
       
          return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'trabajo':trabajos,'resultado':resultado,'perfil':perfil,'coautores':coautores,'instituciones':instituciones,'paso':1,'formulario1':EditarResumen,'formulario2':AddCoautores}, context_instance=RequestContext(request)) 
    
    else: 
       try:
          coautores = RelacionPersonasTrabajos.objects.filter(trabajo=trabajos).order_by('orden')
       except RelacionPersonasTrabajos.DoesNotExist:            
          coautores = None
               
       EditarResumen = DatosResumen1(instance=trabajos)
       AddCoautores = DatosResumenCoautores()
       return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'trabajo':trabajos,'resultado':resultado,'perfil':perfil,'coautores':coautores,'instituciones':instituciones,'paso':1,'formulario1':EditarResumen,'formulario2':AddCoautores}, context_instance=RequestContext(request)) 
       
       
def coautoresBorrar(request,id,trabajo):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    
    try:
       coautores = RelacionPersonasTrabajos.objects.filter(pk=id)
    except RelacionPersonasTrabajos.DoesNotExist:
       coautores = None

    coautores.delete()
    return HttpResponseRedirect("/mogie/eventos/resumen/coautores/" + trabajo)
    
    
def institucionesBorrar(request,id,trabajo):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    
    try:
       instituto = RelacionActoresTrabajos.objects.filter(pk=id)
    except RelacionActoresTrabajos.DoesNotExist:
       instituto = None

    instituto.delete()
    return HttpResponseRedirect("/mogie/eventos/resumen/coautores/" + trabajo)
    
    
def finalizarResumen(request,trabajo):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    
    try:
       trabajos = Trabajoscongresos.objects.get(pk=trabajo)
    except Trabajoscongresos.DoesNotExist:
       trabajos = None

    trabajos.estatu = 4
    trabajos.save()
    return HttpResponseRedirect("/mogie/eventos/resumen/" + trabajo)
    
    
def CuartoPasoPostulacion(request,trabajo):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    if not resultado:
       return HttpResponseRedirect("/mogie")
       
    try:
       trabajos = Trabajoscongresos.objects.get(pk=trabajo)
    except Trabajoscongresos.DoesNotExist:
       trabajos = None 
       
    if trabajos.estatu <> 5:
       return HttpResponseRedirect("/mogie/eventos/resumen/previsual/"+trabajo)
       
    try:
       coautores = RelacionPersonasTrabajos.objects.filter(trabajo=trabajos).order_by('orden')      
    except RelacionPersonasTrabajos.DoesNotExist:            
       coautores = None 
       
    try:
       institucionesPosicion = RelacionActoresTrabajos.objects.filter(trabajo=trabajos).order_by('-orden')[:1]
    except RelacionActoresTrabajos.DoesNotExist:
       institucionesPosicion = None
       
    if not institucionesPosicion:
       posicion2 = 1
    else:
       for p in institucionesPosicion:
           porden = p.orden
       posicion2 = porden + 1       
    
    if request.method == 'POST':
       AddInstituciones = DatosResumenInstituciones(request.POST)
       try:
          historicoid = ActoresHistorico.objects.get(nombre_completo=request.POST['nombre_completo'])
       except ActoresHistorico.DoesNotExist:
          historicoid = None
       if not historicoid:
          if AddInstituciones.is_valid():
             guardarInstitucion = AddInstituciones.save()
             try:
                instituto = RelacionActoresTrabajos.objects.get(Q(trabajo=trabajos) & Q(instituciones=guardarInstitucion))
             except RelacionActoresTrabajos.DoesNotExist:
                instituto = None               
             if not instituto:
                institucionesreg = RelacionActoresTrabajos(trabajo=trabajos,instituciones=guardarInstitucion)
                institucionesreg.save()
                institucionesreg.orden = posicion2
                institucionesreg.save()
       else:
          try:
             instituto = RelacionActoresTrabajos.objects.get(Q(trabajo=trabajos) & Q(instituciones=historicoid))
          except RelacionActoresTrabajos.DoesNotExist:
             instituto = None               
          if not instituto:
             institucionesreg = RelacionActoresTrabajos(trabajo=trabajos,instituciones=historicoid)
             institucionesreg.save()
             institucionesreg.orden = posicion2
             institucionesreg.save()
       try:
          instituciones = RelacionActoresTrabajos.objects.filter(trabajo=trabajos).order_by('orden') 
       except RelacionActoresTrabajos.DoesNotExist:
          instituciones = None 
       EditarResumen = DatosResumen1(instance=trabajos)
       AddCoautores = DatosResumenCoautores()
       return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'trabajo':trabajos,'resultado':resultado,'perfil':perfil,'coautores':coautores,'instituciones':instituciones,'paso':2,'formulario1':EditarResumen,'formulario2':AddCoautores}, context_instance=RequestContext(request))      
    else:
       try:
          instituciones = RelacionActoresTrabajos.objects.filter(trabajo=trabajos).order_by('orden') 
       except RelacionActoresTrabajos.DoesNotExist:
          instituciones = None 
       EditarResumen = DatosResumen1(instance=trabajos)
       AddCoautores = DatosResumenCoautores()
       return render_to_response('mogie/publico/eventos/trabajos/postulacion.html',{'trabajo':trabajos,'resultado':resultado,'perfil':perfil,'coautores':coautores,'instituciones':instituciones,'paso':2,'formulario1':EditarResumen,'formulario2':AddCoautores}, context_instance=RequestContext(request))            
 
 
def ResumenPrevisual(request,trabajo):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    if not resultado:
       return HttpResponseRedirect("/mogie")
       
    try:
       trabajos = Trabajoscongresos.objects.get(pk=trabajo)
    except Trabajoscongresos.DoesNotExist:
       trabajos = None 
       
    try:
       configuracion = DetalleResumenConfiguracion.objects.get(evento=trabajos.evento)
    except DetalleResumenConfiguracion.DoesNotExist:
       configuracion = None 
       
    try:
       coautores = RelacionPersonasTrabajos.objects.filter(trabajo=trabajos).order_by('orden')      
    except RelacionPersonasTrabajos.DoesNotExist:            
       coautores = None 
       
    try:
       instituciones = RelacionActoresTrabajos.objects.filter(trabajo=trabajos).order_by('orden')
    except RelacionActoresTrabajos.DoesNotExist:
       instituciones = None
       
    return render_to_response('mogie/publico/eventos/trabajos/previsual.html',{'trabajo':trabajos,'resultado':resultado,'perfil':perfil,'coautores':coautores,'instituciones':instituciones,'configuracion':configuracion}, context_instance=RequestContext(request))    
       

def OrdenarCoautores(request,id,orden):
    try:
       coautores = RelacionPersonasTrabajos.objects.get(pk=id)      
    except RelacionPersonasTrabajos.DoesNotExist:            
       coautores = None     
    if not coautores:
       response_dict = {}                                          
       response_dict.update({'respuesta':'error > no procesado'})
    else:
       coautores.orden = orden 
       coautores.save()     
       response_dict = {}                                          
       response_dict.update({'respuesta':'procesado orden coautor'})     
    return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
    
    
def OrdenarInstituciones(request,id,orden):
    try:
       instituciones = RelacionActoresTrabajos.objects.get(pk=id)      
    except RelacionActoresTrabajos.DoesNotExist:            
       instituciones = None     
    if not instituciones:
       response_dict = {}                                          
       response_dict.update({'respuesta':'error > no procesado'})
    else:
       instituciones.orden = orden 
       instituciones.save()     
       response_dict = {}                                          
       response_dict.update({'respuesta':'procesado orden instituciones'})     
    return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')   


              
       
def preinscripcionEvento(request,id,trabajo):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
     
    try:
       eventos = Eventos.objects.get(pk=id)
    except Eventos.DoesNotExist:
       eventos = None  
    
    try:
       participacion = participacioEvento.objects.get(Q(evento=eventos) & Q(directorio=perfil.persona))
    except participacioEvento.DoesNotExist:
       participacion = None    
    
    try:
       colaboracion = ColaboracionConf.objects.get(Q(evento=eventos) & Q(metodo=1) & Q(estatu=0))
    except ColaboracionConf.DoesNotExist:
       colaboracion = None   
       
    try:
       detallecolaboracion = DetalleColaboracionConf.objects.filter(colaboracion=colaboracion)
    except DetalleColaboracionConf.DoesNotExist:
       detallecolaboracion = None     
       
    if resultado:
       if colaboracion:
          return render_to_response('mogie/publico/eventos/preinscripcion.html',{'eventos':eventos,'colaboracion':colaboracion,'detallecolaboracion':detallecolaboracion,'resultado':resultado,'hoy':date.today(),'perfil':perfil,'participacion':participacion}, context_instance=RequestContext(request))
       else:
          if participacion:
             return HttpResponseRedirect("/mogie")
          else:
             participacion = participacioEvento(directorio=perfil.persona,evento=eventos,estatu=2)
             participacion.save()
             return render_to_response('mogie/publico/eventos/preinscripcion/registro_exitoso.html',{'eventos':eventos,'perfil':perfil})
    else:
       return HttpResponseRedirect("/mogie")    
       
       
def preinscripcionColaboracionEvento(request,event,colab):
    if request.method == 'POST':
		try:
		    _username = request.user.username
		except request.DoesNotExist:
		    _username = None
		resultado,perfil = accesoValidacion(_username) 
		 
		try:
		   eventos = Eventos.objects.get(pk=event)
		except Eventos.DoesNotExist:
		   eventos = None  
		
		try:
		   participacion = participacioEvento.objects.get(Q(evento=eventos) & Q(directorio=perfil.persona))
		except participacioEvento.DoesNotExist:
		   participacion = None
		
		if participacion:
			return HttpResponseRedirect("/mogie/eventos/detalle/" + str(event))
		else:  
		  
			try:
			   	colaboracion = ColaboracionConf.objects.get(pk=colab)
			except ColaboracionConf.DoesNotExist:
			   	colaboracion = None   
			   
			try:
			   	detallecolaboracion = DetalleColaboracionConf.objects.filter(colaboracion=colaboracion)
			except DetalleColaboracionConf.DoesNotExist:
			   	detallecolaboracion = None
			   	
			colaboracionpersonas = ColaboracionPersonas(colaboracionconf=colaboracion,personas=perfil.persona,estatu=1)
			colaboracionpersonas.save()
			
			try:
			   	colaboracionpersonasGuardado = ColaboracionPersonas.objects.get(colaboracionconf=colaboracion,personas=perfil.persona,estatu=1)
			except ColaboracionPersonas.DoesNotExist:
			   	colaboracionpersonasGuardado = None 
			   	
			for i in detallecolaboracion:
				idCampo = str(i.id)
				if i.tipo == 0:
					valor = request.POST[idCampo]
					colaboracionregistro1 = ColaboracionInformacion(colaboracionconf=colaboracion,colaboracionpersonas=colaboracionpersonasGuardado,textos=valor)
					colaboracionregistro1.save()
				if i.tipo == 1:
					valor = request.POST[idCampo]
					colaboracionregistro2 = ColaboracionInformacion(colaboracionconf=colaboracion,colaboracionpersonas=colaboracionpersonasGuardado,textos=valor)
					colaboracionregistro2.save()
				if i.tipo == 2:
					valor = request.POST[idCampo]
					colaboracionregistro3 = ColaboracionInformacion(colaboracionconf=colaboracion,colaboracionpersonas=colaboracionpersonasGuardado,textos=valor)
					colaboracionregistro3.save()
				if i.tipo == 3:
					valor = request.POST[idCampo]
					colaboracionregistro4 = ColaboracionInformacion(colaboracionconf=colaboracion,colaboracionpersonas=colaboracionpersonasGuardado,textos=valor)
					colaboracionregistro4.save()
				if i.tipo == 4:
					valor = request.POST[idCampo]
					colaboracionregistro5 = ColaboracionInformacion(colaboracionconf=colaboracion,colaboracionpersonas=colaboracionpersonasGuardado,textos=valor)
					colaboracionregistro5.save()
				if i.tipo == 5:
					colaboracionregistro6 = ColaboracionInformacion(colaboracionconf=colaboracion,colaboracionpersonas=colaboracionpersonasGuardado,foto=request.FILES[idCampo])
					colaboracionregistro6.save()
				if i.tipo == 6:
					colaboracionregistro7 = ColaboracionInformacion(colaboracionconf=colaboracion,colaboracionpersonas=colaboracionpersonasGuardado,archivo=request.FILES[idCampo])
					colaboracionregistro7.save()
			preinscrito = participacioEvento(directorio=perfil.persona,evento=eventos,estatu=0)
			preinscrito.save()
			return render_to_response('mogie/publico/eventos/preinscripcion/registro_exitoso.html',{'eventos':eventos,'perfil':perfil})
    else:
    	return HttpResponseRedirect("/mogie")
     


       
       
def RegistrarUsuarios(request):
    try:
        _username = request.user.username
    except request.DoesNotExist:
        _username = None
    resultado,perfil = accesoValidacion(_username) 
    if resultado:
       return HttpResponseRedirect("/mogie")
    if request.method == 'POST':
       persona_formulario = PersonasRegForm(request.POST)
       usuario_formulario = UserCreationForm(request.POST)
       if persona_formulario.is_valid() and usuario_formulario.is_valid():
          
          usuario_validado = usuario_formulario.save()
          validando_persona = persona_formulario.save()
          
          perfil_publico = PerfilPublico(user=usuario_validado,persona=validando_persona)
          perfil_publico.save() 
          
          salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
          validacion = validaciones(usuario=perfil_publico,codigo=salt,estatu=0,estado=True)
          validacion.save()
          subject, from_email, to = 'SVIDB Registro de Usuarios', settings.EMAIL_HOST_USER, request.POST['username']
          correo4= request.POST['username']
          text_content = 'SVIDB Registro de Usuarios'
          d= settings.URL_SET_SITE
          ctx_dict = {'salt': salt,'d': d,'correo':correo4}
          html_content= render_to_string('correos/plantillas/validacion.txt',ctx_dict)
          msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
          msg.attach_alternative(html_content, "text/html")
          msg.send()

          return render_to_response('mogie/publico/perfil/registro_exitoso.html')

       else:
          # Si el usuario es valido
          if usuario_formulario.is_valid():
             #Se guarda el tipo de documento y el documento en dos variables
             cedula = request.POST['documentoidentidad']
             tipod = request.POST['tipodoci']
             #Se realiza una consulta para ver si existen en la base de datos
             try:
                 validando_persona = Directorios.objects.get(Q(documentoidentidad=cedula) & Q(tipodoci=tipod))
             except Directorios.DoesNotExist:
                 validando_persona = False
             #Si existe un registro con ese documento de identidad    
             if validando_persona:
                #Se realiza una consulta para ver si la persona tiene un registro en perfil
                try:
                    validando_perfil = PerfilPublico.objects.filter(persona=validando_persona)
                except PerfilPublico.DoesNotExist:
                    validando_perfil = False
                #Si no existe un registro en perfil con esa cedula
                if not validando_perfil:
                   usuario_validado = usuario_formulario.save()
                   perfil_publico = PerfilPublico(user=usuario_validado,persona=validando_persona)
                   perfil_publico.save()
                   salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
                   validacion = validaciones(usuario=perfil_publico,codigo=salt,estatu=0,estado=True)
                   validacion.save()
                   subject, from_email, to = 'SVIDB Registro de Usuarios', settings.EMAIL_HOST_USER, request.POST['username']
                   correo4= request.POST['username']
                   text_content = 'SVIDB Registro de Usuarios'
                   d= settings.URL_SET_SITE
                   ctx_dict = {'salt': salt,'d': d,'correo':correo4}
                   html_content= render_to_string('correos/plantillas/validacion.txt',ctx_dict)
                   msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                   msg.attach_alternative(html_content, "text/html")
                   msg.send()
                   return render_to_response('mogie/publico/perfil/registro_exitoso.html')
                #Existe un perfil con el documento de identidad asociado
                else:
                   return render_to_response('mogie/publico/perfil/registrar.html',{'persona_formulario':persona_formulario,'usuario_formulario':usuario_formulario,'mensaje':'Se ha presentado un error en el formulario. Revise el contenido y vuelva a intentarlo.'}, context_instance=RequestContext(request))
             #No existe un registro de persona con ese documento de identidad
             else:
                return render_to_response('mogie/publico/perfil/registrar.html',{'persona_formulario':persona_formulario,'usuario_formulario':usuario_formulario,'mensaje':'Se ha presentado un error en el formulario. Revise el contenido y vuelva a intentarlo.'}, context_instance=RequestContext(request))
          #Los datos de usuarios son incorrectos
          else:
             return render_to_response('mogie/publico/perfil/registrar.html',{'persona_formulario':persona_formulario,'usuario_formulario':usuario_formulario,'mensaje':'Se ha presentado un error en el formulario. Revise el contenido y vuelva a intentarlo.'}, context_instance=RequestContext(request))
    else:
       return render_to_response('mogie/publico/perfil/registrar.html')

    
    
    
    
    
    
    
       
       
       
       
           