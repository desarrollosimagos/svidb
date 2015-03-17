#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from gestion.models import *
from documentos.models import *
from inicio.models import *
from django import forms
from django.contrib import admin

from posiciones.autocomplete.widgets import *

#=================================================================================================
class LicenciasAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(LicenciasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Licencias,LicenciasAdmin)





