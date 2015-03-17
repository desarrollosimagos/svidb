# -*- coding: utf8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from congresos.models import *
from django.db import connection
from django.contrib.auth.models import *
from especies.models import *
from mapas.models import *
from actores.models import *
from django.db.models import *

def listaInstitucionesCongresos(request):
    cursor = connection.cursor()
    cursor.execute('select distinct(actores_id,nombre,nombre_completo) from "trabajosCongresos_colectivos", "trabajosCongresos", actores  where "trabajosCongresos_colectivos".trabajoscongresos_id="trabajosCongresos".id and "trabajosCongresos".evento_id=7 and actores.id = "trabajosCongresos_colectivos".trabajoscongresos_id')
    rmw = cursor.fetchall()
    return render_to_response('consultas/inst.html',{'resultado':rmw}) 