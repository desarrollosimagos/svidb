#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
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
          return HttpResponseRedirect("/mogie/perfil2")
    else:
       return HttpResponseRedirect("/mogie/perfil3")
       
       
def RegistrarUsuarios(request):
    if request.method == 'POST':
       personas_form_post = PersonasRegForm(request.POST)
       formulario_post = UserCreationFormSVIDB(request.POST)
       if request.POST['g-recaptcha-response']:
          robot = request.POST['g-recaptcha-response']
          if request.POST['documentoidentidad'] and  request.POST['tipodoci'] and request.POST['username'] :
             cedula = request.POST['documentoidentidad']
             tipod = request.POST['tipodoci']
             username = request.POST['username']
             try:
                 validando_persona = Directorios.objects.get(Q(documentoidentidad=cedula) & Q(tipodoci=tipod))
             except Directorios.DoesNotExist:
                 validando_persona = False
             try:
                 validando_user = User.objects.get(username=username)
             except User.DoesNotExist:
                 validando_user = False
             if not validando_persona and not validando_user:
                #registrar persona y crear usuario
                if personas_form_post.is_valid() and formulario_post.is_valid():
                   result_user = formulario_post.save()
                   validando_persona = personas_form_post.save()
                   validando_persona.correo = username
                   validando_persona.save()
                   perfil_publico = PerfilPublico(user=result_user,persona=validando_persona)
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
                   formulario = UserCreationFormSVIDB()
                   personas_form = PersonasRegForm()
                   return render_to_response('mogie/publico/perfil/registrar.html',{'formulario':formulario,'error':'No','mensaje_error':'Su registro ha sido satisfactorio.','personas_form':personas_form,'url':url}, context_instance=RequestContext(request))
                else:
                   formulario = UserCreationFormSVIDB()
                   personas_form = PersonasRegForm()
                   return render_to_response('mogie/publico/perfil/registrar.html',{'formulario':formulario,'error':'Si','mensaje_error':'Los datos del Formulario son incorrectos','personas_form':personas_form,'url':url}, context_instance=RequestContext(request))
             else:
                if not validando_user:
                   #crear usuario
                   if formulario_post.is_valid():
                      try:
                          validando_perfil = PerfilPublico.objects.filter(persona=validando_persona)
                      except PerfilPublico.DoesNotExist:
                          validando_perfil = False
                      if validando_perfil:
                         formulario = UserCreationFormSVIDB()
                         personas_form = PersonasRegForm()
                         return render_to_response('mogie/publico/perfil/registrar.html',{'formulario':formulario,'error':'Si','mensaje_error':'El documento de identidad suministrado ya posee un registro de usuario en el sistema. Ingrese en la seccion de recuperar datos.','personas_form':personas_form,'recuperar':'si','url':url}, context_instance=RequestContext(request))	
                      else:				  
                         result_user = formulario_post.save()
                         validando_persona.correo = username
                         validando_persona.save()
                         perfil_publico = PerfilPublico(user=result_user,persona=validando_persona)
                         perfil_publico.save()
                         salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
                         validacion = validaciones(usuario=perfil_publico,codigo=salt,estatu=0,estado=True)
                         validacion.save()
                         subject, from_email, to = 'SVIDB Registro de Usuarios', settings.EMAIL_HOST_USER, request.POST['username']
                         text_content = 'SVIDB Registro de Usuarios'
                         d= settings.URL_SET_SITE
                         correo4= request.POST['username']
                         ctx_dict = {'salt': salt,'d': d,'correo':correo4}
                         html_content= render_to_string('correos/plantillas/validacion.txt',ctx_dict)
                         msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                         msg.attach_alternative(html_content, "text/html")
                         msg.send()
                         formulario = UserCreationFormSVIDB()
                         personas_form = PersonasRegForm()
						 
                         return render_to_response('mogie/publico/perfil/registrar.html',{'formulario':formulario,'error':'No','mensaje_error':'Se ha registrado su usuario y asociado a sus datos previamente almacenados en nuestra base de datos','personas_form':personas_form,'url':url}, context_instance=RequestContext(request))
                else:
                   formulario = UserCreationFormSVIDB()
                   personas_form = PersonasRegForm()
                   return render_to_response('mogie/publico/perfil/registrar.html',{'formulario':formulario,'error':'Si','mensaje_error':'El correo electronico ya esta asociado a una cuenta de usuario.','personas_form':personas_form,'url':url}, context_instance=RequestContext(request))
          else:
             formulario = UserCreationFormSVIDB()
             personas_form = PersonasRegForm()
             return render_to_response('mogie/publico/perfil/registrar.html',{'formulario':formulario,'error':'Si','mensaje_error':'No se enviaron los datos completos para procesar el formulario.','personas_form':personas_form,'url':url}, context_instance=RequestContext(request))
       else:
          formulario = UserCreationFormSVIDB()
          personas_form = PersonasRegForm()
          return render_to_response('mogie/publico/perfil/registrar.html',{'formulario':formulario,'error':'Si','mensaje_error':'Se envio el formulario sin formato POST','personas_form':personas_form,'url':url}, context_instance=RequestContext(request))
    else: 
       formulario = UserCreationFormSVIDB()
       personas_form = PersonasRegForm()
       return render_to_response('mogie/publico/perfil/registrar.html',{'formulario':formulario,'personas_form':personas_form}, context_instance=RequestContext(request))
       
       
       
       
           