#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from congresos.models import *
from arbitraje.models import *
from django import forms
from django.contrib import admin
from posiciones.autocomplete.widgets import *
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response

from posiciones.autocomplete.widgets import *

class coordinadorAdmin(AutocompleteModelAdmin):
      list_filter = ('evento','estatu',)
      search_fields = ('coordinador__documentoidentidad','coordinador__nombre', 'coordinador__apellido','coordinador__correo')
      list_display = ('evento','coordinador','estatu',)
      related_search_fields = {
                'coordinador': ('id','documentoidentidad','nombre',),
      }

admin.site.register(coordinador,coordinadorAdmin)


#class TabTrabajosArbitrosAdmin(AutocompleteTabularInline):
#      model = TrabajosArbitros
#      extra = 1
#      related_search_fields = {
#                'trabajos': ('titulo','directorio__documentoidentidad','directorio__nombre',),
#      }

class arbitrosAdmin(AutocompleteModelAdmin):
      list_filter = ('evento','estatu','coordinador','modalidad','tematicas','accespecifi',)
      search_fields = ('coordinador__documentoidentidad','coordinador__nombre', 'coordinador__apellido','coordinador__correo','arbitro__documentoidentidad','arbitro__nombre', 'arbitro__apellido','arbitro__correo')
      list_display = ('evento','coordinador','arbitro','estatu',)
      fieldsets = [
            ('Datos Generales',               {'fields':  ['evento','coordinador','arbitro']}),
            ('Datos Trasversales', {'fields': ['accespecifi','modalidad','tematicas','estatu'],}),
        ]
      related_search_fields = {
                'arbitro': ('id','documentoidentidad','nombre',),
      }

admin.site.register(arbitros,arbitrosAdmin)


def cambiarEstadoArbitrando(modeladmin, request, queryset):
    queryset.update(estatu=3)
cambiarEstadoArbitrando.short_description = "Cambiar estatus a Arbitrando"

def cambiarEstadoAprobado(modeladmin, request, queryset):
    queryset.update(estatu=1)
cambiarEstadoAprobado.short_description = "Cambiar estatus a Aprobado"

def cambiarEstadoRechazado(modeladmin, request, queryset):
    queryset.update(estatu=2)
cambiarEstadoRechazado.short_description = "Cambiar estatus a Rechazado"


class TrabajosArbitrosAdmin(admin.ModelAdmin):
      actions = [cambiarEstadoArbitrando,cambiarEstadoAprobado,cambiarEstadoRechazado]
      list_filter = ('estatu','arbitro')
      search_fields = ('arbitro__arbitro__documentoidentidad','arbitro__arbitro__nombre', 'arbitro__arbitro__apellido','arbitro__arbitro__correo')
      list_display = ('trabajos','arbitro','estatu',)
      fieldsets = [
            ('Datos Generales',               {'fields':  ['evento','coordinador','arbitro']}),
            ('Datos Trasversales', {'fields': ['trabajos','estatu'],}),
        ]


admin.site.register(TrabajosArbitros,TrabajosArbitrosAdmin)

admin.site.register(MensajeTrabajosArbitraje)

admin.site.register(HistorialModificacionesTrabajos)


