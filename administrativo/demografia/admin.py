#!/usr/bin/python -u
# -*- coding: utf-8 -*-
#from posiciones.models import *
from demografia.models import *
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response

from posiciones.autocomplete.widgets import *

class PaisAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(PaisAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Pais,PaisAdmin)

class EstadosAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(EstadosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Estados,EstadosAdmin)

class MunicipiosAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(MunicipiosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Municipios,MunicipiosAdmin)

class ParroquiasAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ParroquiasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Parroquias,ParroquiasAdmin)



