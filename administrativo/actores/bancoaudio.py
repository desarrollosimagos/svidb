# -*- coding: utf8
from gestion.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from actores.models import *
from areas.models import *
from especies.models import *
from plantillas.models import *
from menu.models import *
from perfil.models import PerfilPublico,ModulosPublicos,PerfilModulos
from django.db.models import Q
from forms import *
from inicio.models import Tipocolaboracion
from mapas.models import Colaboradorespersonas,contriBiblioteca,contriAudio,contriAvistamiento

def index(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    return render_to_response('actores/bancoaudio/index.html', {'persona':persona})
	
def lista(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    try:
        biblioteca = Bancoaudiovisuals.objects.filter(directorio=persona).order_by('fecha')
    except Bancoaudiovisuals.DoesNotExist:
        biblioteca = None
    return render_to_response('actores/bancoaudio/tus_aportes.html', {'persona':persona,'biblioteca':biblioteca})
	
#@csrf_protect
def agregar(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    #si se recibe el metodo post
    if request.method == 'POST':
       #formulario enviado
       banco_form = AgregarBancoaudiovisualsPublic(request.POST, request.FILES)
       #validar formulario
       if banco_form.is_valid():
          banco = banco_form.save()
          today = datetime.now()
          dateFormat = today.strftime("%Y-%m-%d")
          tipocolaboracion = Tipocolaboracion.objects.get(id=15)
          titulo = u'Colaboracion en Banco Audiovisual: %s' %(banco.id)
          contribucion = Colaboradorespersonas(fecha=dateFormat,tipoColaboracion=tipocolaboracion,titulo=titulo,userupdate=id_usuario,persona=persona,estatu=3)
          contribucion.save()
          aporte = contriAudio(contribucion=contribucion,audio=banco)
          aporte.save()
          mensaje=True
          return render_to_response('actores/bancoaudio/index.html',{'msm':mensaje,'persona':persona,'id_usuario':id_usuario})   
       else:
          biblioteca_form = AgregarBancoaudiovisualsPublic(request.POST)
          mensaje=True
          return render_to_response('actores/bancoaudio/nuevo.html',{'form':banco_form,'msm':mensaje,'persona':persona,'usuario':id_usuario}, context_instance=RequestContext(request))     

    else:
       #formulario incial
       mensaje=False
       banco_form = AgregarBancoaudiovisualsPublic()
    return render_to_response('actores/bancoaudio/nuevo.html',{'form':banco_form,'persona':persona,'usuario':id_usuario}, context_instance=RequestContext(request))
	
def galeria(request,elemento,id):
    if elemento == 'actor':
       try:
           datos = Actores.objects.get(id=id)
       except Actores.DoesNotExist:
           datos = None

    if elemento == 'areas':
       try:
           datos = Areas.objects.get(id=id)
       except Areas.DoesNotExist:
           datos = None
		   
    if elemento == 'taxon':
       try:
           datos = DetalleTaxon.objects.get(id=id)
       except DetalleTaxon.DoesNotExist:
           datos = None
    return render_to_response('actores/bancoaudio/galeria.html', {'elemento':datos})
	
	
def PaginadorGaleria(request,elemento,id,pagina):
    if elemento == 'actor':
       try:
           datos = Actores.objects.get(id=id)
       except Actores.DoesNotExist:
           datos = None

    if elemento == 'areas':
       try:
           datos = Areas.objects.get(id=id)
       except Areas.DoesNotExist:
           datos = None
		   
    if elemento == 'taxon':
       try:
           datos = DetalleTaxon.objects.get(id=id)
       except DetalleTaxon.DoesNotExist:
           datos = None
    image_list = datos.bancoaudio.all()
		   
    paginator = Paginator(image_list, 4)
    page = pagina
    try:
        mesn = paginator.page(page)
    except PageNotAnInteger:
        mesn = paginator.page(1)
    return render_to_response('actores/bancoaudio/paginadorGaleria.html', {'elemento':elemento,'mesn':mesn,'id':id})

def PaginadorGaleria2(request,pagina,id):
    try:
        dat = Bancoaudiovisuals.objects.get(pk=id)
    except Bancoaudiovisuals.DoesNotExist:
        dat = None

    try:
        datos = Bancoaudiovisuals.objects.filter()
    except Bancoaudiovisuals.DoesNotExist:
        datos = None

#    image_list = datos.all()
		   
    paginator = Paginator(datos, 10)
    page = pagina
    try:
        mesn = paginator.page(page)
    except PageNotAnInteger:
        mesn = paginator.page(1)
    return render_to_response('actores/bancoaudio/paginadorGaleria2.html', {'mesn':mesn,'dat':dat})

def bancoVer(request,id):
    try:
        datos = Bancoaudiovisuals.objects.get(pk=id)
    except Bancoaudiovisuals.DoesNotExist:
        datos = None
    return render_to_response('actores/bancoaudio/bancover.html', {'datos':datos})

	
	

