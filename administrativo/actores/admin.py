#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from especies.models import *
import os
from actores.models import *
from inicio.models import *
from congresos.models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response
from mapas.models import Colaboradorespersonas
from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField
from django.forms.widgets import TextInput
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin

from posiciones.autocomplete.widgets import *

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
		  
#-===========================================================================
class ManifestacionesculturalesAdmin(AutocompleteModelAdmin):
      inlines = [ColaboradorespersonasAdmin]
      filter_horizontal = ('bancoaudio',)
      fieldsets = [
            ('Datos Generales',               {'fields':  ['titulo','descripcion','tipo']}),
            ('Datos Trasversales', {'fields': ['bancoaudio','bibliog'],}),
            ('Bibliografía', {'fields': ['biblio','url'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      related_search_fields = { 
                'bibliog': ('id','titulo'),
                'bancoaudio': ('id','descripcion','fecha'),
                'url': ('id','nombre','enlaces',),
                'biblio': ('id','titulo',),
      }
      list_display=('titulo','tipo','estatu')
      search_fields = ('titulo','descripcion')
      list_filter = ('estatu',)
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ManifestacionesculturalesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Manifestacionesculturales,ManifestacionesculturalesAdmin)

#-===========================================================================
class DirectoriosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
      resource_class = DirectoriosResource
      pass
      filter_horizontal = ('areasaccion','fund')
      list_filter = ('estatu','areasaccion','estado','fund','tipodoci')
      search_fields = ('documentoidentidad','nombre', 'apellido','correo')
      list_display = ('documentoidentidad','nombre', 'apellido','estatu')
      list_display_links = ('documentoidentidad','nombre', 'apellido','estatu')
      fieldsets = [
            ('Datos Basicos',               {'fields': ['tipodoci','documentoidentidad','nombre','apellido','sexo','edocivil','nacimiento','correo','telefono1','telefono2','fax','movil','listacorreos','ocupacion']}),
#            ('Datos Basicos',               {'fields': ['documentoidentidad','nombre','apellido','correo','telefono1','telefono2','fax','movil','sector']}),
            ('Datos Demograficos', {'fields': ['pai','estado','municipio','parroquia','sector'],}),
            ('Datos de Contenido', {'fields': ['gruposespecie','localidadesaccion','areasaccion','fund','organizacion','suscritobool'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(DirectoriosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Directorios,DirectoriosAdmin)


class RedesAdmin(admin.TabularInline):
      model = Redessociales
      extra = 1
	  
class DocAsocActAdmin(AutocompleteTabularInline):
      model = DocAsocActores
      extra = 1
      related_search_fields = { 
	           'blibliote' : ('titulo','autores','ibsn'),
      }

class MiembrosdeInstitucionesAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'miembros': ('id','documentoidentidad','nombre','apellido'),
                'institucion': ('id','nombre','nombre_completo'),
      }
admin.site.register(MiembrosdeInstituciones,MiembrosdeInstitucionesAdmin)


class SistemaMensajeriaAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'remi': ('id','documentoidentidad','nombre','apellido'),
                'destino': ('documentoidentidad','nombre','apellido','id'),
      }
admin.site.register(SistemaMensajeria,SistemaMensajeriaAdmin)

class TrabajosInline(admin.TabularInline):
      model = Trabajoscongresos.colectivos.through


class ActoresAdmin(ImportExportModelAdmin,AutocompleteModelAdmin):
      resource_class = ActoresResource
      pass
      inlines = [DocAsocActAdmin,RedesAdmin,ColaboradorespersonasAdmin,TrabajosInline]
      list_filter = ('estatu','estado','categoriact','tipocolec',)
      related_search_fields = { 
                'directorio': ('id','documentoidentidad','nombre','apellido'),
                'bancoaudio': ('id','descripcion','fecha'),
                'url': ('id','nombre','enlaces',),
                'actoresrex': ('id','nombre_completo',),
      }
      formfield_overrides = {
          AddressField: {'widget': GoogleMapsAddressWidget},
          GeoLocationField: {'widget': TextInput(attrs={'readonly': 'readonly'})},
      }
      fieldsets = [
            ('Vinculación con Actores', {'fields': ['actoresrex','directorio'],}),
            ('Datos Basicos',               {'fields':  ['categoriact','tipocolec','tipoorganizacion','nombre_completo','siglas','nombre','rif','correo','url','telefono','fax','logotipo']}),
            ('Datos Demograficos', {'fields': ['pai','estado','municipio','parroquia','direccion','address','geolocation','coord'],}),
            ('Datos de Contenido', {'fields': ['aniofundacion','reseniahistorica','numeromiembros','estrucorg','objetivos','particularidades','principalesorgfinan','publicacionesPeriodicas','horarios'],}),
            ('Accionar', {'fields': ['ambitoaccion','actinteres','grupobio','tiposAreasAccion','fund','areasesconserv'],}),
            ('Datos Trasversales', {'fields': ['bancoaudio'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      filter_horizontal = ('fund','tiposAreasAccion','bancoaudio')
      search_fields = ('nombre', 'siglas','nombre_completo','rif')
      list_display = ('categoriact','tipocolec','nombre_completo','estatu')
      list_display_links = ('categoriact','tipocolec','nombre_completo','estatu')
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          if db_field.name == "categoriact":
             kwargs["queryset"] = Categorias.objects.filter(seccione__id=5)
          return super(ActoresAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Actores,ActoresAdmin)


admin.site.register(DetalleBiblioteca)


#=================================================================================================
class BibliotecasAdmin(AutocompleteModelAdmin):
      fieldsets = [
            ('Datos del Documento',{'fields': ['repositoriolinea','tipodocs','titulo','fecha','autores','autorinstitucional','editorial','resumen','observaciones','idioma','ibsn','edicion','numerovolumen','numeropaginas','licencia']}),
            ('Vinculación con Usuarios', {'fields': ['directorio'],}),
            ('Repositorios Fisicos', {'fields': ['biblioteca'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      related_search_fields = { 
                'directorio':  ('id','documentoidentidad','nombre','apellido'),
      }
      list_display=('titulo','fecha','autores')
      search_fields = ('titulo','autores','editorial','resumen','autorinstitucional')
      list_filter = ('estatu',)
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(BibliotecasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Bibliotecas,BibliotecasAdmin)


#=================================================================================================
class BancoaudiovisualsAdmin(AutocompleteModelAdmin):
      def imagen(self, instance):
          file_name=str(instance.pathimg)
          splitted_filename = list(os.path.splitext(file_name))
          splitted_filename.insert(1, '.157_118')
          file_nombre_157_118 = ''.join(splitted_filename)
          return u"<img src=\"/media/%s\" height=\"150px\" width=\"150pxpx\" />" %(file_nombre_157_118)

      imagen.allow_tags = True
      imagen.short_description = ''
      list_display = ('id','imagen','directorio','tipo','estatu','seccion','userupdate')
      list_display_links = ('id','directorio','tipo','estatu','seccion')
      def id(self, instance):
          return instance.id
      search_fields = ('directorio__documentoidentidad','directorio__nombre','directorio__apellido','lugar','descripcion','observaciones')
      list_filter = ('estatu','seccion',)
      fieldsets = [
            ('Datos del Colaborador',{'fields': ['directorio']}),
            ('Datos del Aduiovisual', {'fields': ['pathimg','seccion','fecha','lugar','descripcion','observaciones','tipo','licencia','url'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      related_search_fields = { 
                'directorio':  ('id','documentoidentidad','nombre','apellido'),
                'url': ('id','enlaces',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(BancoaudiovisualsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Bancoaudiovisuals,BancoaudiovisualsAdmin)


class BioregionsAdmin(AutocompleteModelAdmin):
      list_display = ('nombre','estatu')
      related_search_fields = { 
                'bancoaudio': ('id','descripcion',),
                'bibliografia': ('id','autores','titulo',),
                'docasocia': ('id','autores','titulo',),
                'glosar': ('id','nombre',),
                'manisf': ('id','titulo',),
                'enlaces': ('id','enlaces',),
                'url': ('id','enlaces',),
                'mapas': ('id','nombre',),
      }
      fieldsets = [
            ('Datos Generales',{'fields': ['nombre','superficie','ubicacion','altitud','geologia','geomorfologia','hidrografia','clima','suelos','ecosistemas','impactos_antropicos']}),
            ('Datos Transversales', {'fields': ['bancoaudio','mapas','docasocia','glosar','manisf','enlaces'],}),
            ('Bibliografia', {'fields': ['bibliografia','url'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      inlines=[ColaboradorespersonasAdmin]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(BioregionsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Bioregions,BioregionsAdmin)

#=================================================================================================
class TipoareaaccionsAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TipoareaaccionsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Tipoareaaccions,TipoareaaccionsAdmin)

admin.site.register(ActoresCCModificados)
