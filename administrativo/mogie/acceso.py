#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render_to_response, get_object_or_404,HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from congresos.models import Eventos,Trabajoscongresos,participacioEvento
from django.contrib.auth.models import User
from perfil.models import PerfilPublico,ModulosPublicos,PerfilModulos
from actores.models import Directorios,Bancoaudiovisuals,Bibliotecas
from mogie.models import *

def accesoValidacion(correo):

    try:
        usuarios = User.objects.get(username=correo)
    except User.DoesNotExist:
        usuarios = None

    try:
        perfil = PerfilPublico.objects.get(user=usuarios)
    except PerfilPublico.DoesNotExist:
        perfil = None

    if perfil == None:
       personas_id= None
    else:
       personas_id=perfil

    try:
        extension =  ExtensionPerfilUsuario.objects.get(perfil=personas_id)
    except ExtensionPerfilUsuario.DoesNotExist:
        extension = None
    return extension,perfil
    
