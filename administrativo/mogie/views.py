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
    try:
       eventos = Eventos.objects.get(pk=id)
    except Eventos.DoesNotExist:
       eventos = None  
    
    try:
       participacion = participacioEvento.objects.get(Q(evento=eventos) & Q(directorio=perfil.persona))
    except participacioEvento.DoesNotExist:
       participacion = None    
       
    try:
       cursos = Eventos.objects.filter(eventpadre__pk=id)
    except Eventos.DoesNotExist:
       cursos = None 
    if resultado:
       return render_to_response('mogie/publico/eventos/detalle.html',{'eventos':eventos,'cursos':cursos,'resultado':resultado,'hoy':date.today(),'perfil':perfil,'participacion':participacion}, context_instance=RequestContext(request))
    else:
       return render_to_response('mogie/publico/eventos/detalle.html',{'eventos':eventos}, context_instance=RequestContext(request))    



def postulacionResumenes(request,evento,tematica):
    if request.method == 'POST':
       return render_to_response('mogie/publico/eventos/trabajos/postulacion.html')
    else:
       return render_to_response('mogie/publico/eventos/trabajos/postulacion.html')
       
              
       
def preinscripcionEvento(request,id):
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

    
    
    
    
    
    
    
       
       
       
       
           