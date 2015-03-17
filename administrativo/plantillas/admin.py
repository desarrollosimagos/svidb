#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.contrib import admin
from plantillas.models import *

admin.site.register(Templates)

class TemplatesEventosAdmin(admin.ModelAdmin):
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')
admin.site.register(TemplatesEventos)
admin.site.register(TemplatesInfoLateral)