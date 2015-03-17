# -*- coding: utf8
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404,HttpResponse
from django.template import RequestContext, loader
from actores.models import *
from areas.models import *
from perfil.models import *
from menu.models import *
from listasTematicas.models import *
from especies.models import *
from plantillas.models import *
from django.db.models import *
from django.utils import simplejson

def secActores(request):
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
        principal = Secciones.objects.get(id=5)
    except Secciones.DoesNotExist:
        principal = None

    try:
        actores = SubTipoCategorias.objects.filter(categoria__seccione=principal).order_by('categoria')
    except SubTipoCategorias.DoesNotExist:
        actores = None

    try:
        lateral = TemplatesInfoLateral.objects.filter(Q(seccion=principal) & Q(activar=True)).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    return render_to_response('menu/actores.html', {"principal": principal,'actores':actores,'lateral':lateral,'persona':persona})
	
	
def detActores(request,id):
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
        seccion = Secciones.objects.get(id=5)
    except Secciones.DoesNotExist:
        seccion = None
		
    try:
        principal = Categorias.objects.get(id=id)
    except Categorias.DoesNotExist:
        principal = None

    try:
        areas = SubTipoCategorias.objects.filter(categoria=principal).order_by('nombre')
    except SubTipoCategorias.DoesNotExist:
        areas = None

    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=seccion) & Q(subseccion=principal)) | (Q(seccion=seccion) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
    return render_to_response('menu/det_actores.html', {'principal':principal,'areas':areas,'lateral':lateral,'seccion':seccion,'persona':persona})
	
def listaComplementoActores(request,limite,load,prin):
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
    a = 100
    b = int(limite)
    a += b
    c = int(load)
    c += 1

    if persona:
       if id_usuario.is_staff:
          try:
              areas = Actores.objects.filter(tipocolec=principal).order_by('nombre')[limite:a]
          except Actores.DoesNotExist:
              areas = None        
       else:
          try:
              areas = Actores.objects.filter(Q(tipocolec=principal) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')[limite:a]
          except Actores.DoesNotExist:
              areas = None
    else:
       try:
           areas =Actores.objects.filter(Q(tipocolec=principal) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')[limite:a]
       except Actores.DoesNotExist:
           areas = None
    return render_to_response('menu/listas_complemento_actores.html', {'areas':areas,'persona':persona,'usuario':id_usuario,'load':c})	
	
	
def listaActores(request,id):
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
        seccion = Secciones.objects.get(id=5)
    except Secciones.DoesNotExist:
        seccion = None

    try:
        principal = SubTipoCategorias.objects.get(id=id)
    except SubTipoCategorias.DoesNotExist:
        principal = None

	
    if persona:
       if id_usuario.is_staff:
          try:
              areas = Actores.objects.filter(tipocolec=principal).order_by('nombre')[:100]
          except Actores.DoesNotExist:
              areas = None        
       else:
          try:
              areas = Actores.objects.filter(Q(tipocolec=principal) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')[:100]
          except Actores.DoesNotExist:
              areas = None
    else:
       try:
           areas =Actores.objects.filter(Q(tipocolec=principal) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')[:100]
       except Actores.DoesNotExist:
           areas = None

    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=seccion) & Q(subseccion=principal.categoria.id)) | (Q(seccion=seccion) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    return render_to_response('menu/lista_actores.html', {'principal':principal,'areas':areas,'seccion':seccion,'lateral':lateral,'persona':persona,'usuario':id_usuario,'url':'/actores/complemento/'})
	
	
def secAreas(request):
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
        principal = Secciones.objects.get(id=4)
    except Secciones.DoesNotExist:
        principal = None
		
    try:
        areas = SubTipoCategorias.objects.filter(categoria__seccione=principal).order_by('categoria')
    except SubTipoCategorias.DoesNotExist:
        areas = None

    try:
        lateral = TemplatesInfoLateral.objects.filter(Q(seccion=principal) & Q(activar=True)).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    return render_to_response('menu/areas.html', {"principal": principal,'areas':areas,'lateral':lateral,'persona':persona})
	
def detAreas(request,id):
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
        seccion = Secciones.objects.get(id=4)
    except Secciones.DoesNotExist:
        seccion = None
		
    try:
        principal = Categorias.objects.get(id=id)
    except Categorias.DoesNotExist:
        principal = None

    try:
        areas = SubTipoCategorias.objects.filter(categoria=principal).order_by('nombre')
    except SubTipoCategorias.DoesNotExist:
        areas = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=seccion) & Q(subseccion=principal)) | (Q(seccion=seccion) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    return render_to_response('menu/det_categoria.html', {'principal':principal,'areas':areas,'lateral':lateral,'seccion':seccion,'persona':persona})
	
	
def listaComplementoAreas(request,limite,load,prin):
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
    a = 100
    b = int(limite)
    a += b
    c = int(load)
    c += 1
    if persona:
       if id_usuario.is_staff:
          try:
              areas = Areas.objects.filter(subtipoas=principal).order_by('nombre')[limite:a]
          except Taxon.DoesNotExist:
              areas = None        
       else:
          try:
              areas = Areas.objects.filter(Q(subtipoas=principal) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')[limite:a]
          except Areas.DoesNotExist:
              areas = None
    else:
       try:
           areas = Areas.objects.filter(Q(subtipoas=principal) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')[limite:a]
       except Areas.DoesNotExist:
           areas = None
    return render_to_response('menu/listas_complemento_areas.html', {'areas':areas,'persona':persona,'usuario':id_usuario,'load':c})
	
def listaAreas(request,id):
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
        seccion = Secciones.objects.get(id=4)
    except Secciones.DoesNotExist:
        seccion = None
		
    try:
        principal = SubTipoCategorias.objects.get(id=id)
    except SubTipoCategorias.DoesNotExist:
        principal = None

    if persona:
       if id_usuario.is_staff:
          try:
              areas = Areas.objects.filter(subtipoas=principal).order_by('nombre')[:100]
          except Taxon.DoesNotExist:
              areas = None        
       else:
          try:
              areas = Areas.objects.filter(Q(subtipoas=principal) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')[:100]
          except Areas.DoesNotExist:
              areas = None
    else:
       try:
           areas = Areas.objects.filter(Q(subtipoas=principal) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')[:100]
       except Areas.DoesNotExist:
           areas = None

    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=seccion) & Q(subseccion=principal.categoria.id)) | (Q(seccion=seccion) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    return render_to_response('menu/lista_areas.html', {'principal':principal,'areas':areas,'lateral':lateral,'seccion':seccion,'persona':persona,'usuario':id_usuario,'url':'/areas/complemento/'})



def secTaxon(request):
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
        principal = Secciones.objects.get(id=6)
    except Secciones.DoesNotExist:
        principal = None

    try:
        categoria = Categorias.objects.filter(Q(seccione=principal) & Q(estatu=0)).order_by('posicion','titulo')
    except Categorias.DoesNotExist:
        categoria = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter(Q(seccion=principal) & Q(activar=True)).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None

    return render_to_response('menu/especies.html', {"principal": principal,'categoria':categoria,'lateral':lateral,'persona':persona})


def listaexoticaComplemento(request,limite,load,prin):
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
    a = 100
    b = int(limite)
    a += b
    c = int(load)
    c += 1
    if persona:
       if id_usuario.is_staff:
          taxon_colaboracion = []
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espexot=True)).order_by('nombrecomun')[limite:a]
          except Taxon.DoesNotExist:
              taxon = None        
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espexot=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__espexot=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_complemento.html', {'taxon':taxon,'persona':persona,'usuario':id_usuario,'load':c,'principal':prin})
	
	
def listaexoticaComplementoFiltro(request):
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
    if persona:
       if id_usuario.is_staff:
          taxon_colaboracion = []
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espexot=True)).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None        
       else:
          taxon = None
    else:
       taxon = None
	   
    return render_to_response('menu/listas_complemento.html', {'taxon':taxon,'persona':persona,'usuario':id_usuario,'load':c,'principal':prin})

def listaexoticas(request,id):
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
        principal = Categorias.objects.get(id=id)
    except SubTipoCategorias.DoesNotExist:
        principal = None
		
    if persona:
       if id_usuario.is_staff:
          taxon_colaboracion = []
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espexot=True)).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None        
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espexot=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__espexot=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
       except Taxon.DoesNotExist:
           taxon = None
    
    return render_to_response('menu/listas_exoticas.html', {'principal':principal,'taxon':taxon,'persona':persona,'usuario':id_usuario,'url':'/exoticas/complemento/'})
	

def listatraficosComplemento(request,limite,load,prin):
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
    a = 100
    b = int(limite)
    a += b
    c = int(load)
    c += 1
    if persona:
       if id_usuario.is_staff:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__esptraf=True)).order_by('nombrecomun')[limite:a]
          except Taxon.DoesNotExist:
              taxon = None        
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__esptraf=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__esptraf=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_complemento.html', {'taxon':taxon,'persona':persona,'usuario':id_usuario,'load':c,'principal':prin})

	
def listatraficos(request,id):
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
        principal = Categorias.objects.get(id=id)
    except SubTipoCategorias.DoesNotExist:
        principal = None

    if persona:
       if id_usuario.is_staff:
          try:
              taxon = Taxon.objects.filter(detalletaxon__esptraf=True).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None       
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__esptraf=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__esptraf=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_exoticas.html', {'principal':principal,'taxon':taxon,'persona':persona,'usuario':id_usuario,'url':'/comercio/complemento/'})


def listapeligroextComplemento(request,limite,load,prin):
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
    a = 100
    b = int(limite)
    a += b
    c = int(load)
    c += 1
    if persona:
       if id_usuario.is_staff:
          taxon_colaboracion = []
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__esppeligr=True)).order_by('nombrecomun')[limite:a]
          except Taxon.DoesNotExist:
              taxon = None        
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__esppeligr=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__esppeligr=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_complemento.html', {'taxon':taxon,'persona':persona,'usuario':id_usuario,'load':c,'principal':prin})
	
	
def listapeligroext(request,id):
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
        principal = Categorias.objects.get(id=id)
    except SubTipoCategorias.DoesNotExist:
        principal = None

    if persona:
       if id_usuario.is_staff:
          try:
              taxon = Taxon.objects.filter(detalletaxon__esppeligr=True).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None       
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__esppeligr=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__esppeligr=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_exoticas.html', {'principal':principal,'taxon':taxon,'persona':persona,'usuario':id_usuario,'url':'/extincion/complemento/'})
	

def listaagricolasComplemento(request,limite,load,prin):
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
    a = 100
    b = int(limite)
    a += b
    c = int(load)
    c += 1
    if persona:
       if id_usuario.is_staff:
          taxon_colaboracion = []
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espagrico=True)).order_by('nombrecomun')[limite:a]
          except Taxon.DoesNotExist:
              taxon = None        
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espagrico=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__espagrico=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_complemento.html', {'taxon':taxon,'persona':persona,'usuario':id_usuario,'load':c,'principal':prin})

	
def listaagricolas(request,id):
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
        principal = Categorias.objects.get(id=id)
    except SubTipoCategorias.DoesNotExist:
        principal = None

    if persona:
       if id_usuario.is_staff:
          try:
              taxon = Taxon.objects.filter(detalletaxon__espagrico=True).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None       
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espagrico=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__espagrico=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_exoticas.html', {'principal':principal,'taxon':taxon,'persona':persona,'usuario':id_usuario,'url':'/agropecuaria/complemento/'})
	

def listasaludComplemento(request,limite,load,prin):
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
    a = 100
    b = int(limite)
    a += b
    c = int(load)
    c += 1
    if persona:
       if id_usuario.is_staff:
          taxon_colaboracion = []
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espsalud=True)).order_by('nombrecomun')[limite:a]
          except Taxon.DoesNotExist:
              taxon = None        
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espsalud=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__espsalud=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_complemento.html', {'taxon':taxon,'persona':persona,'usuario':id_usuario,'load':c,'principal':prin})

	
def listasalud(request,id):
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
        principal = Categorias.objects.get(id=id)
    except SubTipoCategorias.DoesNotExist:
        principal = None

    if persona:
       if id_usuario.is_staff:
          try:
              taxon = Taxon.objects.filter(detalletaxon__espsalud=True).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None       
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espsalud=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__espsalud=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_exoticas.html', {'principal':principal,'taxon':taxon,'persona':persona,'usuario':id_usuario,'url':'/salud/complemento/'})


def listasustentableComplemento(request,limite,load,prin):
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
    a = 100
    b = int(limite)
    a += b
    c = int(load)
    c += 1
    if persona:
       if id_usuario.is_staff:
          taxon_colaboracion = []
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espaprove=True)).order_by('nombrecomun')[limite:a]
          except Taxon.DoesNotExist:
              taxon = None        
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espaprove=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__espaprove=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')
       except Taxon.DoesNotExist:
           taxon = None
    return render_to_response('menu/listas_complemento.html', {'taxon':taxon,'persona':persona,'usuario':id_usuario,'load':c,'principal':prin})


	
def listasustentable(request,id):
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
        principal = Categorias.objects.get(id=id)
    except SubTipoCategorias.DoesNotExist:
        principal = None

    if persona:
       if id_usuario.is_staff:
          try:
              taxon = Taxon.objects.filter(detalletaxon__espaprove=True).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None       
       else:
          try:
              taxon = Taxon.objects.filter(Q(detalletaxon__espaprove=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
          except Taxon.DoesNotExist:
              taxon = None
    else:
       try:
           taxon = Taxon.objects.filter(Q(detalletaxon__espaprove=True) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombrecomun')[:100]
       except Taxon.DoesNotExist:
           taxon = None

    return render_to_response('menu/listas_exoticas.html', {'principal':principal,'taxon':taxon,'persona':persona,'usuario':id_usuario,'url':'/sustentables/complemento/'})
	
	
#-----------------------------------------------------------------------------------------------
def laPlataforma(request):
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
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=25)
    except Categorias.DoesNotExist:
        sub = None

    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        estatica = Templates.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except Templates.DoesNotExist:
        estatica = None
   


    return render_to_response('menu/index2.html', {"principal": principal,'lateral':lateral,'estatica':estatica,'persona':persona})
	
	
#-----------------------------------------------------------------------------------------------
def elSistema(request):
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
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=26)
    except Categorias.DoesNotExist:
        sub = None

#    try:
#        lateral_prin = TemplatesInfoLateral.objects.filter(Q(seccion=principal) & Q(activar=True)).order_by('posicion')
#    except TemplatesInfoLateral.DoesNotExist:
#        lateral_prin = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        estatica = Templates.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except Templates.DoesNotExist:
        estatica = None

    return render_to_response('menu/plataforma.html', {"principal": principal,'sub':sub,'lateral':lateral,'estatica':estatica,'persona':persona})
	
#-----------------------------------------------------------------------------------------------
def ConstruccionColectiva(request):
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
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=28)
    except Categorias.DoesNotExist:
        sub = None

#    try:
#        lateral_prin = TemplatesInfoLateral.objects.filter(Q(seccion=principal) & Q(activar=True)).order_by('posicion')
#    except TemplatesInfoLateral.DoesNotExist:
#        lateral_prin = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        estatica = Templates.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except Templates.DoesNotExist:
        estatica = None

    return render_to_response('menu/plataforma.html', {"principal": principal,'sub':sub,'lateral':lateral,'estatica':estatica,'persona':persona})
	
	
#-----------------------------------------------------------------------------------------------
def LaEstrategia(request):
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
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=29)
    except Categorias.DoesNotExist:
        sub = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        estatica = Templates.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except Templates.DoesNotExist:
        estatica = None

    return render_to_response('menu/plataforma.html', {"principal": principal,'sub':sub,'lateral':lateral,'estatica':estatica,'persona':persona})
	
	
#-----------------------------------------------------------------------------------------------
def OMG(request):
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
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=32)
    except Categorias.DoesNotExist:
        sub = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        estatica = Templates.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except Templates.DoesNotExist:
        estatica = None

    return render_to_response('menu/plataforma.html', {"principal": principal,'sub':sub,'lateral':lateral,'estatica':estatica,'persona':persona})
	

#-----------------------------------------------------------------------------------------------
def RECOB(request):
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
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=33)
    except Categorias.DoesNotExist:
        sub = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        estatica = Templates.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except Templates.DoesNotExist:
        estatica = None

    return render_to_response('menu/plataforma.html', {"principal": principal,'sub':sub,'lateral':lateral,'estatica':estatica,'persona':persona})
	
#-----------------------------------------------------------------------------------------------
def MSIIDB(request):
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
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=34)
    except Categorias.DoesNotExist:
        sub = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        estatica = Templates.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except Templates.DoesNotExist:
        estatica = None

    return render_to_response('menu/plataforma.html', {"principal": principal,'sub':sub,'lateral':lateral,'estatica':estatica,'persona':persona})
	

def FUNZA(request):
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
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=36)
    except Categorias.DoesNotExist:
        sub = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        estatica = Templates.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except Templates.DoesNotExist:
        estatica = None

    return render_to_response('menu/plataforma.html', {"principal": principal,'sub':sub,'lateral':lateral,'estatica':estatica,'persona':persona})
	
	
def Licencias(request):
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
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=37)
    except Categorias.DoesNotExist:
        sub = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        estatica = Templates.objects.filter(Q(seccion=principal) & Q(subseccion=sub)).order_by('posicion')
    except Templates.DoesNotExist:
        estatica = None

    return render_to_response('menu/plataforma.html', {"principal": principal,'sub':sub,'lateral':lateral,'estatica':estatica,'persona':persona})


def PaginadorGaleria2(request,pagina,id):
    try:
        dat = Mapas.objects.get(pk=id)
    except Mapas.DoesNotExist:
        dat = None

    try:
        datos = Mapas.objects.filter()
    except Mapas.DoesNotExist:
        datos = None

#    image_list = datos.all()
		   
    paginator = Paginator(datos, 63)
    page = pagina
    try:
        mesn = paginator.page(page)
    except PageNotAnInteger:
        mesn = paginator.page(1)
    return render_to_response('menu/mapas/paginadorGaleria2.html', {'mesn':mesn,'dat':dat})

def bancoVer(request,id):
    try:
        datos = Mapas.objects.get(pk=id)
    except Mapas.DoesNotExist:
        datos = None
    return render_to_response('menu/mapas/bancover.html', {'datos':datos})


def elimina_tildes(self, cadena):
    # http://guimi.net
    # Cambiamos caracteres modificados (áüç...) por los caracteres base (auc...)
    # Basado en una función de Miguel en
    # http://www.leccionespracticas.com/uncategorized/eliminar-tildes-con-python-solucionado/
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s.decode()

def ajax(request):
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
		
    if request.method == 'GET':
       x = request.GET['term']
       #s = ''.join((c for c in unicodedata.normalize('NFD',unicode(x)) if unicodedata.category(c) != 'Mn'))
       #xnotilde = s.decode()
#       try:
#           datos = Taxon.objects.filter(Q(nombre__icontains=x) | Q(nombrecomun__icontains=x)).order_by('subtipo','nombre')[:10]
#       except Taxon.DoesNotExist:
#           datos = None 
		   
       if persona:
          if id_usuario.is_staff:
             try:
                 datos = Taxon.objects.filter(Q(taxonrelax__nombre__icontains=x) | Q(nombre__icontains=x) | Q(nombrecomun__icontains=x)).order_by('subtipo','nombre')[:10]
             except Taxon.DoesNotExist:
                 datos = None    

             try:
                 datosareas = Areas.objects.filter(Q(nombre__icontains=x))[:10]
             except Areas.DoesNotExist:
                 datosareas = None   
				 
             try:
                 datosactores = Actores.objects.filter(Q(nombre_completo__icontains=x))[:10]
             except Actores.DoesNotExist:
                 datosactores = None  
				  
          else:
             try:
                 datos = Taxon.objects.filter((Q(taxonrelax__nombre__icontains=x) | Q(nombre__icontains=x) | Q(nombrecomun__icontains=x)) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('subtipo','nombre')[:10]
             except Taxon.DoesNotExist:
                 datos = None

             try:
                 datosareas = Areas.objects.filter(Q(nombre__icontains=x) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9))[:10]
             except Areas.DoesNotExist:
                 datosareas = None   
				 
             try:
                 datosactores = Actores.objects.filter(Q(nombre_completo__icontains=x) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9))[:10]
             except Actores.DoesNotExist:
                 datosactores = None  
       else:
          try:
              datos = Taxon.objects.filter((Q(taxonrelax__nombre__icontains=x) | Q(nombre__icontains=x) | Q(nombrecomun__icontains=x)) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('subtipo','nombre')[:10]
          except Taxon.DoesNotExist:
              datos = None
			  
          try:
              datosareas = Areas.objects.filter(Q(nombre__icontains=x) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9))[:10]
          except Areas.DoesNotExist:
              datosareas = None   
          try:
              datosactores = Actores.objects.filter(Q(nombre_completo__icontains=x) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9))[:10]
          except Actores.DoesNotExist:
              datosactores = None  
			  
       taxon_list=[]
       for list in datos:
           if list.nombrecomun :
              nocu =list.nombrecomun
           else:
              nocu = ''

           if list.nombre :
              no =list.nombre
           else:
              no = ''

           if list.taxonrelax :
              if list.taxonrelax.nombre :
                 tax =list.taxonrelax.nombre
              else:
                 tax = ''
              if list.taxonrelax.taxonrelax :
                 if list.taxonrelax.taxonrelax.nombre :
                    taxtax =list.taxonrelax.taxonrelax.nombre
                 else:
                    taxtax = ''
              else:
                 taxtax = ''
           else:
              tax = ''
              taxtax = ''
			  



           list_info = {}
           if list.subtipo.id >= 26 :
              if list.subtipo.id == 26:
                 list_info['label'] = nocu + ' (<em>' + tax + '  ' +  no + '</em>)'
                 list_info['labelcmp'] = nocu + ' (' + tax + '  ' +  no + ')'
              if list.subtipo.id > 26:
                 list_info['label'] = nocu + ' (<em>' + taxtax + '  ' +  tax +' '  + no + '</em>)'
                 list_info['labelcmp'] = nocu + ' (' + taxtax + '  ' +  tax +' '  +  no + ')'
           else:
              list_info['label'] = ' (<em>' +  no + '</em>)'
              list_info['labelcmp'] = ' (' +  no + ')'
           
           list_info['category'] = list.subtipo.nombre
           list_info['aut_model'] = 'Especies'
           list_info['id'] = list.id
           list_info['hiddenName'] = 'foreingkey'
           taxon_list.append(list_info)

       for list in datosareas:
           list_info = {}
           list_info['label'] = list.nombre
           list_info['labelcmp'] = list.nombre
           list_info['aut_model'] = 'Areas'
           
           list_info['category'] = 'Areas'
           list_info['id'] = list.id
           list_info['hiddenName'] = 'foreingkey'
           taxon_list.append(list_info)
		   
       for list in datosactores:
           list_info = {}
           list_info['label'] = list.nombre_completo
           list_info['labelcmp'] = list.nombre_completo
           list_info['aut_model'] = 'Actores'
           
           list_info['category'] = 'Actores'
           list_info['id'] = list.id
           list_info['hiddenName'] = 'foreingkey'
           taxon_list.append(list_info)
       return HttpResponse(simplejson.dumps(taxon_list), mimetype='application/javascript')
    else:
       return render_to_response('ajaxexample.html', context_instance=RequestContext(request))

