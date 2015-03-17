#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from perfil.models import *
from actores.models import *
from congresos.models import *
from posiciones.autocomplete.widgets import *
from django.shortcuts import render_to_response, get_object_or_404,HttpResponseRedirect

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter

from perfil.forms import *


import csv

from django.template import loader, Context

class TrabajosFiltro(SimpleListFilter):
     title = _('Filtro Trabajos')
     parameter_name = 'Trabajos'
     def lookups(self, request, model_admin):
        return (
            ('2', _('sin trabajos registrados en eventos activos')),
            ('3', _('con trabajos registrados en eventos activos')),
        )
     def queryset(self, request, queryset):
        if self.value() == '1':
           return queryset.exclude(perfilmodulos__activo=True)
        if self.value() == '2':
           per = Directorios.objects.filter(trabajoscongresos__evento__estatu=0)
           return queryset.exclude(persona__in=per)
        if self.value() == '3':
           per = Directorios.objects.filter(trabajoscongresos__evento__estatu=0)
           return queryset.filter(persona__in=per)
        if self.value() == '4':
           per = Directorios.objects.filter(participacioevento__evento__estatu=0)
           return queryset.exclude(persona__in=per)
        if self.value() == '5':
           per = Directorios.objects.filter(participacioevento__evento__estatu=0)
           return queryset.filter(persona__in=per)
		   
class UsuariosFiltro(SimpleListFilter):
     title = _('Filtro Permisos')
     parameter_name = 'sin validar'
     def lookups(self, request, model_admin):
        return (
            ('1', _('sin validar')),
            ('2', _('Validados')),
        )
     def queryset(self, request, queryset):
        if self.value() == '1':
           return queryset.exclude(perfilmodulos__activo=True)
        if self.value() == '2':
           return queryset.filter(perfilmodulos__activo=True)
		   
class PreinscripcionFiltro(SimpleListFilter):
     title = _('Filtro Inscripciones')
     parameter_name = 'Pre-inscritos'
     def lookups(self, request, model_admin):
        return (
            ('4', _('sin pre-inscribirse en eventos activos')),
            ('5', _('con pre-inscripcion en eventos activos')),
        )
     def queryset(self, request, queryset):
        if self.value() == '1':
           return queryset.exclude(perfilmodulos__activo=True)
        if self.value() == '2':
           per = Directorios.objects.filter(trabajoscongresos__evento__estatu=0)
           return queryset.exclude(persona__in=per)
        if self.value() == '3':
           per = Directorios.objects.filter(trabajoscongresos__evento__estatu=0)
           return queryset.filter(persona__in=per)
        if self.value() == '4':
           per = Directorios.objects.filter(participacioevento__evento__estatu=0)
           return queryset.exclude(persona__in=per)
        if self.value() == '5':
           per = Directorios.objects.filter(participacioevento__evento__estatu=0)
           return queryset.filter(persona__in=per)

def Csv1(modeladmin, request, queryset):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename="listaCorreos.csv"'

    writer = csv.writer(response)
#    rows = queryset.exclude(perfilmodulos__activo=True)
    for i in queryset:
        writer.writerow([i.persona.correo])
    return response
	
Csv1.short_description = "Exportar Correos en CSV"

class TabPerfilModulosAdmin(admin.TabularInline):
      model = PerfilModulos
      extra = 1
	  
class TabPerfilSubModulosAdmin(admin.TabularInline):
      model = PerfilSubModulos
      extra = 1

class PerfilPublicoAdmin(AutocompleteModelAdmin):
      list_filter=[TrabajosFiltro,UsuariosFiltro,PreinscripcionFiltro]
      actions = [Csv1,]
      inlines = [TabPerfilModulosAdmin,TabPerfilSubModulosAdmin,]
#      list_filter = ('evento','estatu','coordinador','modalidad','tematicas','accespecifi',)
      list_display = ('persona','user',)
      search_fields = ('persona__documentoidentidad','persona__correo',)
      related_search_fields = { 
                'persona': ('documentoidentidad','nombre',),
                'user': ('username',),
      }
admin.site.register(PerfilPublico,PerfilPublicoAdmin)

admin.site.register(TipoSolicitud)

class SeguimientoAdmin(admin.ModelAdmin):
      list_display = ('solicitud','persona','fecha',)
	  
admin.site.register(Seguimiento,SeguimientoAdmin)

class TabSeguimientoAdmin(admin.TabularInline):
      model = Seguimiento
      extra = 1
      def save_model(self, request, obj, form, add):
        perfil = Perfil.objects.get(user = request.user)
        obj.persona = perfil.persona
        obj.save()

class SistemaSolicitudesAdmin(AutocompleteModelAdmin):
      list_filter = ('tipoSolicitud','asunto','prioridad','estatu',)
      list_display = ('remi','tipoSolicitud','asunto','prioridad','estatu')
      inlines = [TabSeguimientoAdmin,]
      add_form = SolicitudesNewForm
      related_search_fields = { 
                'remi': ('id','documentoidentidad','nombre','apellido'),
                'destino': ('documentoidentidad','nombre','apellido','id'),
                'destinoinst': ('nombre','nombre_completo','id'),
                'personasinvol': ('documentoidentidad','nombre','apellido','id'),
                'instituinvol': ('nombre','nombre_completo','id'),
                'especies': ('id','nombre','subtipo__nombre'),
                'areas': ('id','nombre',),
      }
      def get_form(self, request, obj=None, **kwargs):
           """
           Use special form during user creation
           """
           defaults = {}
           if obj is None:
               defaults.update({
                   'form': self.add_form,
                   'fields': ('remi','tipoSolicitud','destino','asunto','mensaje','personasinvol','prioridad','estatu'),
               })
           defaults.update(kwargs)
           return super(SistemaSolicitudesAdmin, self).get_form(request, obj, **defaults)
#      def formfield_for_foreignkey(self, db_field, request, **kwargs):
#          if db_field.name == "userupdate":
#             kwargs["queryset"] = User.objects.filter(id=request.user.id)
#          return super(TipoTaxonAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
      def save_model(self, request, obj, form, add):
        obj.save()
		

admin.site.register(SistemaSolicitudes,SistemaSolicitudesAdmin)



class ModulosPublicosAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'persona': ('documentoidentidad','nombre',),
      }
      list_filter = ('is_admmin','activo','paneles__panel',)
      list_display = ('logo','paneles','modulo','is_admmin','activo','posicion',)

admin.site.register(ModulosPublicos,ModulosPublicosAdmin)

class PerfilModulosAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'perfil': ('persona__id','persona__documentoidentidad','persona__nombre','persona__apellido'),
      }
      search_fields = ('perfil__persona__nombre','perfil__persona__apellido','perfil__persona__documentoidentidad','perfil__persona__correo','perfil__user__username')
      list_filter = ('modulos__paneles__panel','modulos__modulo','ver','add','edit','activo',)
      list_display = ('perfil','modulos','ver','add','edit','activo',)

admin.site.register(PerfilModulos,PerfilModulosAdmin)

class PerfilSubModulosAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'perfil': ('persona__id','persona__documentoidentidad','persona__nombre','persona__apellido'),
      }
      search_fields = ('perfil__persona__nombre','perfil__persona__apellido','perfil__persona__documentoidentidad','perfil__persona__correo','perfil__user__username')
      list_filter = ('submodulos__modulos__modulo','ver','add','edit','activo',)
      list_display = ('perfil','submodulos','ver','add','edit','activo',)
admin.site.register(PerfilSubModulos,PerfilSubModulosAdmin)

admin.site.register(SeccionesPanelPublico)


class SubModulosPublicosAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'persona': ('documentoidentidad','nombre',),
      }
      list_filter = ('is_admmin','activo','modulos__modulo','modulos__paneles__panel',)
      list_display = ('logo','modulos','titulo','is_admmin','activo','posicion',)
admin.site.register(SubModulosPublicos,SubModulosPublicosAdmin)


def cambiarEstadoValidacionTrue(modeladmin, request, queryset):
    queryset.update(estado=True)
cambiarEstadoValidacionTrue.short_description = "Cambiar estado Activo"

def cambiarEstadoValidacionFalse(modeladmin, request, queryset):
    queryset.update(estado=False)
cambiarEstadoValidacionFalse.short_description = "Cambiar estado a Inactivo"

def enviarNotificacion(modeladmin, request, queryset):
#    return render_to_response('correos/correo.html',{'query':queryset})
     for i in queryset:
         subject, from_email, to = 'SVIDB Código de Verificación', settings.EMAIL_HOST_USER, i.usuario.persona.correo
         text_content = 'SVIDB Código de Verificación'
         d= settings.URL_SET_SITE
         ctx_dict = {'salt': i.codigo,'d': d}
         html_content= render_to_string('correos/plantillas/validacion.txt',ctx_dict)
         msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
         msg.attach_alternative(html_content, "text/html")
         msg.send()
     return HttpResponseRedirect("/manager/perfil/validaciones/")
	 
class ValidacionesSinCompletar(SimpleListFilter):
     title = _('Validaciones sin completar')
     parameter_name = 'estado'
     def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('1', _('sin finalizar')),
        )
     def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or 'other')
        # to decide how to filter the queryset.
        if self.value() == '1':
           per = PerfilPublico.objects.filter(perfilmodulos__activo=True)
           return queryset.exclude(usuario__in=per)

class validacionesAdmin(AutocompleteModelAdmin):
      actions = [cambiarEstadoValidacionTrue,cambiarEstadoValidacionFalse,enviarNotificacion]
      related_search_fields = { 
                'usuario': ('persona__documentoidentidad','persona__nombre','persona__correo',),
      }
      list_filter = ('estatu','estado',ValidacionesSinCompletar)
      list_display = ('usuario','codigo','estatu','fecha','estado',)
admin.site.register(validaciones,validacionesAdmin)


admin.site.register(GruposPermisos)

admin.site.register(DetalleGruposPermisos)
