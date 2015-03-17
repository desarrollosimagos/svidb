#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from linea.models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response

from posiciones.autocomplete.widgets import *

class TiposFundamentosAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TiposFundamentosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(TiposFundamentos,TiposFundamentosAdmin)

class FundamentosAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(FundamentosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/eventos/linea/textareas.js')

admin.site.register(Fundamentos,FundamentosAdmin)

class ObjetivoespecificosAdmin(admin.ModelAdmin):
      list_display = ('fundamentos','numero','nombre',) #cambios
      list_display_links = ('fundamentos','numero','nombre',) #cambios
      def fundamentos(self, instance):
          return instance.fundamento.numero
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ObjetivoespecificosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/eventos/linea/textareas.js')

admin.site.register(Objetivoespecificos,ObjetivoespecificosAdmin)

class AccionesgeneralesAdmin(admin.ModelAdmin):
      list_display = ('fundamentos','objetivos','numero','nombre',) #cambios
      list_display_links = ('fundamentos','objetivos','numero','nombre',) #cambios
      def objetivos(self, instance):
          return instance.objetivoespecifico.numero
      def fundamentos(self, instance):
          return instance.objetivoespecifico.fundamento.numero
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(AccionesgeneralesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/eventos/linea/textareas.js')


admin.site.register(Accionesgenerales,AccionesgeneralesAdmin)

class AccionesespecificasAdmin(admin.ModelAdmin):
      list_display = ('fu','oe','ag','numero','nombre',) #cambios
      list_display_links = ('fu','oe','ag','numero','nombre',)
#acciones generales
#ints->accionesgenerale->numero
      def ag(self, instance):
          return instance.accionesgenerale.numero
#objetivos Generales
      def oe(self, instance):
          return instance.accionesgenerale.objetivoespecifico.numero
#Fundamentos
#ints->accionesgenerale->objetivoespecifico->fundamento->numero
      def fu(self, instance):
          return instance.accionesgenerale.objetivoespecifico.fundamento.numero
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(AccionesespecificasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/eventos/linea/textareas.js')

admin.site.register(Accionesespecificas,AccionesespecificasAdmin)

class TareasAdmin(admin.ModelAdmin):
      list_display = ('nombre','acciones',) #cambios
      list_display_links = ('nombre','acciones',)
      search_fields = ('nombre','acciones',)

admin.site.register(Tareas,TareasAdmin)
