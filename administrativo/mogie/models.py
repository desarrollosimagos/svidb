#!/usr/bin/python -u
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from perfil.models import *


class ConfiguracionIndexPatrocinador(models.Model):
    patrocinador = models.CharField(max_length=150,verbose_name='Nombre Completo')
    siglas = models.CharField(max_length=20,verbose_name='Siglas')
    url = models.TextField(validators=[URLValidator()])
    icono = models.CharField(max_length=150,verbose_name='icono')
    fondo = models.CharField(max_length=150,verbose_name='fondo')
    class Meta:
        verbose_name_plural='Configuracion Patrocinador en Index'
        verbose_name='Configuracion Patrocinador en Index'
    def __unicode__(self):
        return u"%s" %(self.patrocinador)
        
class ExtensionPerfilUsuario(models.Model):
    perfil = models.OneToOneField(PerfilPublico,verbose_name='Perfil')
    foto = models.ImageField(upload_to='fotos',null=True, blank=True)
    facebook = models.CharField(max_length=150,verbose_name='Facebook',blank=True,null=True)
    instagram = models.CharField(max_length=150,verbose_name='Instagram',blank=True,null=True)
    twitter = models.CharField(max_length=150,verbose_name='Twitter',blank=True,null=True)
    google = models.CharField(max_length=150,verbose_name='Google',blank=True,null=True)
    class Meta:
        verbose_name_plural='Extension de Perfil'
        verbose_name='Extension de Perfil'
    def __unicode__(self):
        return u"%s" %(self.perfil)
        
class ComentariosModulo(models.Model):
    perfil = models.ForeignKey(ExtensionPerfilUsuario,verbose_name='Perfil')
    comentario = models.CharField(max_length=150,verbose_name='Comentarios')
    class Meta:
        verbose_name_plural='Comentarios'
        verbose_name='Comentarios'
    def __unicode__(self):
        return u"%s" %(self.perfil)
    
		