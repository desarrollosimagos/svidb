#!/usr/bin/python -u
# -*- coding: utf-8 -*-
#from especies.models import *
from areas.models import *
from mapas.models import Etnias,Etniaareas
from mapas.models import Colaboradorespersonas
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response

from posiciones.autocomplete.widgets import *


#=================================================================================================
class ServiciosAreaAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ServiciosAreaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 


admin.site.register(ServiciosArea,ServiciosAreaAdmin)


#=================================================================================================
class UbicacionsAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(UbicacionsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Ubicacions,UbicacionsAdmin)


class RedesAreasAdmin(admin.TabularInline):
      model = RedessocialesAreas
      extra = 0

class ColaboradorespersonasAdmin(AutocompleteTabularInline):
      model = Colaboradorespersonas
      extra = 1
      related_search_fields = { 
	           'cultural' : ('id','titulo',),
	           'colectivos' : ('id','nombre_completo',),
	           'areas' : ('id','nombre',),
	           'etnias' : ('id','nombre',),
	           'mapas' : ('id','nombre',),
	           'taxon' : ('id','nombre',),
	           'persona' : ('id','documentoidentidad','nombre','apellido',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ColaboradorespersonasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 

class EtniasAdmin(admin.TabularInline):
      model = Etnias
      extra = 1
      max_num = 1
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(EtniasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 

#class MapasAreasAdmin(admin.TabularInline):
#      model = Mapasareas
#      extra = 1
#      def formfield_for_foreignkey(self, db_field, request, **kwargs):
#          if db_field.name == "userupdate":
#             kwargs["queryset"] = User.objects.filter(id=request.user.id)
#          return super(MapasAreasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
		  
class EtniasAreasAdmin(admin.TabularInline):
      model = Etniaareas
      extra = 1
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(EtniasAreasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
		  
class AreasAdmin(AutocompleteModelAdmin):
      list_filter = ('estatu','categoriact', 'subtipoas')
      list_display = ('categoriact', 'subtipoas','nombre','estatu')
      list_display_links = ('categoriact', 'subtipoas','nombre','estatu')
      search_fields = ('nombre',)
      inlines = [EtniasAreasAdmin,RedesAreasAdmin,ColaboradorespersonasAdmin]
      fieldsets = [
            ('Información General',{'fields': ['categoriact', 'subtipoas','nombre','siglas','areasrex','descricion','datecreado','biblioteca','objetocreado','particuld','planorden','actore']}),
            ('Ubicación', {'fields': ['ubicpol','bioregion'],}),
            ('Información Turística', {'fields': ['horario','servic','comollegar'],}),
            ('Caracteristicas', {'fields': ['superficie','altitud','clima','ecosistema','geologia','geomorfo','hidrografia','suelos'],}),
            ('Factores Antrópicos', {'fields': ['concesiones','impacantro','inicpart','tipoyusrecur'],}),
            ('Especies', {'fields': ['esprepretxt','esprepre'],}),
            ('Poblaciones', {'fields': ['asentahumanos'],}),
            ('Bibliografía', {'fields': ['bibliografia','url'],}),
            ('Datos Transversales', {'fields': ['bancoaudio','mapas','docasocia','glosar','manisf'],}),
            ('Vinculación con Actores', {'fields': ['orgcolab','personacolab'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),

        ]
      related_search_fields = { 
                'actore': ('id','nombre','nombre_completo',),
                'ubicpol': ('id','municipio__estado__nombre','municipio__nombre','nombre',),
                'bancoaudio': ('id','descripcion',),
                'bibliografia': ('id','autores','titulo',),
                'biblioteca': ('id','titulo',),
                'orgcolab': ('id','categoriact__titulo','nombre_completo',),
                'personacolab': ('id','nombre','apellido'),
                'planorden': ('id','titulo',),
                'esprepre': ('id','nombre','subtipo__nombre',),
                'docasocia': ('id','autores','titulo',),
                'glosar': ('id','nombre',),
                'manisf': ('id','titulo',),
                'areasrex': ('areasrex__id','areasrex__nombre','areasrex__categoriact','areasrex__subtipoas'),
                'url': ('id','enlaces',),
                'mapas': ('id','nombre',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          if db_field.name == "categoriact":
             kwargs["queryset"] = Categorias.objects.filter(seccione__titulo='Áreas Estratégicas para la Conservación')
          return super(AreasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Areas,AreasAdmin)

admin.site.register(RedessocialesAreas)
