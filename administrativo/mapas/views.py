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
from mapas.models import *

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
		   
    paginator = Paginator(datos, 63)
    page = pagina
    try:
        mesn = paginator.page(page)
    except PageNotAnInteger:
        mesn = paginator.page(1)
    return render_to_response('actores/bancoaudio/paginadorGaleria2.html', {'mesn':mesn,'dat':dat})

def listaColaboraciones(request,pagina,estatus):
    try:
        if estatus == '2':
           datos = Colaboradorespersonas.objects.filter(Q(estatu=2) | Q(estatu=3)).exclude(taxon__isnull=True).order_by('taxon__nombrecomun')
        else:
           datos = Colaboradorespersonas.objects.filter(estatu=estatus).exclude(taxon__isnull=True).order_by('taxon__nombrecomun')
    except Colaboradorespersonas.DoesNotExist:
        datos = None
    paginator = Paginator(datos, 30)
    page = pagina
    try:
        mesn = paginator.page(page)
    except PageNotAnInteger:
        mesn = paginator.page(1)
    titulo = "Gestión de Colaboraciones de Información sobre Especies"
    url = "especies"
    return render_to_response('mapas/colaboradores/lista.html', {'mesn':mesn,'estatus':estatus,'titulo':titulo,'url':url})
	
def listaColaboracionesActores(request,pagina,estatus):
    try:
        if estatus == '2':
           datos = Colaboradorespersonas.objects.filter(Q(estatu=2) | Q(estatu=3)).exclude(colectivos__isnull=True).order_by('colectivos__nombre','colectivos__nombre_completo')
        else:
           datos = Colaboradorespersonas.objects.filter(estatu=estatus).exclude(colectivos__isnull=True).order_by('colectivos__nombre','colectivos__nombre_completo')
    except Colaboradorespersonas.DoesNotExist:
        datos = None
    paginator = Paginator(datos, 30)
    page = pagina
    try:
        mesn = paginator.page(page)
    except PageNotAnInteger:
        mesn = paginator.page(1)
    titulo = "Gestión de Colaboraciones de Información sobre Actores"
    url = "actores"
    return render_to_response('mapas/colaboradores/lista.html', {'mesn':mesn,'estatus':estatus,'titulo':titulo,'url':url})
	
	
def listaColaboracionesAreas(request,pagina,estatus):
    try:
        if estatus == '2':
           datos = Colaboradorespersonas.objects.filter(Q(estatu=2) | Q(estatu=3)).exclude(areas__isnull=True).order_by('areas__nombre')
        else:
           datos = Colaboradorespersonas.objects.filter(estatu=estatus).exclude(areas__isnull=True).order_by('areas__nombre')
    except Colaboradorespersonas.DoesNotExist:
        datos = None
    paginator = Paginator(datos, 30)
    page = pagina
    try:
        mesn = paginator.page(page)
    except PageNotAnInteger:
        mesn = paginator.page(1)
    titulo = "Gestión de Colaboraciones de Información sobre Areas"
    url = "areas"
    return render_to_response('mapas/colaboradores/lista.html', {'mesn':mesn,'estatus':estatus,'titulo':titulo,'url':url})

def validarEstatusEspecie(request,id,estatus):
    try:
        datos = Taxon.objects.get(pk=id)
    except Taxon.DoesNotExist:
        datos = None
    if estatus == '0': 
       datos.estatu = 0
    if estatus == '1': 
       datos.estatu = 1
    if estatus == '2': 
       datos.estatu = 2
    if datos.save():
       return render_to_response('mapas/colaboradores/validar.html', {'datos':datos,'error':'No'})
    else:
       return render_to_response('mapas/colaboradores/validar.html', {'datos':datos,'error':'Si'})

def validarEstatusActores(request,id,estatus):
    try:
        datos = Actores.objects.get(pk=id)
    except Actores.DoesNotExist:
        datos = None
    if estatus == '0': 
       datos.estatu = 0
    if estatus == '1': 
       datos.estatu = 1
    if estatus == '2': 
       datos.estatu = 2
    if datos.save():
       return render_to_response('mapas/colaboradores/validar.html', {'datos':datos,'error':'No'})
    else:
       return render_to_response('mapas/colaboradores/validar.html', {'datos':datos,'error':'Si'})

def validarEstatusAreas(request,id,estatus):
    try:
        datos = Areas.objects.get(pk=id)
    except Areas.DoesNotExist:
        datos = None
    if estatus == '0': 
       datos.estatu = 0
    if estatus == '1': 
       datos.estatu = 1
    if estatus == '2': 
       datos.estatu = 2
    if datos.save():
       return render_to_response('mapas/colaboradores/validar.html', {'datos':datos,'error':'No'})
    else:
       return render_to_response('mapas/colaboradores/validar.html', {'datos':datos,'error':'Si'})

def validarColaboracion(request,id,estatus):
    try:
        datos = Colaboradorespersonas.objects.get(pk=id)
    except Colaboradorespersonas.DoesNotExist:
        datos = None
    if estatus == '0': 
       datos.estatu = 0
    if estatus == '1': 
       datos.estatu = 1
    if estatus == '2': 
       datos.estatu = 2
    if datos.save():
       return render_to_response('mapas/colaboradores/validar.html', {'datos':datos,'error':'No'})
    else:
       return render_to_response('mapas/colaboradores/validar.html', {'datos':datos,'error':'Si'})


def bancoVer(request,id):
    try:
        datos = Bancoaudiovisuals.objects.get(pk=id)
    except Bancoaudiovisuals.DoesNotExist:
        datos = None
    return render_to_response('actores/bancoaudio/bancover.html', {'datos':datos})
	

def incidencias(request,id):
    try:
        datos = Taxon.objects.get(pk=id)
    except Taxon.DoesNotExist:
        datos = None   
    if request.method == 'POST':
       incidencias = SistematizacionForm(request.POST)
       if incidencias.is_valid():
          incidencias.save()
          return render_to_response('mapas/colaboradores/incidencias.html',{'msm':'Exito','datos':datos})   
       else:
          incidencias = SistematizacionForm()
          return render_to_response('mapas/colaboradores/incidencias.html',{'form':incidencias,'msm':'Fallo','datos':datos}, context_instance=RequestContext(request))
    else:
       incidencias = SistematizacionForm()
    return render_to_response('mapas/colaboradores/incidencias.html',{'form':incidencias,'msm':'inicial','datos':datos}, context_instance=RequestContext(request))