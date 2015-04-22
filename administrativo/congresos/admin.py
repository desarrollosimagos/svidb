#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from congresos.models import *
from arbitraje.models import *
from actores.models import *
from django import forms
from django.contrib import admin
from posiciones.autocomplete.widgets import *
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response
from django.db.models import Q
from django.contrib.admin import SimpleListFilter
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext, ugettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from posiciones.autocomplete.widgets import *
import csv

from django.template import loader, Context

from import_export.admin import ImportExportModelAdmin

#admin.site.register(Directorios)

def Csv1(modeladmin, request, queryset):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename="listaParticipantes.csv"'

    writer = csv.writer(response)
    for i in queryset:
        writer.writerow([i.directorio.documentoidentidad,i.directorio.nombre.encode('utf-8', 'ignore'),i.directorio.apellido.encode('utf-8', 'ignore'),i.directorio.correo,i.directorio.estado])
    return response
	
Csv1.short_description = "Exportar Listados en CSV"

class participacioEventoAdmin(AutocompleteModelAdmin):
      actions = [Csv1,]
      list_filter = ('evento','estatu','directorio__estado')
      search_fields = ('directorio__documentoidentidad','directorio__nombre', 'directorio__apellido','directorio__correo')
      list_display = ('participanteCedula','participanteNombre','participanteApellido','participanteCorreo','participanteEstado','estatu',)
      related_search_fields = {
                'directorio': ('id','documentoidentidad','nombre',),
      }

admin.site.register(participacioEvento,participacioEventoAdmin)

admin.site.register(AportesEventos)
admin.site.register(TipoAportesEventos)
admin.site.register(AportesEventosConfiguracion)

class participacioEventoAporteAdmin(admin.ModelAdmin):
      search_fields = ('campo1',)
      list_display = ('evento','campo1','campo2','campo3','campo4',)

admin.site.register(participacioEventoAporte,participacioEventoAporteAdmin)

class participacioEventoVariosAdmin(ImportExportModelAdmin,admin.ModelAdmin):
      resource_class = participacioEventoVariosResource
      list_filter = ('evento','certificado','material','directorio__estado',)
      list_display = ('directorio','evento','certificado','material','ImprimirCertificado')
admin.site.register(participacioEventoVarios,participacioEventoVariosAdmin)



#class ActoresAdmin(admin.ModelAdmin):
#	class Media:
#		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

#admin.site.register(Actores,ActoresAdmin)
class TipomiembrosAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TipomiembrosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Tipomiembros,TipomiembrosAdmin)


class ProgramaCursosAdmin(admin.TabularInline):
      model = ProgramaCursos
      extra = 1


class EventosAdmin(AutocompleteModelAdmin):
      inlines = [ProgramaCursosAdmin,]
      related_search_fields = { 
                'biblio': ('id','autores','titulo',),
                'bancoaudios': ('id','descripcion','fecha'),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(EventosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Eventos,EventosAdmin)

class ModalidadsAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ModalidadsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Modalidads,ModalidadsAdmin)


class TabMensajeTrabajosAdmin(admin.TabularInline):
      model = MensajeTrabajosArbitraje
      extra = 1
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TabMensajeTrabajosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
		  
#class TabTrabajosArbitrosAdmin2(AutocompleteTabularInline):
class TrabajosAdminArbitros(admin.TabularInline):
      model = TrabajosArbitros
      extra = 1

class TabSeguimientoTrabajos(admin.TabularInline):
      model = SeguimientoTrabajos
      extra = 1

	  
class FiltroArbitros(SimpleListFilter):

     title = _('Filtro Arbitros')
     parameter_name = 'Arbitraje'
     def lookups(self, request, model_admin):
        return (
            ('1', _('sin arbitro')),
            ('2', _('con arbitro')),
            ('3', _('con arbitro sin estatus')),
            ('4', _('con arbitro con estatus aprobado')),
            ('5', _('con arbitro con estatus rechazado')),
            ('6', _('con arbitro con estatus arbitrando')),
        )
     def queryset(self, request, queryset):
        if self.value() == '1':
           return queryset.filter(trabajosarbitros__arbitro__isnull=True)
        if self.value() == '2':
           return queryset.filter(trabajosarbitros__arbitro__isnull=False)
        if self.value() == '3':
           return queryset.filter(trabajosarbitros__estatu=0)
        if self.value() == '4':
           return queryset.filter(trabajosarbitros__estatu=1)
        if self.value() == '5':
           return queryset.filter(trabajosarbitros__estatu=2)
        if self.value() == '6':
           return queryset.filter(trabajosarbitros__estatu=3)


class TrabajoscongresosAdmin(ImportExportModelAdmin,AutocompleteModelAdmin):
      resource_class = TrabajoscongresosResource
      pass
      inlines = [TrabajosAdminArbitros,TabSeguimientoTrabajos,]
      list_filter = ('evento','modalidad','tematicas','accespecifi','presento','impreso','armado','entregado','devueto','estatu',FiltroArbitros)
      search_fields = ('titulo','directorio__nombre', 'directorio__apellido','directorio__correo','directorio__documentoidentidad',)
      list_display = ('titulo_html','directorio','presento','impreso','armado','entregado','devueto','estatu',)
      list_editable = ('presento','impreso','armado','entregado','devueto')
      #titulo.allow_tags = True      
      related_search_fields = { 
                'coautores':  ('documentoidentidad','nombre','apellido',),
                'palabrasclave':  ('palabrasclave',),
                'colectivos': ('nombre_completo',),
                'evento': ('nombre',),
                'directorio': ('documentoidentidad','nombre','apellido',),
      }
      fieldsets = [
            ('Datos Generales',               {'fields': ['presento','impreso','armado','entregado','devueto','evento','titulo','resumen','modalidad','fundamento','objetivoespecifico','accionesgenerale','accespecifi','tematicas','palabrasclave','ambitoaccion']}),
            ('Vinculación con Actores', {'fields': ['directorio','coautores','colectivos'],}),
            ('Datos de Validación', {'fields': ['userupdate','estatu'],}),
        ]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TrabajoscongresosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/eventos/linea/textareas.js')
admin.site.register(Trabajoscongresos,TrabajoscongresosAdmin)


class GrupotrabajocongresosAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(GrupotrabajocongresosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Grupotrabajocongresos,GrupotrabajocongresosAdmin)

class DetalleGrupotrabajosAdmin(admin.TabularInline):
    model = RelacionGrupoTrabajoAccionEspecifica
    extra=1

#-===========================================================================


class GrupotrabajosAdmin(admin.ModelAdmin):
      inlines = [DetalleGrupotrabajosAdmin]
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(GrupotrabajosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Grupotrabajos,GrupotrabajosAdmin)


class RelacionGrupoTrabajoAccionEspecificaAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RelacionGrupoTrabajoAccionEspecificaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(RelacionGrupoTrabajoAccionEspecifica,RelacionGrupoTrabajoAccionEspecificaAdmin)


class MiembrosgrupotrabajosAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(MiembrosgrupotrabajosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(Miembrosgrupotrabajos,MiembrosgrupotrabajosAdmin)


admin.site.register(TipoEventos)

class TematicasAdmin(ImportExportModelAdmin):
    resource_class = TematicasResource
    pass
admin.site.register(Tematicas,TematicasAdmin)


admin.site.register(TipoLogistica)

class MiembrosLogisticaAdmin(admin.TabularInline):
    model = MiembrosLogistica
    extra=1
class CoordinadorLogisticaAdmin(AutocompleteModelAdmin):
      list_filter = ('tipo',)
      search_fields = ('directorio__nombre', 'directorio__apellido','directorio__correo','directorio__documentoidentidad',)
      list_display = ('tipo','directorio',)
      related_search_fields = { 
                'directorio':  ('id','documentoidentidad','nombre','apellido',),
      }

admin.site.register(CoordinadorLogistica,CoordinadorLogisticaAdmin)

class MiembrosLogisticaAdmin(AutocompleteModelAdmin):
      list_filter = ('tipo',)
      search_fields = ('evento','tipo','coordinacion',)
      list_display = ('evento','tipo','coordinacion','directorio',)
      related_search_fields = { 
                'directorio':  ('id','documentoidentidad','nombre','apellido',),
      }
admin.site.register(MiembrosLogistica,MiembrosLogisticaAdmin)


class SeguimientoTrabajosAdmin(AutocompleteModelAdmin):
      list_filter = ('impreso','armado','entregado','devueto',)
      list_display = ('trabajo','impreso','armado','entregado','devueto',)
      related_search_fields = {
                'trabajo': ('id','titulo',),
      }

admin.site.register(SeguimientoTrabajos,SeguimientoTrabajosAdmin)
