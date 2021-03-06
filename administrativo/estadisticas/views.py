# -*- coding: utf8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.db import connection
from django.contrib.auth.models import *
from especies.models import *
from mapas.models import *
from actores.models import *
from django.db.models import *
from perfil.models import PerfilPublico,ModulosPublicos,PerfilModulos

from congresos.models import *
from arbitraje.models import *

def asistenciaCongresos(request):
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
    cursor = connection.cursor()
    cursor.execute('select eventos.fecha,count(*) from "participacioEvento", eventos where "participacioEvento".evento_id=eventos.id and eventos.estatu_id=3 and "participacioEvento".estatu_id=3  group by eventos.fecha order by eventos.fecha')
    rmw = cursor.fetchall()
    try:
       datosparticipantes = participacioEvento.objects.filter(Q(evento__estatu=3) & Q(estatu=3)).order_by('evento__estado')
    except participacioEvento.DoesNotExist:
       datosparticipantes = None
    try:
       datosparticipantesNacimiento = participacioEvento.objects.filter(estatu=3).order_by('directorio__nacimiento')
    except participacioEvento.DoesNotExist:
       datosparticipantesNacimiento = None
    return render_to_response('estadisticas/asistenciacongresos.html',{'resultado':rmw,'persona':persona,'datosparticipantes':datosparticipantes,'datosparticipantesNacimiento':datosparticipantesNacimiento}) 
	
def InscripcionesCongresos(request,id):
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
       datosparticipantes = participacioEvento.objects.filter(Q(evento__id=id) & Q(estatu=3)).order_by('directorio__sexo')
    except participacioEvento.DoesNotExist:
       datosparticipantes = None
    try:
       datosparticipantesNacimiento = participacioEvento.objects.filter(Q(evento__id=id) & Q(estatu=3)).order_by('directorio__nacimiento')
    except participacioEvento.DoesNotExist:
       datosparticipantesNacimiento = None
    cursor = connection.cursor()
    cursor.execute('select estatu_id,count(directorio_id) from "participacioEvento" where evento_id=' + id + ' group by estatu_id order by estatu_id')
    rmw = cursor.fetchall()
    cursor2 = connection.cursor()
    cursor2.execute('select estados.nombre ,count(directorios.id) from "participacioEvento",directorios,estados where "participacioEvento".evento_id=' + id + ' and "participacioEvento".directorio_id = directorios.id and directorios.estado_id = estados.id group by estados.nombre order by estados.nombre')
    rmw2 = cursor2.fetchall()
    return render_to_response('estadisticas/congresos/grafica1.html',{'resultado':rmw,'participantes':rmw2,'persona':persona,'datosparticipantes':datosparticipantes,'datosparticipantesNacimiento':datosparticipantesNacimiento}) 
	
	
def TrabajosEstadisticas(request,id):
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
    trabajos = Trabajoscongresos.objects.filter(Q(evento__id=id) & Q(estatu=1)).order_by('modalidad')
    trabajos2 = Trabajoscongresos.objects.filter(Q(evento__id=id) & Q(estatu=1)).order_by('tematicas')
    trabajos3 = Trabajoscongresos.objects.filter(Q(evento__id=id) & Q(estatu=1)).order_by('estatu')
    trabajos4 = Trabajoscongresos.objects.filter(Q(evento__id=id) & Q(estatu=1)).order_by('accespecifi')
    trabajos5 = Trabajoscongresos.objects.filter(evento__id=id).order_by('estatu')
    try:
       arbitrados =  TrabajosArbitros.objects.filter(trabajos__evento__id=id).order_by('estatu')
    except TrabajosArbitros.DoesNotExist:
       arbitrados = None
	
    return render_to_response('estadisticas/congresos/grafica2.html',{'resultado':trabajos,'resultado2':trabajos2,'resultado3':trabajos3,'resultado4':trabajos4,'persona':persona,'trabajos5':trabajos5,'arbitrados':arbitrados}) 
	


def detalleTipoTaxon(request):
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
    cursor = connection.cursor()
    cursor.execute('select tipotaxon.nombre as tipo, count(*) as numero  from taxon,tipotaxon where taxon.subtipo_id=tipotaxon.id group by tipotaxon.nombre')
    rmw = cursor.fetchall()
    return render_to_response('estadisticas/esta5.html',{'resultado':rmw,'persona':persona}) 
	
def actoresTotalCargados(request):
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
        actores = Actores.objects.filter().count()
    except Actores.DoesNotExist:
        actores = None
    try:
        actores_activos = Actores.objects.filter(Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).count()
    except Actores.DoesNotExist:
        actores_activos = None	
    try:
        actores_pendientes = Actores.objects.filter(Q(colaboradorespersonas__estatu=2) & Q(colaboradorespersonas__tipoColaboracion=9)).count()
    except Actores.DoesNotExist:
        actores_pendientes = None
    try:
        actores_datosp = Actores.objects.filter(Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=18)).count()
    except Actores.DoesNotExist:
        actores_datosp = None	
    try:
        actores_datospp = Actores.objects.filter(Q(colaboradorespersonas__estatu=2) & Q(colaboradorespersonas__tipoColaboracion=18)).count()
    except Actores.DoesNotExist:
        actores_datospp = None	
    try:
        resto = Actores.objects.filter()
        resta = resto.exclude(Q(colaboradorespersonas__tipoColaboracion=9)).count()
    except Actores.DoesNotExist:
        resto = None	
    return render_to_response('estadisticas/actores/01.html',{'actores_activos':actores_activos,'actores_pendientes':actores_pendientes,'actores_datosp':actores_datosp,'actores_datospp':actores_datospp,'actores':actores,'resto':resta,'persona':persona}) 
		
		
def areasTotalCargados(request):
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
        actores = Areas.objects.filter().count()
    except Areas.DoesNotExist:
        actores = None
    try:
        actores_activos = Areas.objects.filter(Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=9)).count()
    except Areas.DoesNotExist:
        actores_activos = None	
    try:
        actores_pendientes = Areas.objects.filter(Q(colaboradorespersonas__estatu=2) & Q(colaboradorespersonas__tipoColaboracion=9)).count()
    except Areas.DoesNotExist:
        actores_pendientes = None
    try:
        actores_datosp = Areas.objects.filter(Q(colaboradorespersonas__estatu=0) & Q(colaboradorespersonas__tipoColaboracion=18)).count()
    except Areas.DoesNotExist:
        actores_datosp = None	
    try:
        actores_datospp = Areas.objects.filter(Q(colaboradorespersonas__estatu=2) & Q(colaboradorespersonas__tipoColaboracion=18)).count()
    except Areas.DoesNotExist:
        actores_datospp = None	
    try:
        resto = Areas.objects.filter()
        resta = resto.exclude(Q(colaboradorespersonas__tipoColaboracion=9)).count()
    except Actores.DoesNotExist:
        resto = None	
    return render_to_response('estadisticas/areas/01.html',{'actores_activos':actores_activos,'actores_pendientes':actores_pendientes,'actores_datosp':actores_datosp,'actores_datospp':actores_datospp,'actores':actores,'resto':resta,'persona':persona})
	
def estadisticataxon1(request):
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
        taxon=Taxon.objects.filter().count()
    except Taxon.DoesNotExist:
        taxon = None
    try:
        dtaxon=DetalleTaxon.objects.filter().count()
    except DetalleTaxon.DoesNotExist:
        dtaxon = None	
    diferencia = taxon - dtaxon
    return render_to_response('estadisticas/esta1.html',{'taxon':taxon,'dtaxon':dtaxon,'diferencia':diferencia,'persona':persona})  
	
	
def estadisticataxon2(request):
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
        taxon=Taxon.objects.filter().count()
    except Taxon.DoesNotExist:
        taxon = None
    try:
        dtaxon=DetalleTaxon.objects.filter().count()
    except DetalleTaxon.DoesNotExist:
        dtaxon = None	
		
    try:
        esptraf=DetalleTaxon.objects.filter(esptraf=True).count()
    except DetalleTaxon.DoesNotExist:
        esptraf = None	
		
    try:
        espaprove=DetalleTaxon.objects.filter(espaprove=True).count()
    except DetalleTaxon.DoesNotExist:
        espaprove = None
		
    try:
        espsalud=DetalleTaxon.objects.filter(espsalud=True).count()
    except DetalleTaxon.DoesNotExist:
        espsalud = None
		
    try:
        esppeligr=DetalleTaxon.objects.filter(esppeligr=True).count()
    except DetalleTaxon.DoesNotExist:
        esppeligr = None	
		
    try:
        espexot=DetalleTaxon.objects.filter(espexot=True).count()
    except DetalleTaxon.DoesNotExist:
        espexot = None	
		
    try:
        espagrico=DetalleTaxon.objects.filter(espagrico=True).count()
    except DetalleTaxon.DoesNotExist:
        espagrico = None

    try:
        falseCla=DetalleTaxon.objects.filter(Q(espagrico=False) & Q(espagrico=False) & Q(espexot=False) & Q(esppeligr=False) & Q(espsalud=False) & Q(espaprove=False) & Q(esptraf=False)).count()
    except DetalleTaxon.DoesNotExist:
        falseCla = None	
#    suma = espagrico + espexot + esppeligr + espsalud + espaprove + esptraf

    return render_to_response('estadisticas/esta2.html',{'taxon':taxon,'espagrico':espagrico,'espexot':espexot,'esppeligr':esppeligr,'espsalud':espsalud,'espaprove':espaprove,'esptraf':esptraf,'falseCla':falseCla,'dtaxon':dtaxon,'persona':persona})    

def ExoticasReportesPorEstados(request):
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
        lista_exo = Avistamientos.objects.filter().order_by('-estado')
    except Avistamientos.DoesNotExist:
        lista_exo = None
    return render_to_response('estadisticas/exoticas/02.html',{'lista_exo':lista_exo,'persona':persona}) 
	
def exoticasreport(request):
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
        lista_exo = Taxon.objects.filter(detalletaxon__espexot=True).annotate(numeroavistamientos = Count('avistamientos')).order_by('-numeroavistamientos')[:10]
    except Taxon.DoesNotExist:
        lista_exo = None
    return render_to_response('estadisticas/exoticas/01.html',{'lista_exo':lista_exo,'persona':persona}) 


def actoresporCategoria(request):
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
    cursor = connection.cursor()
    cursor.execute('select categorias.titulo,count(*) from actores,categorias where actores.categoriact_id=categorias.id and actores.estatu_id=0 group by categorias.titulo order by categorias.titulo')
    rmw = cursor.fetchall()

    try:
        actor = Actores.objects.filter().count()
    except Actores.DoesNotExist:
        actor = None
    return render_to_response('estadisticas/esta4.html',{'resultado':rmw,'actor':actor,'persona':persona}) 
	

