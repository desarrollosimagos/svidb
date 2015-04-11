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


def index(request):
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
    return render_to_response('mod_eventos/index.html',{'persona':persona})

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

