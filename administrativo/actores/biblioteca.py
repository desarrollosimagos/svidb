# -*- coding: utf8
from gestion.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from actores.models import *
from plantillas.models import *
from menu.models import *
from perfil.models import PerfilPublico,ModulosPublicos,PerfilModulos
from django.db.models import Q
from forms import *
from inicio.models import Tipocolaboracion
from mapas.models import Colaboradorespersonas,contriBiblioteca,contriAudio,contriAvistamiento
from django.utils import simplejson
	
def Biblioteca(request,id):
    try:
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=35)
    except Categorias.DoesNotExist:
        sub = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None

    try:
        biblioteca = Bibliotecas.objects.filter(Q(estatu=0) & Q(repositoriolinea__isnull=False)).exclude(repositoriolinea='').order_by('titulo')
    except Glosario.DoesNotExist:
        biblioteca = None

    if len(biblioteca) == 0:
       mesn=None
    else:
        paginator = Paginator(biblioteca, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)

    return render_to_response('actores/biblioteca.html', {"mesn": mesn,"principal":principal,"sub":sub,"lateral":lateral})
	
def buscar(request,id,letra):
    try:
        if letra == '' :
            biblioteca = Bibliotecas.objects.filter(Q(estatu=0) & Q(repositoriolinea__isnull=False)).exclude(repositoriolinea='').order_by('titulo')
        else:
            biblioteca = Bibliotecas.objects.filter(Q(estatu=0) & Q(repositoriolinea__isnull=False)).filter(Q(titulo__icontains=letra) | Q(autores__icontains=letra)).exclude(repositoriolinea='').order_by('titulo')
    except Glosario.DoesNotExist:
        biblioteca = None

    if len(biblioteca) == 0:
       mesn=None
    else:
        paginator = Paginator(biblioteca, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)

    return render_to_response('actores/buscar_biblioteca.html', {"mesn": mesn,"letra":letra})
	

def buscar2(request,id):
    try:
        biblioteca = Bibliotecas.objects.filter(Q(estatu=0) & Q(repositoriolinea__isnull=False)).exclude(repositoriolinea='').order_by('titulo')
    except Glosario.DoesNotExist:
        biblioteca = None

    if len(biblioteca) == 0:
       mesn=None
    else:
        paginator = Paginator(biblioteca, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)

    return render_to_response('actores/buscar_biblioteca.html', {"mesn": mesn})
	

def index(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    return render_to_response('actores/biblioteca/index.html', {'persona':persona})
	
def lista(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    try:
        biblioteca = Bibliotecas.objects.filter(directorio=persona).order_by('titulo')
    except Bibliotecas.DoesNotExist:
        biblioteca = None
    return render_to_response('actores/biblioteca/tus_aportes.html', {'persona':persona,'biblioteca':biblioteca})

	
#@csrf_protect
def agregar(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    #si se recibe el metodo post
    if request.method == 'POST':
       #formulario enviado
       biblioteca_form = AgregarBibliotecaPublic(request.POST, request.FILES)
       #validar formulario
       if biblioteca_form.is_valid():
          biblioteca = biblioteca_form.save()
          today = datetime.now()
          dateFormat = today.strftime("%Y-%m-%d")
          tipocolaboracion = Tipocolaboracion.objects.get(id=14)
          titulo = u'Colaboracion en biblioteca: %s' %(request.POST['titulo'])
          contribucion = Colaboradorespersonas(fecha=dateFormat,tipoColaboracion=tipocolaboracion,titulo=titulo,userupdate=id_usuario,persona=persona,estatu=3)
          contribucion.save()
          aporte = contriBiblioteca(contribucion=contribucion,boblioteca=biblioteca)
          aporte.save()
          mensaje=True
          return render_to_response('actores/biblioteca/index.html',{'msm':mensaje,'persona':persona,'id_usuario':id_usuario})   
       else:
          biblioteca_form = AgregarBibliotecaPublic(request.POST)
          mensaje=True
          return render_to_response('actores/biblioteca/nuevo.html',{'form':biblioteca_form,'msm':mensaje,'persona':persona,'usuario':id_usuario}, context_instance=RequestContext(request))     

    else:
       #formulario incial
       mensaje=False
       biblioteca_form = AgregarBibliotecaPublic()
    return render_to_response('actores/biblioteca/nuevo.html',{'form':biblioteca_form,'persona':persona,'usuario':id_usuario}, context_instance=RequestContext(request))
	

	
