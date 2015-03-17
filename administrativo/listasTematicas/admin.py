#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from listasTematicas.models import *
from especies.models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response

from posiciones.autocomplete.widgets import *

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpagricolasAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpagricolasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 
admin.site.register(Spagricolas,SpagricolasAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpagricolamodsAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpagricolamodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Spagricolamods,SpagricolamodsAdmin)


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpaprovechablesAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpaprovechablesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Spaprovechables,SpaprovechablesAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpaprovechablemodsAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpaprovechablemodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Spaprovechablemods,SpaprovechablemodsAdmin)


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpaprovechamientosustentablesAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpaprovechamientosustentablesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Spaprovechamientosustentables,SpaprovechamientosustentablesAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpaprovechamientosustentablemodsAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpaprovechamientosustentablemodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Spaprovechamientosustentablemods,SpaprovechamientosustentablemodsAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

admin.site.register(TipoAprovechable)
#admin.site.register(Spsaludtipos)
admin.site.register(TipoAgricola)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpexoticasAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      filter_horizontal = ('exotica',)
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpexoticasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Spexoticas,SpexoticasAdmin)


#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpexoticamodsAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpexoticamodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Spexoticamods,SpexoticamodsAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SppeligrosAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SppeligrosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Sppeligros,SppeligrosAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SppeligromodsAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SppeligromodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Sppeligromods,SppeligromodsAdmin)

admin.site.register(SprepresentativaasMods)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SprepresentativaasAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SprepresentativaasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
#admin.site.register(Sprepresentativaas,SprepresentativaasAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpsaludsAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      filter_horizontal = ('tipo',)
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpsaludsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Spsaluds,SpsaludsAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpsaludtiposAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpsaludtiposAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Spsaludtipos,SpsaludtiposAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SpsaludmodsAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SpsaludmodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Spsaludmods,SpsaludmodsAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SptraficosAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SptraficosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Sptraficos,SptraficosAdmin)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class SptraficomodsAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'especie': ('id',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(SptraficomodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Sptraficomods,SptraficomodsAdmin)




