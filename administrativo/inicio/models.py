#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models

from areas.models import *

from os import path
import Image

TINY_SIZE = (80,80)


from django.conf import settings

from django.contrib import admin
from datetime import datetime


#class Actoresorganismosads(models.Model):
#    actore = models.ForeignKey(Actores, null=True, blank=True)
#    organismoadscrito = models.ForeignKey(Organismoadscritos, null=True, db_column='organismoAdscrito_id', blank=True)
#    update = models.DateTimeField(default=datetime.now(),editable = False)
#    userupdate = models.ForeignKey(User,verbose_name='Usuario')
#    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
#    class Meta:
#        db_table = u'actoresOrganismosAds'
#        verbose_name_plural='Relación Actores Organismos Adscritos'
#        verbose_name='Relación Actores Organismos Adscritos'
#    def __unicode__(self):
#        return u"%s <=> %s" %(self.actore.nombre, self.organismoadscrito.name)

class Tipocolaboradors(models.Model):
    nombre = models.CharField(max_length=300, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'tipoColaboradors'
        verbose_name_plural='Funciones Equipos'
        verbose_name='Funciones Equipos'
        #app_label = 'Construccion_Colectiva'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
class Tipocolaboracion(models.Model):
    nombre = models.CharField(max_length=300, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'tipoColaboracion'
        verbose_name_plural='Tipo de Colaboración'
        verbose_name='Tipo de Colaboración'
        #app_label = 'Construccion_Colectiva'
    def __unicode__(self):
        return u"%s" %(self.nombre)		

class Colaboradoresinstitutes(models.Model):
    actore = models.ForeignKey(Actores, null=True, blank=True,verbose_name='Colectivo')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'colaboradoresInstitutes'
        verbose_name_plural='Colectivos Colaboradores'
        verbose_name='Colectivos Colaboradores'
        #app_label = 'Construccion_Colectiva'
    def __unicode__(self):
        return u"%s" %(self.actore)

class Equipos(models.Model):
    tipocolaborador = models.ManyToManyField(Tipocolaboradors, null=True, db_column='tipoColaborador_id', blank=True,verbose_name='Funciones')
    directorio = models.ForeignKey(Directorios, null=True, blank=True,verbose_name='Personas')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    escoord = models.BooleanField(db_column='iscoord',verbose_name='Coordinador')
    class Meta:
        db_table = u'equipos'
        verbose_name_plural='Equipo SVIDB'
        verbose_name='Equipo SVIDB'
        #app_label = 'Construccion_Colectiva'
    def funciones(self):
        return ', '.join([obj.nombre for obj in self.tipocolaborador.all()])
    def __unicode__(self):
        return u"%s" %(self.directorio)



class Directoriotipoareaaccions(models.Model):
    directorio = models.ForeignKey(Directorios, null=True, blank=True)
    tipoareaaccion = models.ForeignKey(Tipoareaaccions, null=True, db_column='tipoAreaAccion_id', blank=True)
    class Meta:
        db_table = u'directorioTipoAreaAccions'
        verbose_name_plural='Directorio Tipos Áreas de Acción'
        verbose_name='Directorio Tipos Áreas de Acción'
        #app_label = 'Actores'
    def __unicode__(self):
        return u"%s" %(self.directorio)

class Personalasociados(models.Model):
    directorio = models.ForeignKey(Directorios, null=True, blank=True)
    actore = models.ForeignKey(Actores, null=True, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'personalAsociados'
        verbose_name_plural='Personal Asociado a Colectivos'
        verbose_name='Personal Asociado a Colectivos'
        #app_label = 'Actores'
    def __unicode__(self):
        return u"%s" %(self.directorio)


class Redessociales(models.Model):
    actore = models.ForeignKey(Actores, null=True, blank=True)
    red = models.ForeignKey(Reds, null=True, blank=True)
    url = models.URLField(max_length=300)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'redesSociales'
        verbose_name_plural='Redes Sociales'
        verbose_name='Redes Sociales'
        #app_label = 'Datos_Transversales'
    def __unicode__(self):
        return u"%s %s" %(self.red,self.actore)


class Vinculacionactores(models.Model):
    actore = models.ForeignKey(Actores, null=True, blank=True)
    fundamento = models.ForeignKey(Fundamentos, null=True, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'vinculacionActores'
        verbose_name_plural='Relación Colectivos-Fundamentos'
        verbose_name='Relación Colectivos-Fundamentos'
        #app_label = 'Actores'
    def __unicode__(self):
        return u"%s" %(self.actore)
		

class Noticias(models.Model):
    titulo = models.CharField(max_length=135)
    contenido = models.TextField()
    fecha = models.DateField()
    autor = models.ForeignKey(Actores)
    pathimg = models.ManyToManyField(Bancoaudiovisuals,related_name='path') 
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'noticias'
        #app_label = 'Gestiones'
        verbose_name_plural='Noticias'
        verbose_name='Noticias'
    def __unicode__(self):
        return u"%s" %(self.titulo)

