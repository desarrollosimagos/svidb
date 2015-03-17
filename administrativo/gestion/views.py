# -*- coding: utf8
from gestion.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from plantillas.models import *
from menu.models import *
from mapas.models import *
from actores.models import *
from areas.models import *
from especies.models import *
from perfil.models import *
from congresos.models import *
from django.db.models import Q
	
def glosario(request,letra,id):
    try:
        principal = Secciones.objects.get(id=7)
    except Secciones.DoesNotExist:
        principal = None

    try:
        sub = Categorias.objects.get(id=31)
    except Categorias.DoesNotExist:
        sub = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=principal) & Q(subseccion=sub)) | (Q(seccion=principal) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None

    try:
        glosario = Glosario.objects.filter(nombre__startswith=letra).order_by('nombre')
    except Glosario.DoesNotExist:
        glosario = None

    if len(glosario) == 0:
       mesn=None
    else:
        paginator = Paginator(glosario, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)

    return render_to_response('gestion/glosario.html', {"mesn": mesn,"letra":letra,"principal":principal,"sub":sub,"lateral":lateral})
	
def buscar(request,letra,id):
    try:
        glosario = Glosario.objects.filter(nombre__icontains=letra).order_by('nombre')
    except Glosario.DoesNotExist:
        glosario = None

    if len(glosario) == 0:
       mesn=None
    else:
        paginator = Paginator(glosario, 10)
        page = id
        try:
           mesn = paginator.page(page)
        except PageNotAnInteger:
           # If page is not an integer, deliver first page.
           mesn = paginator.page(1)

    return render_to_response('gestion/buscar.html', {"mesn": mesn,"letra":letra})


def buscadorCompleto(request):
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
       taxon_id=request.GET.get( 'foreingkey_id', "" )
       textos=request.GET.get( 'valorForen', "" )
       modelo=request.GET.get( 'modelo', "" )
       num=len(textos)
       primero = 0
       datoinicio=""
       if textos <> "" :

          if modelo == 'Especies':
             if taxon_id <> "":
                taxon = Taxon.objects.get(pk=taxon_id)
                if taxon:
                   if primero==0:
                      primero = 1
                      datoinicio = "taxon"
             else:
                try:
                    if persona:
                       if id_usuario.is_staff:
                          taxon = Taxon.objects.filter((Q(nombre__icontains=textos) | Q(nombrecomun__icontains=textos) | Q(otrosnombrec__icontains=textos))).order_by('subtipo__posicion','nombre')
                       else:
                          taxon = Taxon.objects.filter((Q(nombre__icontains=textos) | Q(nombrecomun__icontains=textos) | Q(otrosnombrec__icontains=textos))).order_by('subtipo__posicion','nombre')
                    else:
                       taxon = Taxon.objects.filter((Q(nombre__icontains=textos) | Q(nombrecomun__icontains=textos) | Q(otrosnombrec__icontains=textos))).order_by('subtipo__posicion','nombre')
					   
                    if taxon:
                       if primero==0:
                          primero = 1
                          datoinicio = "taxon"
                except Taxon.DoesNotExist:
                    taxon = None
          else:
             try:
                 if persona:
                    if id_usuario.is_staff:
                       taxon = Taxon.objects.filter(Q(taxonrelax__nombre__icontains=textos) | Q(nombre__icontains=textos) | Q(nombrecomun__icontains=textos) | Q(otrosnombrec__icontains=textos)).order_by('subtipo','nombre')
                    else:
                       taxon = Taxon.objects.filter(Q(taxonrelax__nombre__icontains=textos) | Q(nombre__icontains=textos) | Q(nombrecomun__icontains=textos) | Q(otrosnombrec__icontains=textos)).order_by('subtipo','nombre')
                 else: 
                    taxon = Taxon.objects.filter(Q(taxonrelax__nombre__icontains=textos) | Q(nombre__icontains=textos) | Q(nombrecomun__icontains=textos) | Q(otrosnombrec__icontains=textos)).order_by('subtipo','nombre')
                 if taxon:
                    if primero==0:
                       primero = 1
                       datoinicio = "taxon"
             except Taxon.DoesNotExist:
                 taxon = None

          try:
              if persona:
                 if id_usuario.is_staff:
                    areas = Areas.objects.filter(Q(nombre__icontains=textos) | Q(categoriact__titulo__icontains=textos)).order_by('nombre')
                 else:
                    areas = Areas.objects.filter((Q(nombre__icontains=textos) | Q(categoriact__titulo__icontains=textos)) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')
              else:
                 areas = Areas.objects.filter((Q(nombre__icontains=textos) | Q(categoriact__titulo__icontains=textos)) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')
              if areas:
                 if primero==0:
                    primero = 1
                    datoinicio = "areas"
          except Areas.DoesNotExist:
              areas = None
			  
          try:
              if persona:
                 if id_usuario.is_staff:
                    actor = Actores.objects.filter(Q(nombre_completo__icontains=textos)).order_by('nombre')
                 else:
                    actor = Actores.objects.filter(Q(nombre_completo__icontains=textos) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')
              else:
                  actor = Actores.objects.filter(Q(nombre_completo__icontains=textos) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).order_by('nombre')
              
              if actor:
                 if primero==0:
                    primero = 1
                    datoinicio = "actor"
          except Actores.DoesNotExist:
              actor = None

          try:
              biblioteca = Bibliotecas.objects.filter(Q(titulo__icontains=textos) | Q(autores__icontains=textos))
              if biblioteca:
                 if primero==0:
                    primero = 1
                    datoinicio = "biblioteca"
          except Bibliotecas.DoesNotExist:
              biblioteca = None

          try:
              glosario = Glosario.objects.filter(nombre__icontains=textos)
              if glosario:
                 if primero==0:
                    primero = 1
                    datoinicio = "glosario"
          except Glosario.DoesNotExist:
              glosario = None
	  
          try:
              mapas = Mapas.objects.filter(nombre__icontains=textos)
              if mapas:
                 if primero==0:
                    primero = 1
                    datoinicio = "mapas"
          except Mapas.DoesNotExist:
              mapas = None
			  
          try:
              eventos = Eventos.objects.filter(nombre__icontains=textos)
              if eventos:
                 if primero==0:
                    primero = 1
                    datoinicio = "eventos"
          except Eventos.DoesNotExist:
              eventos = None
			  
          try:
              biorregion = Bioregions.objects.filter(nombre__icontains=textos)
              if biorregion:
                 if primero==0:
                    primero = 1
                    datoinicio = "biorregion"
          except Bioregions.DoesNotExist:
              biorregion = None
			  
          try:
              banco = Bancoaudiovisuals.objects.filter(Q(descripcion__icontains=textos) | Q(lugar__icontains=textos))
              if banco:
                 if primero==0:
                    primero = 1
                    datoinicio = "banco"
          except Bancoaudiovisuals.DoesNotExist:
              banco = None
			  
          try:
              etnias = Etnias.objects.filter(Q(nombre__icontains=textos) | Q(otrosnombre__icontains=textos))
              if etnias:
                 if primero==0:
                    primero = 1
                    datoinicio = "etnias"
          except Etnias.DoesNotExist:
              etnias = None
			  
          try:
              Categoria = Categorias.objects.filter(titulo__icontains=textos)
              if Categoria:
                 if primero==0:
                    primero = 1
                    datoinicio = "plataforma"
          except Categorias.DoesNotExist:
              Categoria = None

          try:
              subCategoria = SubTipoCategorias.objects.filter(nombre__icontains=textos)
              if subCategoria:
                 if primero==0:
                    primero = 1
                    datoinicio = "plataforma"
          except SubTipoCategorias.DoesNotExist:
              subCategoria = None

          return render_to_response('gestion/buscador.html', {'textos':textos,'taxon':taxon,'taxon_id':taxon_id,'subCategoria':subCategoria,'Categoria':Categoria,'etnias':etnias,'banco':banco,'biorregion':biorregion,'eventos':eventos,'mapas':mapas,'actor':actor,'areas':areas,'glosario':glosario,'biblioteca':biblioteca,'modelo':modelo,'datoinicio':datoinicio,'persona':persona})   			
       else:
          return render_to_response('gestion/buscador.html', {"resultados":"No"})
    else:
         return render_to_response('gestion/buscador.html', {"resultados":"No"})
    

def buscadorCompleto2(request):
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
       taxon_id=request.GET.get( 'foreingkey_id', "" )
       textos=request.GET.get( 'valorForen', "" )
       modelo=request.GET.get( 'modelo', "" )
       num=len(textos)
       if textos <> "" :
           biblioteca = None
           if modelo == 'biblioteca':
              try:
                  biblioteca = Bibliotecas.objects.filter(Q(titulo__icontains=textos) | Q(autores__icontains=textos))
              except Bibliotecas.DoesNotExist:
                  biblioteca = None
              return render_to_response('gestion/buscador2.html', {"biblioteca":biblioteca}) 

           glosario = None
           if modelo == 'glosario':
              try:
                  glosario = Glosario.objects.filter(nombre__icontains=textos)
              except Glosario.DoesNotExist:
                  glosario = None
              return render_to_response('gestion/buscador2.html', {"glosario":glosario}) 
			  
           areas = None
           if modelo == 'areas':
              try:
                  if persona:
                     if id_usuario.is_staff:
                        areas = Areas.objects.filter(Q(nombre__icontains=textos) | Q(categoriact__titulo__icontains=textos))					 
                     else:
                        areas = Areas.objects.filter((Q(nombre__icontains=textos) | Q(categoriact__titulo__icontains=textos)) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9))
                  else:
                     areas = Areas.objects.filter((Q(nombre__icontains=textos) | Q(categoriact__titulo__icontains=textos)) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9))
              except Areas.DoesNotExist:
                  areas = None
              return render_to_response('gestion/buscador2.html', {"areas":areas}) 
			  
           taxon = None
           if modelo == 'especie':
              if taxon_id <> "":
                 taxon = Taxon.objects.get(pk=taxon_id)
                 
              else:
                 try:
                     if persona:
                        if id_usuario.is_staff:
                           taxon = Taxon.objects.filter(Q(taxonrelax__nombre__icontains=textos) | Q(nombre__icontains=textos) | Q(nombrecomun__icontains=textos) | Q(otrosnombrec__icontains=textos)).order_by('subtipo','nombre')
                        else:
                           taxon = Taxon.objects.filter(Q(taxonrelax__nombre__icontains=textos) | Q(nombre__icontains=textos) | Q(nombrecomun__icontains=textos) | Q(otrosnombrec__icontains=textos)).order_by('subtipo','nombre')
                     else:
                        taxon = Taxon.objects.filter(Q(taxonrelax__nombre__icontains=textos) | Q(nombre__icontains=textos) | Q(nombrecomun__icontains=textos) | Q(otrosnombrec__icontains=textos)).order_by('subtipo','nombre')
                 except Taxon.DoesNotExist:
                     taxon = None
              return render_to_response('gestion/buscador2.html', {"taxon":taxon,"taxon_id":taxon_id}) 
			  
			  
           actor = None
           if modelo == 'actores':
              try:
                  if persona:
                     if id_usuario.is_staff:
                        actor = Actores.objects.filter(Q(nombre_completo__icontains=textos))					 
                     else:
                        actor = Actores.objects.filter(Q(nombre_completo__icontains=textos) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9))
                  else:
                     actor = Actores.objects.filter(Q(nombre_completo__icontains=textos) & Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9))
              except Actores.DoesNotExist:
                  actor = None
              return render_to_response('gestion/buscador2.html', {"actor":actor}) 
			  
           mapas = None
           if modelo == 'mapas':
              try:
                  mapas = Mapas.objects.filter(nombre__icontains=textos)
              except Mapas.DoesNotExist:
                  mapas = None
              return render_to_response('gestion/buscador2.html', {"mapas":mapas}) 
			  
           eventos = None
           if modelo == 'eventos':
              try:
                  eventos = Eventos.objects.filter(nombre__icontains=textos)
              except Eventos.DoesNotExist:
                  eventos = None
              return render_to_response('gestion/buscador2.html', {"eventos":eventos}) 
			  
           biorregion = None
           if modelo == 'biorregion':
              try:
                  biorregion = Bioregions.objects.filter(nombre__icontains=textos)
              except Bioregions.DoesNotExist:
                  biorregion = None
              return render_to_response('gestion/buscador2.html', {"biorregion":biorregion}) 
			  
           banco = None
           if modelo == 'banco':
              try:
                  banco = Bancoaudiovisuals.objects.filter(Q(descripcion__icontains=textos) | Q(lugar__icontains=textos))
              except Bancoaudiovisuals.DoesNotExist:
                  banco = None
              return render_to_response('gestion/buscador2.html', {"banco":banco}) 
			  
           etnias = None
           if modelo == 'etnias':
              try:
                  etnias = Etnias.objects.filter(Q(nombre__icontains=textos) | Q(otrosnombre__icontains=textos))
              except Etnias.DoesNotExist:
                  etnias = None
              return render_to_response('gestion/buscador2.html', {"etnias":etnias}) 
			  
           Categoria = None
           subCategoria = None
           if modelo == 'plataforma':
              try:
                  Categoria = Categorias.objects.filter(titulo__icontains=textos)
              except Categorias.DoesNotExist:
                  Categoria = None
              try:
                  subCategoria = SubTipoCategorias.objects.filter(nombre__icontains=textos)
              except SubTipoCategorias.DoesNotExist:
                  subCategoria = None
              return render_to_response('gestion/buscador2.html', {"Categoria":Categoria,"subCategoria":subCategoria}) 
       else:
          return render_to_response('gestion/buscador2.html')
    else:
       return render_to_response('gestion/buscador2.html')



