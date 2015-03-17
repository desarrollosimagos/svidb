#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from menu.models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response
from mapas.models import Colaboradorespersonas

from posiciones.autocomplete.widgets import *

class DetalleCategorias(admin.TabularInline):
    model = Categorias
    extra=1

#========================================================================================
class SeccionesAdmin(admin.ModelAdmin):
      inlines = [DetalleCategorias]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SeccionesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
 
admin.site.register(Secciones,SeccionesAdmin)

#========================================================================================

class CategoriasAdmin(admin.ModelAdmin):
      list_filter = ('seccione',)
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(CategoriasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Categorias,CategoriasAdmin)

admin.site.register(SubTipoCategorias)


#=================================================================================================
class colaborar(AutocompleteTabularInline):
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
          return super(colaborar, self).formfield_for_foreignkey(db_field, request, **kwargs) 


class MapasAdmin(AutocompleteModelAdmin):
      fieldsets = [
            ('Datos del Mapa',{'fields': ['nombre','secciones','fuente','basecartogra','observaciones','pathimg1','pathimg2','pathimg3']}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      related_search_fields = { 
                'direct': ('id','nombre',),
      }
      list_display=('nombre','estatu')
      search_fields = ('nombre',)
      list_filter = ('estatu',)
      inlines = [colaborar]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(MapasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Mapas,MapasAdmin)

class ImagenesSistemasAdmin(admin.ModelAdmin):
      def imagen(self, instance):
          file_name=str(instance.pathimg)
          splitted_filename = list(os.path.splitext(file_name))
          splitted_filename.insert(1, '.157_118')
          file_nombre_157_118 = ''.join(splitted_filename)
          return u"<img src=\"/media/%s\" height=\"150px\" width=\"150pxpx\" />" %(file_nombre_157_118)

      imagen.allow_tags = True
      imagen.short_description = ''
      list_display = ('id','imagen','tipo','estatu','seccion','userupdate')
      list_display_links = ('id','tipo','estatu','seccion')
      def id(self, instance):
          return instance.id
      search_fields = ('descripcion','titulo')
      list_filter = ('estatu','seccion','tipo')
      
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ImagenesSistemasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(ImagenesSistemas,ImagenesSistemasAdmin)

