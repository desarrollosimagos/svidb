#!/usr/bin/python -u
# -*- coding: utf-8 -*-
import os
from especies.models import *
from mapas.models import Colaboradorespersonas
from actores.models import *
from listasTematicas.models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response

from posiciones.autocomplete.widgets import *

admin.site.register(Estatuspeligros)

admin.site.register(tipoAprovechamientoSustentable)

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u'<table><tr><td>Normal - redimencion: 300 x 400</td></tr><tr><td><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td width="15" background="/media/imgs/esqsi.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latsup.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqsd.png" style="background-repeat:no-repeat;"></td></tr><tr><td width="15" background="/media/imgs/latizq.png" style="background-repeat:repeat-y;"></td><td><a href="%s" target="_blank"><img src="%s" alt="%s" width="300px" height="400px" /></a></td><td width="32" background="/media/imgs/latder.png" style="background-repeat:repeat-y;"></td></tr><tr><td width="15" background="/media/imgs/esqid.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latinf.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqii.png" style="background-repeat:no-repeat;"></td></tr></table>  </td></tr></table>' % \
                (image_url, image_url, file_name))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

class AdminImageWidget_2(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)

            splitted_filename = list(os.path.splitext(file_name))
            splitted_filename.insert(1, '.59_59')
            file_nombre_59_59 = ''.join(splitted_filename)
            
            splitted_filename = list(os.path.splitext(file_name))
            splitted_filename.insert(1, '.118_118')
            file_nombre_118_118 = ''.join(splitted_filename)

            splitted_filename = list(os.path.splitext(file_name))
            splitted_filename.insert(1, '.157_118')
            file_nombre_157_118 = ''.join(splitted_filename)

            output.append(u'<table><tr><td>Normal - redimencion: 300 x 400</td><td>157 x 118</td><td>118 x 118</td><td>59 x 59</td><tr><tr><td><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td width="15" background="/media/imgs/esqsi.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latsup.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqsd.png" style="background-repeat:no-repeat;"></td></tr><tr><td width="15" background="/media/imgs/latizq.png" style="background-repeat:repeat-y;"></td><td><a href="%s" target="_blank"><img src="%s" alt="%s" width="300px" height="400px" /></a></td><td width="32" background="/media/imgs/latder.png" style="background-repeat:repeat-y;"></td></tr><tr><td width="15" background="/media/imgs/esqid.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latinf.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqii.png" style="background-repeat:no-repeat;"></td></tr></table>  </td><td><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td width="15" background="/media/imgs/esqsi.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latsup.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqsd.png" style="background-repeat:no-repeat;"></td></tr><tr><td width="15" background="/media/imgs/latizq.png" style="background-repeat:repeat-y;"></td><td><a href="/media/%s" target="_blank"><img src="/media/%s" alt="%s" /></a></td><td width="32" background="/media/imgs/latder.png" style="background-repeat:repeat-y;"></td></tr><tr><td width="15" background="/media/imgs/esqid.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latinf.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqii.png" style="background-repeat:no-repeat;"></td></tr></table></td><td><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td width="15" background="/media/imgs/esqsi.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latsup.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqsd.png" style="background-repeat:no-repeat;"></td></tr><tr><td width="15" background="/media/imgs/latizq.png" style="background-repeat:repeat-y;"></td><td><a href="/media/%s" target="_blank"><img src="/media/%s" alt="%s" /></a></td><td width="32" background="/media/imgs/latder.png" style="background-repeat:repeat-y;"></td></tr><tr><td width="15" background="/media/imgs/esqid.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latinf.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqii.png" style="background-repeat:no-repeat;"></td></tr></table></td><td><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td width="15" background="/media/imgs/esqsi.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latsup.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqsd.png" style="background-repeat:no-repeat;"></td></tr><tr><td width="15" background="/media/imgs/latizq.png" style="background-repeat:repeat-y;"></td><td><a href="/media/%s" target="_blank"><img src="/media/%s" alt="%s" /></a></td><td width="32" background="/media/imgs/latder.png" style="background-repeat:repeat-y;"></td></tr><tr><td width="15" background="/media/imgs/esqid.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latinf.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqii.png" style="background-repeat:no-repeat;"></td></tr></table></td></tr></table>' % \
                (image_url, image_url, file_name, file_nombre_157_118, file_nombre_157_118, file_nombre_157_118,file_nombre_118_118, file_nombre_118_118, file_nombre_118_118,file_nombre_59_59, file_nombre_59_59, file_nombre_59_59))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class TipoTaxonAdmin(admin.ModelAdmin):
      list_display =('id','nombre','tiptax','estatu',)
      list_editable = ('estatu',)
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TipoTaxonAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(TipoTaxon,TipoTaxonAdmin)

#========================================================================================

class RSpagricolasAdmin(admin.TabularInline):
      model = Spagricolas
      extra = 1
      max_num = 1
      fieldsets = [
            ('Datos Generales',{'fields': ['especie','impactoagricola','alternativas','tipo','userupdate','estatu']}),
      ]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RSpagricolasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 

class RSpaprovechablesAdmin(admin.TabularInline):
      model = Spaprovechables
      extra = 1
      max_num = 1
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RSpaprovechablesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 

class RSpaprovechamientosustentablesAdmin(admin.TabularInline):
      model = Spaprovechamientosustentables
      extra = 1
      max_num = 1
      fieldsets = [
            ('Datos Generales',{'fields': ['especie','usoaprovecha','tipoaprosus','userupdate','estatu']}),
      ]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RSpaprovechamientosustentablesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 


class RSpexoticasAdmin(admin.TabularInline):
      model = Spexoticas
      extra = 1
      max_num = 1
      fieldsets = [
            ('Datos Generales',{'fields': ['especie','impacto','esppeligr','metodoinic','inicontrol','exotica','userupdate','estatu']}),
      ]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RSpexoticasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 

class RSppeligrosAdmin(admin.TabularInline):
      model = Sppeligros
      extra = 1
      max_num = 1
      fieldsets = [
            ('Datos Generales',{'fields': ['especie','amenazas','metoconserv','estatuspeligro','userupdate','estatu']}),
      ]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RSppeligrosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 

class RSprepresentativaasAdmin(admin.TabularInline):
      model = Sprepresentativaas
      extra = 1
      max_num = 1
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RSprepresentativaasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 

class RSpsaludsAdmin(admin.TabularInline):
      model = Spsaluds
      extra = 1
      max_num = 1
      fieldsets = [
            ('Datos Generales',{'fields': ['especie','importanciasalud','metodoinic','metocontrol','tipo','userupdate','estatu']}),
      ]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RSpsaludsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 

class RSptraficosAdmin(admin.TabularInline):
      model = Sptraficos
      extra = 1
      max_num = 1
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RSptraficosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
		
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
		  

class EspeciesAdmin(AutocompleteModelAdmin):
      fieldsets = [
            ('Datos del Taxon',{'fields': ['nombre','autorespecie','nombrecomun','otrosnombrec','comentariotaxonomico','filogenia','endemica','extinto','subtipo','otroNombreNivel','taxonrelax','detalletaxon']}),
            ('Vinculación con Actores', {'fields': ['direct','actor'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      related_search_fields = { 
                'taxonrelax': ('id','nombre','subtipo__nombre'),
                'subtipo': ('id','nombre',),
                'actor': ('id','nombre','documentoidentidad',),
                'direct': ('id','nombre',),
                'detalletaxon': ('id',),
      }
      inlines =[ColaboradorespersonasAdmin]
      list_filter = ('subtipo',)
      def relacion_id(self, instance):
          return instance.taxonrelax.id
      def st_nombre(self, instance):
          return instance.subtipo.nombre
      def st_id(self, instance):
          return instance.subtipo.id
      list_display = ('st_id','st_nombre','relacion_id','taxonrelax','id','nombre','detalletaxon')
      search_fields = ('nombre','nombrecomun', 'otrosnombrec','comentariotaxonomico','autorespecie')
#      def formfield_for_dbfield(self, db_field, **kwargs):
#          if db_field.name == 'pathimg':
#             request = kwargs.pop("request", None)
#             kwargs['widget'] = AdminImageWidget
#             return db_field.formfield(**kwargs)
#          return super(EspeciesAdmin,self).formfield_for_dbfield(db_field, **kwargs)
#      list_display = ('show_thumb','nombre')

      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(EspeciesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
#        js = ('/static/admin/js/SelectBox.js','/static/admin/js/SelectBox.js')
#        js=('/static/admin/js/SelectFilter2.js','/static/admin/js/SelectFilter2.js')
#        js = ('','js/SelectFilter2.js')

admin.site.register(Taxon,EspeciesAdmin)

#admin.site.register(SubTipoTaxon)


class DetalleTaxonAdmin(AutocompleteModelAdmin):
      fieldsets = [
            ('Taxonomia y Evolución',{'fields': ['descripcionmorfologica','distribucion','habitad','habitos','reproduccion','particularidades','iniconserv','aspectoslegales']}),
            ('Ubicación', {'fields': ['bioregion'],}),
            ('Datos Transversales', {'fields': ['bancoaudio','mapas','docasocia','glosario','maniscultura','enlaces'],}),
            ('Bibliografia', {'fields': ['bibliografia','url'],}),
            ('Criterio Socio-Ambiental', {'fields': ['esptraf','espaprove','espsalud','esppeligr','espexot','espagrico'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      related_search_fields = { 
                'bancoaudio': ('id','descripcion',),
                'mapas': ('id','nombre',),
                'docasocia': ('id','autores','titulo',),
                'glosario': ('id','nombre',),
                'maniscultura': ('id','titulo',),
                'enlaces': ('id','enlaces',),
                'bibliografia': ('id','autores','titulo',),
                'url': ('id','enlaces',),
#                'taxon': ('id','nombre','subtipo__nombre',),

      }
      search_fields = ('descripcionmorfologica','habitad', 'distribucion','habitos','particularidades','aspectoslegales','reproduccion','iniconserv')
      def trafico(self, instance):
          return instance.esptraf
      trafico.boolean = True
      def aprovec(self, instance):
          return instance.espaprove
      aprovec.boolean = True
      def salud(self, instance):
          return instance.espsalud
      salud.boolean = True
      def peligro(self, instance):
          return instance.esppeligr
      peligro.boolean = True
      def exotica(self, instance):
          return instance.espexot
      exotica.boolean = True
      def agricola(self, instance):
          return instance.espagrico
      agricola.boolean = True
      def genero(self, instance):
          return instance.taxon.taxonrelax.nombre

      list_filter = ('esptraf','espaprove','espsalud','esppeligr','espexot','espagrico','estatu',)
#      search_fields = ('Taxones',)
#      list_display = ('genero','taxon', 'trafico','aprovec','salud','peligro','exotica','agricola','estatu',)
      list_display = ('Taxones','VerTaxon','Estatus',)
#      list_max_show_all = 25
      list_per_page=25
      filter_horizontal = ('bancoaudio',)
      inlines = [RSpexoticasAdmin,RSppeligrosAdmin,RSpsaludsAdmin,RSptraficosAdmin,RSpagricolasAdmin,RSpaprovechamientosustentablesAdmin]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(DetalleTaxonAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(DetalleTaxon,DetalleTaxonAdmin)


class TipoexoticasAdmin(admin.ModelAdmin):
      list_display = ('nombre','tipo','estatu')
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TipoexoticasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Tipoexoticas,TipoexoticasAdmin)

class MatrixRelacionTaxonAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "imperio":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Imperio')
          if db_field.name == "reino":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Reino')
          if db_field.name == "subreino":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Subreino')
          if db_field.name == "infrareino":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Infrareino')
          if db_field.name == "superphylum":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Superphylum')
          if db_field.name == "phylum":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Phylum')
          if db_field.name == "subphylum":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Subphylum')
          if db_field.name == "infraphylum":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Infraphylum')
          if db_field.name == "superclase":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Superclase')
          if db_field.name == "clase":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Clase')
          if db_field.name == "subclase":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Subclase')
          if db_field.name == "infraclase":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Infraclase')
          if db_field.name == "superorden":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Superorden')
          if db_field.name == "orden":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Orden')
          if db_field.name == "suborden":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Suborden')
          if db_field.name == "infraorden":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Infraorden')
          if db_field.name == "superfamilia":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Superfamilia')
          if db_field.name == "familia":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Familia')
          if db_field.name == "subfamilia":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Subfamilia')
          if db_field.name == "infrafamilia":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Infrafamilia')
          if db_field.name == "tribu":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Tribu')
          if db_field.name == "subtribu":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Subtribu')
          if db_field.name == "genero":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Género')
          if db_field.name == "subgenero":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Subgénero')
          if db_field.name == "grex":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Grex')
          if db_field.name == "especie":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Especie')
          if db_field.name == "subespecie":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Subespecie')
          if db_field.name == "variedad":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Variedad')
          if db_field.name == "raza":
             kwargs["queryset"] = Taxon.objects.filter(subtipo__nombre='Raza')
          return super(MatrixRelacionTaxonAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(MatrixRelacionTaxon,MatrixRelacionTaxonAdmin)

