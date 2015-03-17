# -*- coding: utf8
from gestion.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from actores.models import *
from especies.models import *
from plantillas.models import *
from menu.models import *
from mapas.models import *
from perfil.models import PerfilPublico,ModulosPublicos,PerfilModulos
from django.db.models import *
from listasTematicas.models import *
from mapas.models import Colaboradorespersonas,contriBiblioteca,contriAudio,contriAvistamiento,Avistamientos
from forms import AvistamientoForm

def index(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    return render_to_response('mapas/avistamientos/index.html', {'persona':persona})
	
def lista(request):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    try:
        biblioteca = Avistamientos.objects.filter(persona=persona).order_by('fecha')
    except Avistamientos.DoesNotExist:
        biblioteca = None
    return render_to_response('mapas/avistamientos/tus_aportes.html', {'persona':persona,'biblioteca':biblioteca})
	
#@csrf_protect
def agregar(request,id):
    _username = request.user.username
    id_usuario = User.objects.get(username=_username)
    id_persona = get_object_or_404(PerfilPublico, user=id_usuario.id)
    persona =  get_object_or_404(Directorios, pk=id_persona.persona.id)
    try:
        lista_exo = Taxon.objects.get(pk=id)
    except Taxon.DoesNotExist:
        lista_exo = None
    #si se recibe el metodo post
    if request.method == 'POST':
       #formulario enviado
       avistamiento = AvistamientoForm(request.POST, request.FILES)
       #validar formulario
       if avistamiento.is_valid():
          avis = avistamiento.save()
          today = datetime.now()
          dateFormat = today.strftime("%Y-%m-%d")
          tipocolaboracion = Tipocolaboracion.objects.get(id=16)
          titulo = u'Registro de Avistamiento Exotica: %s' %(avis.id)
          contribucion = Colaboradorespersonas(fecha=dateFormat,tipoColaboracion=tipocolaboracion,titulo=titulo,userupdate=id_usuario,persona=persona,estatu=3)
          contribucion.save()
          aporte = contriAvistamiento(contribucion=contribucion,avistamiento=avis)
          aporte.save()
          mensaje=True
          return render_to_response('mapas/avistamientos/index.html',{'msm':mensaje,'persona':persona,'id_usuario':id_usuario,'lista_exo':lista_exo})   
       else:
          avistamiento = AvistamientoForm(request.POST)
          mensaje=True
          return render_to_response('mapas/avistamientos/nuevo.html',{'form':avistamiento,'msm':mensaje,'persona':persona,'usuario':id_usuario,'lista_exo':lista_exo}, context_instance=RequestContext(request))     

    else:
       #formulario incial

       mensaje=False
       avistamiento = AvistamientoForm()
    return render_to_response('mapas/avistamientos/nuevo.html',{'form':avistamiento,'persona':persona,'usuario':id_usuario,'lista_exo':lista_exo}, context_instance=RequestContext(request))
	
	
def mostrar(request,id):
    try:
        lista_exo = Taxon.objects.filter(detalletaxon__espexot=True).annotate(numeroavistamientos = Count('avistamientos')).order_by('-numeroavistamientos')
    except Taxon.DoesNotExist:
        lista_exo = None
    else:
        paginator = Paginator(lista_exo, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)
    return render_to_response('mapas/avistamientos/exo.html', {"mesn": mesn,'vueltas':1})
	
def mostrar2(request,id):
    try:
        lista_exo = Taxon.objects.get(pk=id)
    except Taxon.DoesNotExist:
        lista_exo = None
		
    return render_to_response('mapas/avistamientos/exo2.html', {"mesn": lista_exo})