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
from models import *


admin.site.register(ConfiguracionIndexPatrocinador)

admin.site.register(ExtensionPerfilUsuario)

admin.site.register(ComentariosModulo)

admin.site.register(ColaboracionConf)

admin.site.register(ValoresDefectoSeleccion)

admin.site.register(DetalleColaboracionConf)

admin.site.register(ColaboracionPersonas)

admin.site.register(ColaboracionInformacion)