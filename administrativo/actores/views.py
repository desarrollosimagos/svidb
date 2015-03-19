# -*- coding: utf8
import datetime
import hashlib
import random
import re
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from forms import *
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from actores.models import *
from perfil.models import SistemaSolicitudes
from plantillas.models import *
from menu.models import *
from django.db.models import Q
from django.contrib.auth.models import User
from perfil.models import *
from congresos.models import Eventos,Trabajoscongresos
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from inicio.models import *
from mapas.models import Colaboradorespersonas
from django.core.mail import send_mail

from django.http import *
from datetime import *
from django.utils import simplejson





#@csrf_protect
def organizaciones(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    #si se recibe el metodo post
    if request.method == 'POST':
       #formulario enviado
       organizaciones_form = OrganizacionesForm(request.POST)
       #validar formulario
       if organizaciones_form.is_valid():
          organizaciones_form.save()
          mensaje=True
          return render_to_response('actores/guardar.html',{'msm':mensaje})   
       else:
          organizaciones_form = OrganizacionesForm()
          mensaje=True
          return render_to_response('actores/organizaciones.html',{'form':organizaciones_form,'msm':mensaje,'persona':persona,'usuario':id_usuario}, context_instance=RequestContext(request))     

    else:
       #formulario incial
       mensaje=False
       organizaciones_form = OrganizacionesForm()
    return render_to_response('actores/organizaciones.html',{'form':organizaciones_form,'persona':persona,'usuario':id_usuario}, context_instance=RequestContext(request))


def personas(request):
    #si se recibe el metodo post
    if request.method == 'POST':
       #formulario enviado
       personas_form = PersonasForm(request.POST)
       #validar formulario
       if personas_form.is_valid():
          personas_form.save()
          mensaje=True
          return render_to_response('actores/guardar.html',{'msm':mensaje})   
       else:
          personas_form = PersonasForm()
          mensaje=True
          return render_to_response('actores/personas.html',{'form':personas_form,'msm':mensaje}, context_instance=RequestContext(request))     

    else:
       #formulario incial
       mensaje=False
       personas_form = PersonasForm()
    return render_to_response('actores/personas.html',{'form':personas_form}, context_instance=RequestContext(request))


def PermisosSubModulosPublicos(request,id):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
	
    try:
        modulos=ModulosPublicos.objects.get(pk=id)
    except ModulosPublicos.DoesNotExist:
        modulos = None	
    try:
        seccionesPanel=PerfilSubModulos.objects.filter(Q(perfil=id_persona) & Q(submodulos__modulos=modulos)).order_by('submodulos__modulos','submodulos__posicion')
    except PerfilSubModulos.DoesNotExist:
        seccionesPanel = None	

    return render_to_response('actores/modulosPermisos.html', {'seccionesPanel':seccionesPanel})


def perfil(request):
    today = datetime.now() #fecha actual
    dateFormat = today.strftime("%Y-%m-%d") # fecha con formato
    try:
        eventos_activos = Eventos.objects.filter(fecha__gt= dateFormat)
    except Eventos.DoesNotExist:
        eventos_activos = None
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password=password)
       if user is not None and user.is_active:
          # Clave correcta, y el usuario esta marcado "activo"
          auth.login(request, user)
          #_username = request.user.username
          id_usuario = User.objects.get(username=username)
          id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
          persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)	  
          try:
              actores=Actores.objects.filter(directorio=persona)
          except Actores.DoesNotExist:
              actores = None
          try:
              mensajes=SistemaMensajeria.objects.filter(destino=persona).count()
          except SistemaMensajeria.DoesNotExist:
              mensajes = None
          try:
              solicitud=SistemaSolicitudes.objects.filter(destino=persona).count()
          except SistemaSolicitudes.DoesNotExist:
              solicitud = None
			  
          try:
              seccionesPanel=PerfilModulos.objects.filter(Q(perfil=id_persona) & Q(activo=True)).order_by('modulos__paneles','modulos__posicion')
          except PerfilModulos.DoesNotExist:
              seccionesPanel = None	
			  
          try:
              principal = Secciones.objects.get(id=8)
          except Secciones.DoesNotExist:
              principal = None

          try:
              sub = Categorias.objects.get(id=39)
          except Categorias.DoesNotExist:
              sub = None
		
          try:
              lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
          except TemplatesInfoLateral.DoesNotExist:
              lateral = None
          
          return render_to_response("actores/panel.html",{'persona':persona,'actores':actores,'usuario':id_usuario,'mensajes':mensajes,'solicitud':solicitud,'eventos_activos':eventos_activos,'error':'No','seccionesPanel':seccionesPanel,'principal':principal,'sub':sub,'lateral':lateral}, context_instance=RequestContext(request))
       else:
          # Mostrar una pagina de error
          return render_to_response('actores/perfil.html',{'error':'Si'})
    else:
       if not request.user.is_authenticated():
          return render_to_response("actores/perfil.html")
       else:
          _username = request.user.username
          id_usuario = User.objects.get(username=_username)
          id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
          persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
          try:
              actores=Actores.objects.filter(directorio=persona)
          except Actores.DoesNotExist:
              actores = None
          mensajes=SistemaMensajeria.objects.filter(destino=persona)
          try:
              mensajes=SistemaMensajeria.objects.filter(destino=persona).count()
          except SistemaMensajeria.DoesNotExist:
              mensajes = None
          try:
              solicitud=SistemaSolicitudes.objects.filter(destino=persona).count()
          except SistemaSolicitudes.DoesNotExist:
              solicitud = None
			  
          try:
              seccionesPanel=PerfilModulos.objects.filter(Q(perfil=id_persona) & Q(activo=True)).order_by('modulos__paneles','modulos__posicion')
          except PerfilModulos.DoesNotExist:
              seccionesPanel = None		
			  
          try:
              principal = Secciones.objects.get(id=8)
          except Secciones.DoesNotExist:
              principal = None

          try:
              sub = Categorias.objects.get(id=39)
          except Categorias.DoesNotExist:
              sub = None
		
          try:
              lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
          except TemplatesInfoLateral.DoesNotExist:
              lateral = None
			  
          return render_to_response("actores/panel.html",{'persona':persona,'actores':actores,'usuario':id_usuario,'mensajes':mensajes,'solicitud':solicitud,'eventos_activos':eventos_activos,'error':'No','seccionesPanel':seccionesPanel,'principal':principal,'sub':sub,'lateral':lateral}, context_instance=RequestContext(request))

def logout(request):
    auth.logout(request)
    # Redirigir a una pagina de exito.
    return render_to_response("actores/perfil.html")
	
def mis_datos(request):
     _username = request.user.username
     id_usuario = User.objects.get(username=_username)
     print id_usuario.id
     id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
     persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
     if request.method == 'POST':
        personas_edit = PersonasEditForm(request.POST, instance = persona)
        if personas_edit.is_valid():
            personas_edit.save()
            personas_edit = PersonasEditForm(instance=persona)
            return render_to_response("actores/mis_datos.html",{'formulario':personas_edit,'persona':persona}, context_instance=RequestContext(request))
        else:
            print 'no valido'
            return render_to_response("actores/mis_datos.html",{'formulario':personas_edit,'persona':persona}, context_instance=RequestContext(request))
     else:
        personas_post_edit = PersonasEditForm(instance=persona)
        return render_to_response("actores/mis_datos.html",{'formulario':personas_post_edit,'persona':persona}, context_instance=RequestContext(request))
	
	
	
def nuevo_usuario(request):
     if request.method == 'POST':
        personas_form_post = PersonasRegForm(request.POST)
        formulario_post = UserCreationForm(request.POST)
        if request.POST['documentoidentidad'] :
           cedula = request.POST['documentoidentidad']
        else:
           cedula = None
        
        try:
           val = int(cedula)
        except ValueError:
           val = None      

        if val:
            try:
                validando_persona = Directorios.objects.get(documentoidentidad=cedula)
            except Directorios.DoesNotExist:
                validando_persona = None
        else:
           validando_persona = None
       
		   
        if validando_persona:
           validando_persona.correo = request.POST['username']
           validando_persona.save()
           persona_id=validando_persona.id
        else:
           persona_id=None  
		   
        try:
           validando_user = PerfilPublico.objects.get(persona=persona_id)
        except PerfilPublico.DoesNotExist:
           validando_user = None
				
        if formulario_post.is_valid() and validando_user==None:
           if persona_id :
              print '1'
           else:
              if personas_form_post.is_valid():
                  #validando_persona = personas_form_post.save()
                  validando_persona = Directorios(tipodoci=request.POST['tipodoci'],documentoidentidad=request.POST['documentoidentidad'],nombre=request.POST['nombre'],apellido=request.POST['apellido'],correo=request.POST['username'])
                  validando_persona.save()
              else:
                  return render_to_response('actores/nuevo_usuario.html',{'formulario':formulario_post,'error':'Si','personas_form':personas_form_post}, context_instance=RequestContext(request))
 
           result_user = formulario_post.save()

           perfil_publico = PerfilPublico(user=result_user,persona=validando_persona)
           perfil_publico.save()
		   
           #formulario0 = UserCreationForm()
           #personas_form = PersonasRegForm()

           personas_form = PersonasRegForm(request.POST)
           formulario = UserCreationForm(request.POST)
           salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
           validacion = validaciones(usuario=perfil_publico,codigo=salt,estatu=0,estado=True)
           validacion.save()
           subject, from_email, to = 'SVIDB Registro de Usuarios', settings.EMAIL_HOST_USER, request.POST['username']
           text_content = 'SVIDB Registro de Usuarios'
           d= settings.URL_SET_SITE
           ctx_dict = {'salt': salt,'d': d}
           html_content= render_to_string('correos/plantillas/validacion.txt',ctx_dict)
           msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
           msg.attach_alternative(html_content, "text/html")
           msg.send()
           formulario = UserCreationForm()
           personas_form = PersonasRegForm()

           return render_to_response('actores/nuevo_usuario.html',{'formulario':formulario,'error':'No','personas_form':personas_form}, context_instance=RequestContext(request))
#		   return render_to_response('perfil/verificacion2.html',{'codigo':salt,'error':'No','correo':to}, context_instance=RequestContext(request))
        else:
           personas_form = PersonasRegForm(request.POST)
           formulario = UserCreationForm(request.POST)
#           return render_to_response('actores/nuevo_usuario.html',{'formulario':formulario_post,'error':'Si','personas_form':personas_form_post}, context_instance=RequestContext(request))
           return render_to_response('actores/nuevo_usuario.html',{'formulario':formulario,'error':'Si','personas_form':personas_form}, context_instance=RequestContext(request))
     else:
        formulario = UserCreationForm()
        personas_form = PersonasRegForm()
        return render_to_response('actores/nuevo_usuario.html',{'formulario':formulario,'personas_form':personas_form}, context_instance=RequestContext(request))

def coautor(request,id):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    print id_usuario.id
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    #si se recibe el metodo post
    Trabajoscong = Trabajoscongresos.objects.get(pk= id)
    if request.method == 'POST':
       #formulario enviado
       personas_form = coautorform(request.POST)
       #validar formulario
	   
       try:
          if request.POST['documentoidentidad']:
             cedulaUser = request.POST['documentoidentidad']
             tipodoc = request.POST['tipodoci']
             try:
                 val = int(cedulaUser)
             except ValueError:
                 val = None      
             if val:
                 dir = Directorios.objects.get(documentoidentidad = cedulaUser)
             else:
                 dir = None
          else:
             dir = None
       except Directorios.DoesNotExist:
          dir=None
       if dir:
          Trabajoscong.coautores.add(dir)
          return HttpResponseRedirect("/panel/eventos/trabajos/editar/"+id)
       else:
          if personas_form.is_valid():
             personas_form.save()
             dir = Directorios.objects.get(documentoidentidad= request.POST['documentoidentidad'])
             Trabajoscong.coautores.add(dir)
             return HttpResponseRedirect("/panel/eventos/trabajos/editar/"+id)  
          else:
#             personas_form = coautorform()
             mensaje=True
             return render_to_response('actores/coa.html',{'form':personas_form,'msm':mensaje,'persona':persona,'congreso':Trabajoscong}, context_instance=RequestContext(request))     
    else:
       #formulario incial
       mensaje=False
       personas_form = coautorform()
    return render_to_response('actores/coa.html',{'form':personas_form,'id':id,'persona':persona,'congreso':Trabajoscong}, context_instance=RequestContext(request))
	
	
def instituciones(request,id):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    print id_usuario.id
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    #si se recibe el metodo post
    Trabajoscong = Trabajoscongresos.objects.get(pk= id)
    if request.method == 'POST' and request.POST['rif']:
       #formulario enviado
       #validar formulario
       try:
          int = Actores.objects.get(rif= request.POST['rif'])
       except Actores.DoesNotExist:
          int = None
       
       if int:
          Trabajoscong.colectivos.add(int)
          return HttpResponseRedirect("/panel/eventos/trabajos/editar/"+id)
       else:
          institucioform = InstitucionesForm(request.POST)
          if institucioform.is_valid():
              int = institucioform.save() 
              Trabajoscong.colectivos.add(int)
              return HttpResponseRedirect("/panel/eventos/trabajos/editar/"+id)
          else:
              institucioform = InstitucionesForm()
              mensaje=True
              return render_to_response('actores/inst.html',{'form':institucioform,'msm':mensaje,'persona':persona}, context_instance=RequestContext(request))     

    else:
       #formulario incial
       mensaje=False
       institucioform = InstitucionesForm()
    return render_to_response('actores/inst.html',{'form':institucioform,'id':id,'persona':persona}, context_instance=RequestContext(request))
	

	
def miembrosInstituciones(request,id):
     if request.method == 'POST':
        miembros_form = MiembrosInstForm(request.POST)
        if miembros_form.is_valid() :
           miembros_form.save()
           miembros_form = MiembrosInstForm()
           return render_to_response('actores/instmiembros.html',{'miembros_form':miembros_form}, context_instance=RequestContext(request))
        else:
           return render_to_response('actores/instmiembros.html',{'miembros_form':miembros_form}, context_instance=RequestContext(request))
     else:
        miembros_form = MiembrosInstForm()
        return render_to_response('actores/instmiembros.html',{'miembros_form':miembros_form}, context_instance=RequestContext(request))
		
		
def mensajes(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    mensajes = SistemaMensajeria.objects.filter(destino=persona)
    paginator = Paginator(mensajes, 10)
    page = request.GET.get('page')
    try:
        mesn = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mesn = paginator.page(1)
    #except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
    #    mesn = paginator.page(paginator.num_pages)

    return render_to_response('actores/mensajes.html', {"mesn": mesn,'persona':persona})
	
	
def solicitudes(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    mensajes = SistemaSolicitudes.objects.filter(destino=persona)
    paginator = Paginator(mensajes, 10)
    page = request.GET.get('page')
    try:
        mesn = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        mesn = paginator.page(1)
    #except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
    #    mesn = paginator.page(paginator.num_pages)

    return render_to_response('actores/solicitudes.html', {"mesn": mesn,'persona':persona})
	
def vermensajes(request,id):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    mensaje =  get_object_or_404(SistemaMensajeria, pk=id)
    return render_to_response('actores/vermensaje.html', {"mensaje": mensaje,'persona':persona})
	
def redactar(request):
     if request.method == 'POST':
        redactarform = RedactarForm(request.POST)
        if redactarform.is_valid():

           return render_to_response('actores/nuevo_usuario.html',{'formulario':formulario,'mensaje':'Registro Exitoso','personas_form':personas_form}, context_instance=RequestContext(request))
        else:
           return render_to_response('actores/nuevo_usuario.html',{'formulario':formulario_post,'mensaje':'No se pudo completar el registro','personas_form':personas_form_post}, context_instance=RequestContext(request))
     else:
        redactarform = RedactarForm()
        return render_to_response('actores/redactar.html',{'redactarform':redactarform}, context_instance=RequestContext(request))
		
		
def colaboradores(request):
    try:
        coor_general = Equipos.objects.get(tipocolaborador=10)
    except Equipos.DoesNotExist:
        coor_general = None

    try:
        nucleo = Equipos.objects.filter(tipocolaborador=9).filter(escoord=False)
    except Equipos.DoesNotExist:
        nucleo = None
    try:
        nucleo_coord = Equipos.objects.filter(tipocolaborador=9).filter(escoord=True)
    except Equipos.DoesNotExist:
        nucleo_coord = None
#Comite de Especies
    try:
        especies = Equipos.objects.filter(tipocolaborador=2).filter(escoord=False)
    except Equipos.DoesNotExist:
        especies = None
    try:
        especies_coord = Equipos.objects.filter(tipocolaborador=2).filter(escoord=True)
    except Equipos.DoesNotExist:
        especies_coord = None
#Comite de Actores
    try:
        actores = Equipos.objects.filter(tipocolaborador=4).filter(escoord=False)
    except Equipos.DoesNotExist:
        actores = None
    try:
        actores_coord = Equipos.objects.filter(tipocolaborador=4).filter(escoord=True)
    except Equipos.DoesNotExist:
        actores_coord = None
#Comite de Areas
    try:
        areas = Equipos.objects.filter(tipocolaborador=3).filter(escoord=False)
    except Equipos.DoesNotExist:
        areas = None
    try:
        areas_coord = Equipos.objects.filter(tipocolaborador=3).filter(escoord=True)
    except Equipos.DoesNotExist:
        areas_coord = None

#Generacion de textos
    try:
        textos = Colaboradorespersonas.objects.values('persona__nombre','persona__apellido').filter(tipoColaboracion=9).distinct('persona')
    except Colaboradorespersonas.DoesNotExist:
        textos = None

#Revision de textos
    try:
        revision = Colaboradorespersonas.objects.values('persona__nombre','persona__apellido').filter(tipoColaboracion=8).distinct('persona')
    except Colaboradorespersonas.DoesNotExist:
        revision = None
		
#Transcripcion
    try:
        transc = Colaboradorespersonas.objects.values('persona__nombre','persona__apellido').filter(tipoColaboracion=10).distinct('persona')
    except Colaboradorespersonas.DoesNotExist:
        transc = None

#Diseño y Programacion
    try:
        program = Colaboradorespersonas.objects.values('persona__nombre','persona__apellido').filter(tipoColaboracion=11).distinct('persona')
    except Colaboradorespersonas.DoesNotExist:
        program = None
		
#Mapas
    try:
        mapas = Colaboradorespersonas.objects.values('persona__nombre','persona__apellido').filter(tipoColaboracion=7).distinct('persona')
    except Colaboradorespersonas.DoesNotExist:
        mapas = None
    try:
        mapas1 = Colaboradorespersonas.objects.values('persona__nombre','persona__apellido').filter(tipoColaboracion=6).distinct('persona')
    except Colaboradorespersonas.DoesNotExist:
        mapas1 = None
    try:
        mapas2 = Colaboradorespersonas.objects.values('persona__nombre','persona__apellido').filter(tipoColaboracion=5).distinct('persona')
    except Colaboradorespersonas.DoesNotExist:
        mapas2 = None
    try:
        mapas3 = Colaboradorespersonas.objects.values('persona__nombre','persona__apellido').filter(tipoColaboracion=4).distinct('persona')
    except Colaboradorespersonas.DoesNotExist:
        mapas3 = None
#Cambio de Nomenclatura		
    try:
        nomen = Colaboradorespersonas.objects.values('persona__nombre','persona__apellido').filter(tipoColaboracion=13).distinct('persona')
    except Colaboradorespersonas.DoesNotExist:
        nomen = None

#BancoAudioVisual
    try:
        banco = Bancoaudiovisuals.objects.values('directorio__nombre','directorio__apellido').distinct('directorio')
    except Bancoaudiovisuals.DoesNotExist:
        banco = None
		
#Institutos Colaboradores
    try:
        colabinstitute = Colaboradoresinstitutes.objects.values('actore__nombre_completo','actore__siglas').distinct('actore')
    except Colaboradoresinstitutes.DoesNotExist:
        colabinstitute = None
		


    return render_to_response('pagina/colaboradores.html',{'coor_general':coor_general,'nucleo':nucleo,'nucleo_coord':nucleo_coord,'areas':areas,'areas_coord':areas_coord,'actores_coord':actores_coord,'actores':actores,'especies_coord':especies_coord,'especies':especies,'textos':textos,'revision':revision,'transc':transc,'program':program,'mapas':mapas,'mapas1':mapas1,'mapas2':mapas2,'mapas3':mapas3,'banco':banco,'colabinstitute':colabinstitute,'nomen':nomen}, context_instance=RequestContext(request))


def Avances(request):
#Generacion de textos
    try:
        especies_act = Colaboradorespersonas.objects.filter(tipoColaboracion=9).filter(estatu=0).exclude(taxon__isnull=True)
    except Colaboradorespersonas.DoesNotExist:
        especies_act = None
    try:
        especies_inac = Colaboradorespersonas.objects.filter(tipoColaboracion=9).filter(estatu=2).exclude(taxon__isnull=True)
    except Colaboradorespersonas.DoesNotExist:
        especies_inac = None
		
    try:
        areas_act = Colaboradorespersonas.objects.filter(tipoColaboracion=9).filter(estatu=0).exclude(areas__isnull=True)
    except Colaboradorespersonas.DoesNotExist:
        areas_act = None
    try:
        areas_inac = Colaboradorespersonas.objects.filter(tipoColaboracion=9).filter(estatu=2).exclude(areas__isnull=True)
    except Colaboradorespersonas.DoesNotExist:
        areas_inac = None
		
    try:
        actores_act = Colaboradorespersonas.objects.filter(tipoColaboracion=9).filter(estatu=0).exclude(colectivos__isnull=True)
    except Colaboradorespersonas.DoesNotExist:
        actores_act = None
    try:
        actores_inac = Colaboradorespersonas.objects.filter(tipoColaboracion=9).filter(estatu=2).exclude(colectivos__isnull=True)
    except Colaboradorespersonas.DoesNotExist:
        actores_inac = None
		
    try:
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=30)
    except Categorias.DoesNotExist:
        sub = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
    return render_to_response('pagina/avances.html',{'especies_act':especies_act,'especies_inac':especies_inac,'areas_act':areas_act,'areas_inac':areas_inac,'actores_act':actores_act,'actores_inac':actores_inac,'principal':principal,'sub':sub,'lateral':lateral}, context_instance=RequestContext(request))
	
	

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
        actores = Actores.objects.get(id=id)
    except Actores.DoesNotExist:
        actores = None
		
    try:
        redes = Redessociales.objects.filter(actore=actores)
    except Redessociales.DoesNotExist:
        redes = None

    if actores.categoriact:		
       try:
           categoria = Categorias.objects.get(id=actores.categoriact.id)
       except Categorias.DoesNotExist:
           categoria = None
       if categoria.seccione:
          try:
              secciones = Secciones.objects.get(id=categoria.seccione.id)
          except Secciones.DoesNotExist:
              secciones = None
       else:
          secciones = None
    else:
       categoria = None
       secciones = None
	   
    
    if actores.tipocolec == None:
       tip_id = None
    else:
       tip_id = actores.tipocolec.id
		
    try:
        sub = SubTipoCategorias.objects.get(id=tip_id)
    except SubTipoCategorias.DoesNotExist:
        sub = None

    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=secciones) & Q(subseccion=categoria)) | (Q(seccion=secciones) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None

    try:
        contribuciones = Colaboradorespersonas.objects.filter(colectivos=actores).order_by('update','estatu')
    except Colaboradorespersonas.DoesNotExist:
        contribuciones = None

    return render_to_response('actores/ficha.html', {'actores':actores,'categoria':categoria,'secciones':secciones,'sub':sub,'lateral':lateral,'redes':redes,'persona':persona,'usuario':id_usuario,'contribuciones':contribuciones})
	
	
def ver_mapas(request,value1):
    return render_to_response('mapas/ver.html', {'value1':value1})
	
def actor_paso1(request,id):
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
		
    return render_to_response('actores/colectivo1.html',{'id':id,'persona':persona})
	
def paso2_colectivos(request,id):
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
		
     if request.POST:
        nombre = request.POST['nombre']
        try:
           actor =  Actores.objects.filter(nombre_completo__icontains=nombre)
        except Actores.DoesNotExist:
           actor = None
        organizaciones_form = InstitucionesForm()
        return render_to_response('actores/colectivo2.html', {'actor':actor,'nombre':nombre,'form':organizaciones_form,'persona':persona,'id':id})   
     else:
         return render_to_response('actores/colectivo1.html')  

def paso3_colectivos(request,id,actor): 
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
       actor =  Actores.objects.get(id=actor)
    except Actores.DoesNotExist:
       actor = None
    if actor == None:
       organizaciones_form = InstitucionesForm()
    else:
       organizaciones_form = InstitucionesForm(instance=actor)
    return render_to_response('actores/colectivo3.html', {'form':organizaciones_form,'actor':actor,'id':id,'persona':persona})   
	
	
def paso4_colectivos(request,id,actor):
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
       actor =  Actores.objects.get(id=actor)
    except Actores.DoesNotExist:
       actor = None
    if actor == None:
       organizaciones_form = InstitucionesForm()
    else:
       organizaciones_form = InstitucionesForm(instance=actor)
    return render_to_response('actores/colectivo4.html',{'form':organizaciones_form,'persona':persona,'id':id,'id2':actor.id})     
	
def paso5_colectivos(request,id,actor):
    Trabajoscong = Trabajoscongresos.objects.get(pk= id)
    try:
        int = Actores.objects.get(pk= actor)
    except Actores.DoesNotExist:
        int = None
    if int:
       Trabajoscong.colectivos.add(int)
    return HttpResponseRedirect("/panel/eventos/trabajos/editar/"+id)

def paso6_colectivos(request,id,actor):	
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
    Trabajoscong = Trabajoscongresos.objects.get(pk= id)
	 
    try:
       int = Actores.objects.get(pk= actor)
    except Actores.DoesNotExist:
        int = None
    if request.method == 'POST':
        organizaciones_form = InstitucionesForm(request.POST, instance = int)
        if organizaciones_form.is_valid():
            org = organizaciones_form.save()
            if org:
               Trabajoscong.colectivos.add(org)
            return HttpResponseRedirect("/panel/eventos/trabajos/editar/"+id)
        else:
           
            return render_to_response('actores/colectivo3.html', {'form':organizaciones_form,'actor':int,'id':id,'persona':persona}) 
    else:
        organizaciones_form = InstitucionesForm(request.POST, instance = int)
        return render_to_response('actores/colectivo3.html', {'form':organizaciones_form,'actor':int,'id':id,'persona':persona}) 
		
		
def paso7_colectivos(request,id):	
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
    Trabajoscong = Trabajoscongresos.objects.get(pk= id)
	 
    if request.method == 'POST':
        organizaciones_form = InstitucionesForm(request.POST)
        if organizaciones_form.is_valid():
            org = organizaciones_form.save()
            if org:
               Trabajoscong.colectivos.add(org)
            return HttpResponseRedirect("/panel/eventos/trabajos/editar/"+id)
        else:
           
            return render_to_response('actores/colectivo2.html', {'actor':None,'nombre':request.POST['nombre_bb'],'form':organizaciones_form,'persona':persona,'id':id})  
    else:
        organizaciones_form = InstitucionesForm(request.POST)
        return render_to_response('actores/colectivo2.html', {'actor':None,'nombre':request.POST['nombre_bb'],'form':organizaciones_form,'persona':persona,'id':id})  
	
def ajax_2(request):
    if request.method=='GET' or not request.POST.__contains__('start'):
        return HttpResponseForbidden()
 
    # Hacemos la consulta para aquellos elementos que empiecen por start ordenados por nombre
    query = Actores.objects.filter(nombre__istartswith=request.POST['start']).order_by('nombre')
 
    # Serializamos
    objects = u'{items: [\n'
    for i in query:
        objects += u'{"0":"%s"},\n' % (i.nombre.replace('"',''))
    objects=objects.strip(",\n");
    objects+=u']}\n'
 
    return HttpResponse(objects,mimetype="text/plain")

	
def main(request):
   return render_to_response('actores/colectivo1.html', context_instance=RequestContext(request))
 
 
def ajax(request):
   if request.POST.has_key('client_response'):
        x = request.POST['client_response']   
        cc = request.POST['client_response']               
        y = socket.gethostbyname(x)                           
        response_dict = {}                                          
        response_dict.update({'server_response':  cc })                                                                   
        return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript') 
   else:
        return render_to_response('actores/colectivo1.html', context_instance=RequestContext(request))
