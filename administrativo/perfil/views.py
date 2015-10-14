#!/usr/bin/python -u
# -*- coding: utf-8 -*-
import datetime
import hashlib
import random
import re
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from actores.models import *
from actores.forms import *
from congresos.models import *
from django.db.models import *

from django.utils import simplejson

import time, urllib2
import urllib
import string
import xml.etree.ElementTree


from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import *


from django.shortcuts import render_to_response, get_object_or_404,HttpResponseRedirect

from perfil.models import *

def verificacion(request):
    if request.method == 'POST':
       correo = request.POST['correo']
       codigo = request.POST['codigo']
 
       try:
          usuario = User.objects.get(username=correo)
       except User.DoesNotExist:
          usuario=None
		  
       try:
          perfil = PerfilPublico.objects.get(user=usuario)
       except PerfilPublico.DoesNotExist:
          perfil=None

       if usuario and perfil:
          persona =  get_object_or_404(Directorios, pk=perfil.persona.id)
          try:
              validacion = validaciones.objects.get(usuario=perfil,codigo=codigo,estado=True)
          except validaciones.DoesNotExist:
              validacion=None
          if validacion:
             if validacion.estatu == 0:
                personas_post_edit = PersonasEditForm2(instance=persona)
                return render_to_response('perfil/verificacion.html',{'msm':"Complete el siguiente formulario.",'formulario':personas_post_edit,'validacion':validacion})
             if validacion.estatu == 1:
                return render_to_response('perfil/verificacion.html',{'msm':"Ingrese su nueva contraseña como se indica en el formulario.",'formulario':'password','validacion':validacion})
             if validacion.estatu == 2:
                return render_to_response('perfil/verificacion.html',{'msm':"¿Esta seguro que desea eliminar su perfil?"})
           
          else:
             return render_to_response('perfil/verificacion.html',{'msm':"Disculpe no tiene solicitud de Verificación Activa!"})
       else:
          return render_to_response('perfil/verificacion.html',{'msm':"Correo no registrado!"})
    else:
       return render_to_response('perfil/verificacion.html')	

def activacion(request):
    if request.method == 'POST':
       id= request.POST['valid']
       try:
           validacion = validaciones.objects.get(pk=id)
       except validaciones.DoesNotExist:
            validacion=None
       persona =  get_object_or_404(Directorios, pk=validacion.usuario.persona.id)
       personas_edit = PersonasEditForm2(request.POST, instance = persona)
       if personas_edit.is_valid():
          personas_edit.save()
          #enviar correo de informacion
		  #modulos
          try:
              permisos_modulos=DetalleGruposPermisos.objects.filter(grupo__nombre="Publico").annotate(acount=Count('modulo'))
          except DetalleGruposPermisos.DoesNotExist:
              permisos_modulos = None
          if permisos_modulos:
             for i in permisos_modulos:
                if i.modulo:
                   per_modulo = PerfilModulos(perfil=validacion.usuario,modulos=i.modulo,activo=True)
                   per_modulo.save()
				
          #submodulos
          try:
              permisos_submodulos=DetalleGruposPermisos.objects.filter(grupo__nombre="Publico").annotate(acount=Count('submodulo'))
          except DetalleGruposPermisos.DoesNotExist:
              permisos_submodulos = None
          if permisos_submodulos:
             for i in permisos_submodulos:
                if i.submodulo:
                   per_submodulos = PerfilSubModulos(perfil=validacion.usuario,submodulos=i.submodulo,activo=True)
                   per_submodulos.save()
          validacion.estado = False
          validacion.save()
          return HttpResponseRedirect("/perfil")
       else:
          personas_post_edit = PersonasEditForm2(request.POST)
          return render_to_response('perfil/verificacion.html',{'msm':"Se ha generado un error, Complete el siguiente formulario.",'formulario':personas_post_edit,'validacion':validacion})
    else:
       return HttpResponseRedirect("/panel/verificacion/")
	
def cambiar(request):
    if request.method == 'POST':
       id = request.POST['valid']
       clave = request.POST['clave1']
       try:
           validacion = validaciones.objects.get(pk=id)
       except validaciones.DoesNotExist:
            validacion=None
       try:
           u = User.objects.get(pk=validacion.usuario.user.id)
       except User.DoesNotExist:
           u = None
       if u and validacion:
          validacion.estado=False
          validacion.save()
          u.set_password(clave)
          u.save()
          return HttpResponseRedirect("/perfil")
       else:
          return HttpResponseRedirect("/panel/verificacion/")
    else:
       return HttpResponseRedirect("/panel/verificacion/")   

def renValidacion(request):
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
     salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
     validacion = validaciones(usuario=id_persona,codigo=salt,estatu=0,estado=True)
     validacion.save()
     subject, from_email, to = 'SVIDB Código de Verificación', settings.EMAIL_HOST_USER, persona.correo
     text_content = 'SVIDB Código de Verificación'
     d= settings.URL_SET_SITE
     ctx_dict = {'salt': salt,'d': d}
     html_content= render_to_string('correos/plantillas/validacion.txt',ctx_dict)
     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
     msg.attach_alternative(html_content, "text/html")
     msg.send()
     return render_to_response('perfil/exito.html',{'msm':"Se ha enviado un correo con los pasos. Muchas Gracias."})

def recuperacion(request):
     if request.user.username:
        _username = request.user.username
        id_usuario = User.objects.get(username=_username)
        print id_usuario.id
        id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
        persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        validacion = validaciones(usuario=id_persona,codigo=salt,estatu=1,estado=True)
        validacion.save()
        subject, from_email, to = 'SVIDB Cambio de Clave', settings.EMAIL_HOST_USER, persona.correo
        text_content = 'SVIDB Cambio de Clave'
        d= settings.URL_SET_SITE
        ctx_dict = {'salt': salt,'d': d}
        html_content= render_to_string('correos/plantillas/cambio.txt',ctx_dict)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return render_to_response('perfil/exito.html',{'msm':"Se ha enviado un correo con los pasos. Muchas Gracias."})
     else:
        if request.method == 'POST':
           #se envio el form
           correo = request.POST['correo']
           try:
               persona = Directorios.objects.get(correo=correo)
           except Directorios.DoesNotExist:
               persona = None
           
           try:
               perfil = PerfilPublico.objects.get(persona=persona)
           except PerfilPublico.DoesNotExist:
               perfil=None
           if perfil:
              #envio correo
              salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
              validacion = validaciones(usuario=perfil,codigo=salt,estatu=1,estado=True)
              validacion.save()
              subject, from_email, to = 'SVIDB Recuperación de Datos de Acceso', settings.EMAIL_HOST_USER, persona.correo
              correo4 = persona.correo
              text_content = 'SVIDB Recuperación de Datos de Acceso'
              d= settings.URL_SET_SITE
              ctx_dict = {'salt': salt,'d': d,'correo':correo4}
              html_content= render_to_string('correos/plantillas/recuperar.txt',ctx_dict)
              msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
              msg.attach_alternative(html_content, "text/html")
              msg.send()
              return render_to_response('perfil/exito.html',{'msm':"Se ha enviado un correo con los pasos. Muchas Gracias."})
           else:
              return render_to_response('perfil/recuperar.html',{'msm':"Correo no registrado!"})
        else:
           return render_to_response('perfil/exito.html',{'msm':"Lo sentimos, su operación no puede proceder.!"})


def panelCoordinacion(request,id):
    if request.user.username:
       _username = request.user.username
       id_usuario = User.objects.get(username=_username)
       print id_usuario.id
       id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
       persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
       try:
           eventos_activos = Eventos.objects.get(pk= id)
       except Eventos.DoesNotExist:
           eventos_activos = None

       if eventos_activos.eventpadre == None:
          eventoPadre=eventos_activos.id
       else:
          eventoPadre=eventos_activos.eventpadre.id

       try:
           tipo_eventos = TipoEventos.objects.filter()
       except TipoEventos.DoesNotExist:
           tipo_eventos = None
       return render_to_response('panel/index.html',{'persona':persona,'evento':eventos_activos,'id2':eventos_activos.id,'tipo_eventos':tipo_eventos,'eventoPadre':eventoPadre})
    else:
       return HttpResponseRedirect("/perfil")
	   
def panelCursosIndex(request,id,id2):
    tipo = id
    evento = id2
    if request.user.username:
       _username = request.user.username
       id_usuario = User.objects.get(username=_username)
       id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
       persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
       try:
           eventos_activos = Eventos.objects.get(pk=evento)
       except Eventos.DoesNotExist:
           eventos_activos = None

       if eventos_activos.eventpadre == None:
          eventoPadre=eventos_activos.id
       else:
          eventoPadre=eventos_activos.eventpadre.id

       try:
           tipo_eventos = TipoEventos.objects.filter()
       except TipoEventos.DoesNotExist:
           tipo_eventos = None
       try:
           actividades = Eventos.objects.filter(Q(eventpadre=eventos_activos) & Q(tipoe=tipo))
       except Eventos.DoesNotExist:
           actividades = None
       return render_to_response('panel/cursos.html',{'persona':persona,'evento':eventos_activos,'id2':eventos_activos.id,'actividades':actividades,'tipo_eventos':tipo_eventos,'eventoPadre':eventoPadre})
    else:
       return HttpResponseRedirect("/perfil")
	   
def buscarCedula(request,id2,id):
    if request.user.username:
       _username = request.user.username
       id_usuario = User.objects.get(username=_username)
       print id_usuario.id
       id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
       persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
       persona1= None
       sis = True
       pasar = False
       varios=None
       try:
           eventos_activos = Eventos.objects.get(pk= id2)
       except Eventos.DoesNotExist:
           eventos_activos = None
       if eventos_activos.eventpadre == None:
          eventoPadre=eventos_activos.id
       else:
          eventoPadre=eventos_activos.eventpadre.id

       try:
           tipo_eventos = TipoEventos.objects.filter()
       except TipoEventos.DoesNotExist:
           tipo_eventos = None
       try:
           persona1 = Directorios.objects.get(documentoidentidad=id)
       except Directorios.DoesNotExist:
           persona1 = None
       try:
           registro = participacioEvento.objects.get(Q(directorio=persona1) & Q(evento=eventos_activos))
       except participacioEvento.DoesNotExist:
           registro = None
       try:
           varios = participacioEventoVarios.objects.get(Q(directorio=persona1) & Q(evento=eventos_activos))
       except participacioEventoVarios.DoesNotExist:
           varios = None
       try:
           aporte = AportesEventosConfiguracion.objects.get(evento=eventos_activos)
       except AportesEventosConfiguracion.DoesNotExist:
           aporte = None
           pasar = True
       try:
           colaboracion = participacioEventoAporte.objects.get(Q(directorio=persona1) & Q(evento=eventos_activos))
       except participacioEventoAporte.DoesNotExist:
           colaboracion = None
		   
       try:
           trabajos = Trabajoscongresos.objects.filter(Q(directorio=persona1) & Q(evento=eventos_activos) & Q(estatu=1))
       except Trabajoscongresos.DoesNotExist:
           trabajos = None
		   
       if trabajos:
          tra = trabajos
       else:
          try:
              trabajos = Trabajoscongresos.objects.filter(Q(coautores=persona1) & Q(evento=eventos_activos) & Q(estatu=1))
          except Trabajoscongresos.DoesNotExist:
              trabajos = None
       
       if request.method == 'POST':	
          if persona1:
             personas_edit = PersonasEditForm(request.POST,instance = persona1)
          else:
             personas_edit = PersonasEditFormNew(request.POST)	   
          if personas_edit.is_valid():
             personas_edit.save()
             try:
                 persona1 = Directorios.objects.get(documentoidentidad=id)
             except Directorios.DoesNotExist:
                 persona1 = None
             personas_edit = PersonasEditForm(instance = persona1)
             return HttpResponseRedirect("/panel/coord/index/buscar/"+id2+"/"+id)
          else:
             return render_to_response('panel/index.html',{'persona':persona,'persona1':persona1,'sis':sis,'formulario':personas_edit,'id':id,'id2':id2,'evento':eventos_activos,'registro':registro,'varios':varios,'aporte':aporte,'colaboracion':colaboracion,'pasar':pasar,'trabajos':trabajos,'tipo_eventos':tipo_eventos,'eventoPadre':eventoPadre})
       else:
          if persona1:
             personas_edit = PersonasEditForm(instance = persona1)
          else:
             personas_edit = PersonasEditFormNew()
          return render_to_response('panel/index.html',{'persona':persona,'persona1':persona1,'sis':sis,'formulario':personas_edit,'id':id,'id2':id2,'evento':eventos_activos,'registro':registro,'varios':varios,'aporte':aporte,'colaboracion':colaboracion,'pasar':pasar,'trabajos':trabajos,'tipo_eventos':tipo_eventos,'eventoPadre':eventoPadre})
    else:
       return HttpResponseRedirect("/perfil")
	   
	   
def panelOpciones(request,id2,id):
    if request.user.username:
       try:
           eventos_activos = Eventos.objects.get(pk= id2)
       except Eventos.DoesNotExist:
           eventos_activos = None
       try:
           persona1 = Directorios.objects.get(documentoidentidad=id)
       except Directorios.DoesNotExist:
           persona1 = None
       if request.method == 'POST':	
          if request.POST['inscrito']:
             inscrito = request.POST['inscrito']
          else:
             inscrito = None
          if request.POST.get('certificado', False):
             certificado = request.POST['certificado']
          else:
             certificado = None
          if request.POST.get('material', False):
             material = request.POST['material']
          else:
             material = None		  
          if inscrito or certificado or material:
             try:
                registro = participacioEvento.objects.get(Q(directorio=persona1) & Q(evento=eventos_activos))
             except participacioEvento.DoesNotExist:
                registro = None
             try:
                varios = participacioEventoVarios.objects.get(Q(directorio=persona1) & Q(evento=eventos_activos))
             except participacioEventoVarios.DoesNotExist:
                varios = None
             if registro:
                registro.estatu=3
             else:
                registro = participacioEvento(directorio=persona1,evento=eventos_activos,estatu=3)
             registro.save()
			 
             if varios:
                if certificado:
                   varios.certificado=True
                if material:
                   varios.material=True
             else:
                if certificado:
                   vcertificado=True
                else:
                   vcertificado=False
                if material:
                   vmaterial=True
                else:
                   vmaterial=False
                varios = participacioEventoVarios(directorio=persona1,evento=eventos_activos,material=vmaterial,certificado=vcertificado)
             varios.save()
             return HttpResponseRedirect("/panel/coord/index/buscar/"+id2+"/"+id)
          else:
             return HttpResponseRedirect("/panel/coord/index/buscar/"+id2+"/"+id)
       else:
          return HttpResponseRedirect("/panel/coord/index/buscar/"+id2+"/"+id)
    else:
       return HttpResponseRedirect("/perfil")
	   
def panelColaboracion(request,id2,id):
    if request.user.username:
       try:
           eventos_activos = Eventos.objects.get(pk= id2)
       except Eventos.DoesNotExist:
           eventos_activos = None
       try:
           persona1 = Directorios.objects.get(documentoidentidad=id)
       except Directorios.DoesNotExist:
           persona1 = None
       if request.method == 'POST':	
          if request.POST.get('campo1', False):
             campo1 = request.POST['campo1']
          else:
             campo1 = 'n/a'
          if request.POST.get('campo2', False):
             campo2 = request.POST['campo2']
          else:
             campo2 = 'n/a'
          if request.POST.get('campo3', False):
             campo3 = request.POST['campo3']
          else:
             campo3 = 'n/a'
          if request.POST.get('campo4', False):
             campo4 = request.POST['campo4']
          else:
             campo4 = 'n/a'
          if request.POST.get('campo5', False):
             campo5 = request.POST['campo5']
          else:
             campo5 = 'n/a'
          if request.POST.get('campo6', False):
             campo6 = request.POST['campo6']
          else:
             campo6 = 'n/a'
          if request.POST.get('campo7', False):
             campo7 = request.POST['campo7']
          else:
             campo7 = 'n/a'
          if request.POST.get('campo8', False):
             campo8 = request.POST['campo8']
          else:
             campo8 = 'n/a'
          if request.POST.get('campo9', False):
             campo9 = request.POST['campo9']
          else:
             campo9 = 'n/a'	
          if request.POST.get('campo10', False):
             campo10 = request.POST['campo10']
          else:
             campo10 = 'n/a'		  
          colaboracion = participacioEventoAporte(directorio=persona1,evento=eventos_activos,campo1=campo1,campo2=campo2,campo3=campo3,campo4=campo4,campo5=campo5,campo6=campo6,campo7=campo7,campo8=campo8,campo9=campo9,campo10=campo10)
          colaboracion.save()
          return HttpResponseRedirect("/panel/coord/index/buscar/"+id2+"/"+id)
       else:
          return HttpResponseRedirect("/panel/coord/index/buscar/"+id2+"/"+id)
    else:
       return HttpResponseRedirect("/perfil")
	   
def panelCursosInscribir(request,id):
    if request.user.username:
       _username = request.user.username
       id_usuario = User.objects.get(username=_username)
       print id_usuario.id
       id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
       persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
       actividades = None
       try:
           eventos_activos = Eventos.objects.get(pk= id)
       except Eventos.DoesNotExist:
           eventos_activos = None
       if request.method == 'POST':	
          if request.POST.get('curso', False):
             id3 = request.POST['curso']
             try:
                 actividades = Eventos.objects.get(pk=id3)
             except Eventos.DoesNotExist:
                 actividades = None
          return render_to_response('panel/lista.html',{'persona':persona,'evento':eventos_activos,'id2':eventos_activos.id,'actividades':actividades})
       else:
          return render_to_response('panel/cursos.html',{'persona':persona,'evento':eventos_activos,'id2':eventos_activos.id,'actividades':actividades})
    else:
       return HttpResponseRedirect("/perfil")
	   
	   
def buscarCedula3(request,id2,id):
    if request.user.username:
       _username = request.user.username
       id_usuario = User.objects.get(username=_username)
       print id_usuario.id
       id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
       persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
       persona1= None
       sis = True
       pasar = False
       varios=None
       try:
           eventos_activos = Eventos.objects.get(pk= id2)
       except Eventos.DoesNotExist:
           eventos_activos = None
       try:
           persona1 = Directorios.objects.get(documentoidentidad=id)
       except Directorios.DoesNotExist:
           persona1 = None
       try:
           registro = participacioEvento.objects.get(Q(directorio=persona1) & Q(evento=eventos_activos))
       except participacioEvento.DoesNotExist:
           registro = None
       try:
           varios = participacioEventoVarios.objects.get(Q(directorio=persona1) & Q(evento=eventos_activos))
       except participacioEventoVarios.DoesNotExist:
           varios = None
       try:
           aporte = AportesEventosConfiguracion.objects.get(evento=eventos_activos)
       except AportesEventosConfiguracion.DoesNotExist:
           aporte = None
           pasar = True
       try:
           colaboracion = participacioEventoAporte.objects.get(Q(directorio=persona1) & Q(evento=eventos_activos))
       except participacioEventoAporte.DoesNotExist:
           colaboracion = None
       
       if request.method == 'POST':	
          if persona1:
             personas_edit = PersonasEditForm(request.POST,instance = persona1)
          else:
             personas_edit = PersonasEditFormNew(request.POST)	   
          if personas_edit.is_valid():
             personas_edit.save()
             try:
                 persona1 = Directorios.objects.get(documentoidentidad=id)
             except Directorios.DoesNotExist:
                 persona1 = None
             personas_edit = PersonasEditForm(instance = persona1)
             return render_to_response('panel/index2.html',{'persona':persona,'persona1':persona1,'sis':sis,'formulario':personas_edit,'id':id,'id2':id2,'evento':eventos_activos,'registro':registro,'varios':varios,'aporte':aporte,'colaboracion':colaboracion,'pasar':pasar})
          else:
             return render_to_response('panel/index2.html',{'persona':persona,'persona1':persona1,'sis':sis,'formulario':personas_edit,'id':id,'id2':id2,'evento':eventos_activos,'registro':registro,'varios':varios,'aporte':aporte,'colaboracion':colaboracion,'pasar':pasar})
       else:
          if persona1:
             personas_edit = PersonasEditForm(instance = persona1)
          else:
             personas_edit = PersonasEditFormNew()
          return render_to_response('panel/index2.html',{'persona':persona,'persona1':persona1,'sis':sis,'formulario':personas_edit,'id':id,'id2':id2,'evento':eventos_activos,'registro':registro,'varios':varios,'aporte':aporte,'colaboracion':colaboracion,'pasar':pasar})
    else:
       return HttpResponseRedirect("/perfil")
	   
def GuardarTrabajosEntregados(request,id2,id,id3):
    if request.user.username:
       try:
           trabajos = Trabajoscongresos.objects.get(pk=id3)
       except Trabajoscongresos.DoesNotExist:
           trabajos = None
       if request.method == 'POST':	
          if request.POST.get('impreso', False):
             impreso = request.POST['impreso']
          else:
             impreso = None

          if request.POST.get('armado', False):
             armado = request.POST['armado']
          else:
             armado = None
			 
          if request.POST.get('entregado', False):
             entregado = request.POST['entregado']
          else:
             entregado = None		  
          if impreso or armado or entregado:
             if impreso:
                trabajos.impreso=True
             if armado:
                trabajos.armado=True
             if entregado:
                trabajos.entregado=True
             trabajos.save()
             return HttpResponseRedirect("/panel/coord/index/buscar/"+id2+"/"+id)
          else:
             return HttpResponseRedirect("/panel/coord/index/buscar/"+id2+"/"+id)
       else:
          return HttpResponseRedirect("/panel/coord/index/buscar/"+id2+"/"+id)
    else:
       return HttpResponseRedirect("/perfil")

def validarCedula(request):
    if request.is_ajax():        
       if request.method == 'POST':
          if request.POST['documentoidentidad']:
             cedula = request.POST['documentoidentidad']
             try:
                 permiso = Directorios.objects.filter(documentoidentidad=cedula)
             except Trabajoscongresos.DoesNotExist:
                 permiso = False
             if permiso:
                to_json = {'valid':False,'message':'Cedula registrada'}
             else:
                to_json = {'valid':True,'message':'Documento Permitido'}
             return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
          else:
             to_json = {'valid':False,'message':'InCorrecto'}
             return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
       else:
          to_json = {'valid':False,'message':'InCorrecto'}
          return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    else:
       to_json = {'valid':False,'message':'InCorrecto'}
       return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
	   
	   
def validarCorreo(request):
    if request.is_ajax():        
       if request.method == 'POST':
          if request.POST['username']:
             correo = request.POST['username']
             try:
                 permiso = Directorios.objects.filter(correo=correo)
             except Directorios.DoesNotExist:
                 permiso = False
             try:
                 permiso1 = User.objects.filter(username=correo)
             except User.DoesNotExist:
                 permiso1 = False
             if permiso and permiso1:
                to_json = {'valid':False,'message':'<h1 style="color:#F00">Correo registrado</h1>'}
             else:
                to_json = {'valid':True,'message':'<h1 style="color:#0C0">Correo Permitido</h1>'}
             return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
          else:
             to_json = {'valid':False,'message':'<h1 style="color:#F00">InCorrecto</h1>'}
             return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
       else:
          to_json = {'valid':False,'message':'<h1 style="color:#F00">InCorrecto</h1>'}
          return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    else:
       to_json = {'valid':False,'message':'<h1 style="color:#F00">InCorrecto</h1>'}
       return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
	   
def ajaxIdentificacion(request):
    if request.is_ajax():        
       if request.method == 'GET':
          if request.GET['cedula']:
             cedula = request.GET['cedula']
             tipo = request.GET['tipo']
             persona = False
             perfil = False
             try:
                 persona = Directorios.objects.get(Q(tipodoci=tipo) & Q(documentoidentidad=cedula))
             except Directorios.DoesNotExist:
                 persona = False
             if not persona:
                if tipo == "0":
                   tipoDoc ="V"
                if tipo == "1":
                   tipoDoc = "E"
                if tipo == "2":
                   tipoDoc = "P"
                if tipo == "3":
                   tipoDoc = "CE"
                url =  "http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad="+str(tipoDoc)+"&cedula="+str(cedula) 
                f = urllib.urlopen("http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad="+str(tipoDoc)+"&cedula="+str(cedula)) 
                data = f.read()
                f.close()
                lista = string.split( data, '\n' )
                u = 0
                n = []
                h = ""
                for i in lista:
                    u = u + 1
                    try:
                        h = ''.join(xml.etree.ElementTree.fromstring(i).itertext())
                        n.append(h)
                    except:
                        p = "nada"
                u = 0
                cedula = ""
                nombre = ""
                for a in n:
                    if n[u] == u"Cédula:":
                       cedula = n[u + 1]
                    if n[u] == u"Nombre:":
                       nombre = n[u + 1]
                    u = u + 1 
                to_json = {'valid':True,'message':'Persona no registrada','personaID':False,'nombre':nombre,'apellido':'S/N','url':url}
                return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
             else:
                try:
                    perfil = PerfilPublico.objects.get(persona=persona)
                except PerfilPublico.DoesNotExist:
                    perfil = False
                if not perfil:
                   to_json = {'valid':True,'message':'Persona registrada sin perfil','personaID':persona.id,'nombre':persona.nombre,'apellido':persona.apellido}
                else:
                   to_json = {'valid':False,'message':'El documento de identidad que ingreso ya se encuentra registrado y posee una cuenta de usuario activa.','personaID':False,'nombre':'','apellido':''}                   
                return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
          else:
             to_json = {'valid':False,'message':'InCorrecto'}
             return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
       else:
          to_json = {'valid':False,'message':'InCorrecto'}
          return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
    else:
       to_json = {'valid':False,'message':'InCorrecto'}
       return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')
       
       
def consultasCNE(request,dat,dat1):       
	  cedula = dat1
	  tipo = dat
	  url =  "http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad="+str(tipo)+"&cedula="+str(cedula) 
	  f = urllib.urlopen("http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad="+str(tipo)+"&cedula="+str(cedula)) 
	  data = f.read()
	  f.close()
	  lista = string.split( data, '\n' )
	  u = 0
	  n = []
	  h = ""
	  for i in lista:
	      u = u + 1
	      try:
	          h = ''.join(xml.etree.ElementTree.fromstring(i).itertext())
	          n.append(h)
	      except:
	          p = "nada"
	  u = 0
	  cedula = ""
	  nombre = ""
	  centro = ""
	  direccion = ""
	  for a in n:
	      if n[u] == u"Cédula:":
	         cedula = n[u + 1]
	      if n[u] == u"Nombre:":
	         nombre = n[u + 1]
	      if n[u] == u"Centro:":
	         centro = n[u + 1]
	      if n[u] == u"Dirección:":
	         direccion = n[u + 1]
	      u = u + 1 
	  to_json = {'valid':True,'Cedula':cedula,'nombre':nombre,'centro':centro,'direccion':direccion}
	  return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')             
             

       
