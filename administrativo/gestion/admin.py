#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from gestion.models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response
from posiciones.autocomplete.widgets import *

#from sorl.thumbnail.admin import AdminImageMixin

#-===========================================================================
admin.site.register(Tablas) 

#-===========================================================================
admin.site.register(Tipoelementos) 

#-===========================================================================
admin.site.register(Estatus)

admin.site.register(EnlacesExternos)

admin.site.register(Tsauro)

#-===========================================================================
class TipoorganizacionsAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TipoorganizacionsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Tipoorganizacions,TipoorganizacionsAdmin) 

#-===========================================================================
class DocumentosgeneradosAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(DocumentosgeneradosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Documentosgenerados,DocumentosgeneradosAdmin)

#-===========================================================================
class PablabrasclavesAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(PablabrasclavesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Pablabrasclaves,PablabrasclavesAdmin) 

#=================================================================================================

class TiposManifestacionesAdmin(admin.ModelAdmin):
#      inlines = [DetalleManifestacionesculturales]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TiposManifestacionesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(TiposManifestaciones,TiposManifestacionesAdmin)


#-===========================================================================
admin.site.register(Servicios) 

#-===========================================================================
class RedsAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RedsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Reds,RedsAdmin) 


#-===========================================================================
class PreguntasFrecuentesAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(PreguntasFrecuentesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(PreguntasFrecuentes,PreguntasFrecuentesAdmin) 


class GlosarioAdmin(admin.ModelAdmin):
      list_display=('nombre','estatu')
      search_fields = ('nombre',)
      list_filter = ('estatu',)
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(GlosarioAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Glosario,GlosarioAdmin)

admin.site.register(ListasCorreos)