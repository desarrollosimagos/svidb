#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from gestion.models import *
from datetime import datetime
from import_export import resources
from import_export import fields


# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=180)
    cod = models.CharField(max_length=135, blank=True,verbose_name='Codigo')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'pais'
        verbose_name_plural='Pais'
        verbose_name='País'
    def __unicode__(self):
        return u"%s  %s" %(self.nombre, self.cod)

class Estados(models.Model):
    nombre = models.CharField(max_length=300)
    cod = models.CharField(max_length=135, blank=True,verbose_name='Codigo')
    pai = models.ForeignKey(Pais,verbose_name='País')
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    class Meta:
        db_table = u'estados'
        verbose_name_plural='Estados'
        verbose_name='Estados'
    def __unicode__(self):
        return u"%s  %s" %(self.nombre, self.cod)
        
class EstadosResource(resources.ModelResource):
    class Meta:
        model = Estados
        fields = ('nombre',)

class Municipios(models.Model):
    nombre = models.CharField(max_length=300)
    cod = models.CharField(max_length=135, blank=True,verbose_name='Codigo')
    estado = models.ForeignKey(Estados,verbose_name='Estado')
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    class Meta:
        db_table = u'municipios'
        verbose_name_plural='Municipios'
        verbose_name='Municipios'
    def __unicode__(self):
        return u"%s  %s" %(self.nombre, self.cod)
        
class MunicipiosResource(resources.ModelResource):
    class Meta:
        model = Municipios
        fields = ('nombre',)

class Parroquias(models.Model):
    nombre = models.CharField(max_length=360)
    cod = models.CharField(max_length=135, blank=True,verbose_name='Codigo')
    municipio = models.ForeignKey(Municipios,verbose_name='Municipio')
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    class Meta:
        db_table = u'parroquias'
        verbose_name_plural='Parroquias'
        verbose_name='Parroquias'
    def __unicode__(self):
        return u"%s %s" %(self.nombre, self.cod)
        
class ParroquiasResource(resources.ModelResource):
    class Meta:
        model = Parroquias
        fields = ('nombre',)


