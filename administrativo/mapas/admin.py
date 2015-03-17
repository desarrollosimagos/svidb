#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms.widgets import TextInput
from listasTematicas.models import *
from areas.models import Areas
from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField
from posiciones.autocomplete.widgets import *
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response

from posiciones.autocomplete.widgets import *

from mapas.models import *


class GeoLocalizaionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField: {'widget': GoogleMapsAddressWidget},
        GeoLocationField: {'widget': TextInput(attrs={'readonly': 'readonly'})},
    }

admin.site.register(GeoLocalizaion, GeoLocalizaionAdmin)

class AvistamientosAdmin(AutocompleteModelAdmin):
    list_filter = ('estatu',)
    list_display = ('fechaAvistamiento','especie','persona','estado','estatu',)
    related_search_fields = { 
                'especie': ('nombre','id',),
                'persona': ('nombre','apellido','documentoidentidad','correo',),
    }
    fieldsets = [
            ('Datos Colaborador',               {'fields': ['persona']}),
            ('Datos Avistamiento',               {'fields': ['especie','fechaAvistamiento','desde','pai','estado','municipio','parroquia','sector','puntor','address','geolocation','gps','pathimg1']}),
            ('Datos Complementarios', {'fields': ['entorno','numero','tamaniop','medidasc','cuamedida','frecuencia','observaciones','estatu',],}),]
    formfield_overrides = {
        AddressField: {'widget': GoogleMapsAddressWidget},
        GeoLocationField: {'widget': TextInput(attrs={'readonly': 'readonly'})},
    }

admin.site.register(Avistamientos,AvistamientosAdmin)

class RColaboradorespersonasAdmin(AutocompleteTabularInline):
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
          return super(RColaboradorespersonasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
		  
class contriBibliotecaAdmin(AutocompleteTabularInline):
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
          return super(RColaboradorespersonasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
		  
class EtniasAdmin(AutocompleteModelAdmin):
      list_display = ('nombre',)
      inlines = [RColaboradorespersonasAdmin]
      related_search_fields = { 
                'especierepre':  ('id','nombre',),
                'actvinc':  ('id','nombre_completo'),
                'bancaudio':  ('id','descripcion',),
                'biblio':  ('id','autores','titulo',),
                'bibliogra':  ('id','autores','titulo',),
                'enlaces':  ('id','enlaces',),
                'url':  ('id','enlaces',),
                'manisfes':  ('id','titulo',),
      }
      fieldsets = [
            ('Datos Generales',{'fields': ['nombre','otrosnombre','descripcion','descripcionge','vivienda','subsistencia','vidasosial','idioma','especierepre','actvinc']}),
            ('Datos Transversales', {'fields': ['bancaudio','biblio','enlaces','manisfes'],}),
            ('Bibliografia', {'fields': ['bibliogra','url'],}),
            ('Datos de Validación', {'fields': ['userupdate'],}),
      ]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(EtniasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 		  
		  
admin.site.register(Etnias,EtniasAdmin)


class contriBibliotecaAdmin(AutocompleteTabularInline):
      model = contriBiblioteca
      extra = 1
      related_search_fields = { 
	           'contribucion' : ('id','titulo',),
      }
	  
class contriAudioAdmin(AutocompleteTabularInline):
      model = contriAudio
      extra = 1
      related_search_fields = { 
	           'contribucion' : ('id','titulo',),
      }
	  
class contriAvistamientoAdmin(AutocompleteTabularInline):
      model = contriAvistamiento
      extra = 1
      related_search_fields = { 
	           'contribucion' : ('id','titulo',),
      }

#=================================================================================================
# RELACIONES PARA COLABORADORES PERSONAS
#==================================================================================================


class ColaboradorespersonasAdmin(AutocompleteModelAdmin):
      inlines = [contriBibliotecaAdmin,contriAudioAdmin,contriAvistamientoAdmin]
      related_search_fields = { 
                'persona': ('nombre','id','documentoidentidad','apellido'),
                'taxon': ('nombre','subtipo__nombre','id'),
                'cultural': ('titulo','id'),
                'colectivos': ('nombre','nombre_completo','id'),
                'areas': ('nombre','id'),
                'etnias': ('nombre','id'),
                'mapas': ('nombre','id'),
                'bioregiones': ('nombre','id'),

      }
      list_display = ('fecha','tipoColaboracion','persona','titulo','Estatus')
      search_fields = ('titulo','persona__documentoidentidad')
      list_filter = ('tipoColaboracion','estatu')
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ColaboradorespersonasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 


admin.site.register(Colaboradorespersonas,ColaboradorespersonasAdmin)


#=================================================================================================
class EtniaareasAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(EtniaareasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Etniaareas,EtniaareasAdmin)


admin.site.register(contriBiblioteca)
admin.site.register(contriAudio)
admin.site.register(contriAvistamiento)
admin.site.register(puntosAvistamientos)
	  




