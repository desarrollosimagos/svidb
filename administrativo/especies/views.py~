# -*- coding: utf8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from perfil.models import PerfilPublico,ModulosPublicos,PerfilModulos
from django.contrib.auth.models import User
from datetime import *
from listasTematicas.models import *
from inicio.models import *
from mapas.models import *
from plantillas.models import *
from menu.models import *
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from especies.models import *
from django.utils import simplejson
#from django.db.models import Count,Max
from django.db.models import *
from django.db.models import Q


def vertaxon(request,id):
    try:
       taxon = Taxon.objects.get(pk= id)
    except Taxon.DoesNotExist:
       taxon = None
    return render_to_response("especies/ver_mini_taxon.html",{'taxon':taxon}, context_instance=RequestContext(request))
	
def ficha(request,id):
    try:
       taxon = Taxon.objects.get(pk= id)
    except Taxon.DoesNotExist:
       taxon = None
    return render_to_response("especies/taxon.html",{'taxon':taxon}, context_instance=RequestContext(request))

def listasEscalera(request):
    try:
       escalera = TipoTaxon.objects.filter(estatu__nombre="Activo")
    except Taxon.DoesNotExist:
       imperio = None
    return render_to_response("especies/escalera.html",{'escalera':imperio}, context_instance=RequestContext(request))


def listas(request):
    try:
       imperio = Taxon.objects.filter(subtipo__nombre="Imperio")
       lista2 = Taxon.objects.filter(subtipo__nombre="Imperio").count()
       lista3 = Taxon.objects.filter(subtipo__nombre="Imperio").aggregate(Max('id'))
    except Taxon.DoesNotExist:
       imperio = None
    return render_to_response("especies/listas.html",{'imperio':imperio,'lista2':lista2,'lista3':lista3}, context_instance=RequestContext(request))
	
def list(request,id):
    lista4 = None
    lista5 = None
    try:
       taxon = Taxon.objects.get(pk= id)
    except Taxon.DoesNotExist:
       taxon = None
	
    try:
       list = Taxon.objects.filter(taxonrelax=taxon)
       lista2 = Taxon.objects.filter(taxonrelax=taxon).count()
       lista3 = Taxon.objects.filter(taxonrelax=taxon).aggregate(Max('id'))
       #lista4 = Taxon.objects.filter(taxonrelax=list)
       #lista5 = Taxon.objects.filter(taxonrelax=list).aggregate(Max('id'))
    except Taxon.DoesNotExist:
       list = None
    return render_to_response("especies/list.html",{'list':list,'lista2':lista2,'lista3':lista3,'lista4':lista4,'lista5':lista5}, context_instance=RequestContext(request))


def reino(request,id):
    try:
       taxon = Taxon.objects.get(pk= id)
    except Taxon.DoesNotExist:
       taxon = None

    try:
       sub_reino = Taxon.objects.filter(taxonrelax=taxon).exclude(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Reino")
    except Taxon.DoesNotExist:
       sub_reino = None

    try:
       phylum = Taxon.objects.filter(taxonrelax=taxon).filter(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Phylum")
    except Taxon.DoesNotExist:
       phylum = None
	   
    return render_to_response("especies/reino.html",{'sub_reino':sub_reino,'phylum':phylum}, context_instance=RequestContext(request))
	
	
def phylum(request,id):
    try:
       taxon = Taxon.objects.get(pk= id)
    except Taxon.DoesNotExist:
       taxon = None

    try:
       sub_phylum = Taxon.objects.filter(taxonrelax=taxon).exclude(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Phylum")
    except Taxon.DoesNotExist:
       sub_phylum = None

    try:
       clase = Taxon.objects.filter(taxonrelax=taxon).filter(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Clase")
    except Taxon.DoesNotExist:
       clase = None
	   
    return render_to_response("especies/phylum.html",{'sub_phylum':sub_phylum,'clase':clase}, context_instance=RequestContext(request))

	
def clase(request,id):
    try:
       taxon = Taxon.objects.get(pk= id)
    except Taxon.DoesNotExist:
       taxon = None

    try:
       sub_clase = Taxon.objects.filter(taxonrelax=taxon).exclude(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Clase")
    except Taxon.DoesNotExist:
       sub_clase = None

    try:
       orden = Taxon.objects.filter(taxonrelax=taxon).filter(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Orden")
    except Taxon.DoesNotExist:
       orden = None
	   
    return render_to_response("especies/clase.html",{'sub_clase':sub_clase,'orden':orden}, context_instance=RequestContext(request))	
	

def orden(request,id):
    try:
       taxon = Taxon.objects.get(pk= id)
    except Taxon.DoesNotExist:
       taxon = None

    try:
       sub_orden = Taxon.objects.filter(taxonrelax=taxon).exclude(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Orden")
    except Taxon.DoesNotExist:
       sub_orden = None

    try:
       familia = Taxon.objects.filter(taxonrelax=taxon).filter(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Familia")
    except Taxon.DoesNotExist:
       familia = None
	   
    return render_to_response("especies/orden.html",{'sub_orden':sub_orden,'familia':familia}, context_instance=RequestContext(request))	


def familia(request,id):
    try:
       taxon = Taxon.objects.get(pk= id)
    except Taxon.DoesNotExist:
       taxon = None

    try:
       sub_familia = Taxon.objects.filter(taxonrelax=taxon).exclude(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Familia")
    except Taxon.DoesNotExist:
       sub_familia = None

    try:
       genero = Taxon.objects.filter(taxonrelax=taxon).filter(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Genero")
    except Taxon.DoesNotExist:
       genero = None
	   
    return render_to_response("especies/familia.html",{'sub_familia':sub_familia,'genero':genero}, context_instance=RequestContext(request))	
	
	
def genero(request,id):
    try:
       taxon = Taxon.objects.get(pk= id)
    except Taxon.DoesNotExist:
       taxon = None

    try:
       sub_genero = Taxon.objects.filter(taxonrelax=taxon).exclude(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Genero")
    except Taxon.DoesNotExist:
       sub_genero = None

    try:
       especie = Taxon.objects.filter(taxonrelax=taxon).filter(subtipo__nombre="Principal").filter(subtipo__tipotax__nombre="Especie")
    except Taxon.DoesNotExist:
       especie = None
	   
    return render_to_response("especies/genero.html",{'sub_genero':sub_genero,'especie':especie}, context_instance=RequestContext(request))	

def extficha(request,id):
    try:
        taxon = Taxon.objects.get(id=id)
    except Taxon.DoesNotExist:
        taxon = None
		
    try:
        taxoninferior1 = Taxon.objects.filter(taxonrelax=taxon)
    except Taxon.DoesNotExist:
        taxon = None
    return render_to_response('especies/fichaext.html', {'taxon':taxon,'taxoninferior1':taxoninferior1})
	
def contficha(request,id):
    try:
        taxon = Taxon.objects.get(id=id)
    except Taxon.DoesNotExist:
        taxon = None
		
    try:
        taxoninferior1 = Taxon.objects.filter(taxonrelax=taxon)[:1]
    except Taxon.DoesNotExist:
        taxon = None
    return render_to_response('especies/fichaext.html', {'taxon':taxon,'taxoninferior1':taxoninferior1})
	
def ficha(request,cat,id):
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
        taxon = Taxon.objects.get(id=id)
    except Taxon.DoesNotExist:
        taxon = None
		
    try:
        taxoninferior1 = Taxon.objects.filter(taxonrelax=taxon)
    except Taxon.DoesNotExist:
        taxon = None
		
    try:
        taxoninferiorcount = Taxon.objects.filter(taxonrelax=taxon).count()
    except Taxon.DoesNotExist:
        taxoninferiorcount = None
		
    try:
        #avistamientos = Avistamientos.objects.filter(Q(especie=taxon) & Q(estatu=2)).annotate(avistamientocnt = Count('puntosavistamientos')).order_by('-avistamientocnt')
        avistamientos = Avistamientos.objects.filter(Q(especie=taxon) & (Q(estatu=1) | Q(estatu=0)))
    except Avistamientos.DoesNotExist:
        avistamientos = None
		
    try:
        detalleTax = DetalleTaxon.objects.get(taxon=taxon)
    except DetalleTaxon.DoesNotExist:
        detalleTax = None
		
    try:
        spagricolas = Spagricolas.objects.get(especie=detalleTax)
    except Spagricolas.DoesNotExist:
        spagricolas = None
		
    try:
        spaprovechables = Spaprovechables.objects.get(especie=detalleTax)
    except Spaprovechables.DoesNotExist:
        spaprovechables = None
		
    try:
        spsustentables = Spaprovechamientosustentables.objects.get(especie=detalleTax)
    except Spaprovechamientosustentables.DoesNotExist:
        spsustentables = None
		
    try:
        spexoticas = Spexoticas.objects.get(especie=detalleTax)
    except Spexoticas.DoesNotExist:
        spexoticas = None
		
		
    try:
        sppeligro = Sppeligros.objects.get(especie=detalleTax)
    except Sppeligros.DoesNotExist:
        sppeligro = None
		
		
    try:
        sprepresentativas = Sprepresentativaas.objects.get(especie=detalleTax)
    except Sprepresentativaas.DoesNotExist:
        sprepresentativas = None
		
    try:
        spsalud = Spsaluds.objects.get(especie=detalleTax)
    except Spsaluds.DoesNotExist:
        spsalud = None
		
    try:
        sptrafico = Sptraficos.objects.get(especie=detalleTax)
    except Sptraficos.DoesNotExist:
        sptrafico = None
		
    try:
        secciones = Secciones.objects.get(id=6)
    except Secciones.DoesNotExist:
        secciones = None
		
    try:
        categoria = Categorias.objects.get(id=cat)
    except Categorias.DoesNotExist:
        categoria = None
		
    try:
        lateral = TemplatesInfoLateral.objects.filter((Q(seccion=secciones) & Q(subseccion=categoria)) | (Q(seccion=secciones) & Q(activar=True))).order_by('posicion')
    except TemplatesInfoLateral.DoesNotExist:
        lateral = None
		
    try:
        contribuciones = Colaboradorespersonas.objects.filter(taxon=taxon).order_by('update','estatu')
    except Colaboradorespersonas.DoesNotExist:
        contribuciones = None
		
    try:
        habilitardatos = Colaboradorespersonas.objects.filter(Q(taxon=taxon) & Q(estatu=0) & Q(tipoColaboracion=9)).order_by('update','estatu')
    except Colaboradorespersonas.DoesNotExist:
        habilitardatos = None


  

    return render_to_response('especies/ficha.html', {'taxon':taxon,'categoria':categoria,'secciones':secciones,'lateral':lateral,'detalleTax':detalleTax,'spagricolas':spagricolas,'spaprovechables':spaprovechables,'spsustentables':spsustentables,'spexoticas':spexoticas,'sppeligro':sppeligro,'sprepresentativas':sprepresentativas,'spsalud':spsalud,'sptrafico':sptrafico,'persona':persona,'usuario':id_usuario,'contribuciones':contribuciones,'avistamientos':avistamientos,'taxoninferior1':taxoninferior1,'taxoninferiorcount':taxoninferiorcount,'habilitardatos':habilitardatos})


def patrticipacion(request,id,resp):
    _username = request.user.username
    try:
       id_usuario = User.objects.get(username=_username)
    except User.DoesNotExist:
       id_usuario = None
    try:
       id_persona = PerfilPublico.objects.get(user=id_usuario.id)
    except PerfilPublico.DoesNotExist:
       id_persona = None
    try:
       persona = Directorios.objects.get(pk=id_persona.persona.id)
    except Directorios.DoesNotExist:
       persona = None
    try:
       avistamiento = Avistamientos.objects.get(pk= id)
    except Avistamientos.DoesNotExist:
       avistamiento = None  

    try:
       registro = puntosAvistamientos(avistamiento=avistamiento,persona=persona,opinion=resp) 
       registro.save()
       op=True
    except puntosAvistamientos.DoesNotExist:
       op=False
    return render_to_response("especies/parti.html",{'op':op}, context_instance=RequestContext(request))


def buscador(request):
    print "hola"
    return render_to_response('especies/buscador.html')

def search_view(request ):

	#	Searches in the fields of the given related model and returns the 
	#	result as a simple string to be used by the jQuery Autocomplete plugin

	query=request.GET.get( 'q', None )
	app_label=request.GET.get( 'app_label', None )
	model_name=request.GET.get( 'model_name', None )
	search_fields=request.GET.get( 'search_fields', None )

	if search_fields and app_label and model_name and query:
		def construct_search( field_name ):
			# use different lookup methods depending on the notation
			if field_name.startswith( '^' ):
				return "%s__istartswith"%field_name[1:], field_name[1:]
			elif field_name.startswith( '=' ):
				return "%s__iexact"%field_name[1:], field_name[1:]
			elif field_name.startswith( '@' ):
				return "%s__search"%field_name[1:], field_name[1:]
			else:
				return "%s__icontains"%field_name, field_name

		model=models.get_model( app_label, model_name )
		q=None
		fields=[]
		for field_name in search_fields.split( ',' ):
			name, name1=construct_search( field_name )
			fields.append( name1 )

			if q:
				q=q|models.Q( **{str( name ):query} )
			else:
				q=models.Q( **{str( name ):query} )

		qs=model.objects.filter( q )


		data=''
		for f in qs[0:10]:
			res=[]
                        parts=[]
			for field in fields:
				parts=field.split( '__' )
				if len( parts )>1:
                                       s='%s'%getattr( f, parts[0] )
					#s='%s'%getattr( getattr( f, parts[0] ), parts[1] )
				else:
					s='%s'%getattr( f, parts[0] )
				if s and s not in( res ):
					res.append( s )
			data+=u'%s|%s\n'%( ', '.join( res ), f.pk )

		return HttpResponse( data )

		rel_name=field_name.split( '__' )[0]

		data=''.join( [u'%s|%s\n'%( getattr( f, rel_name ), f.pk ) for f in qs] )
		return HttpResponse( data )
	return HttpResponseNotFound()
