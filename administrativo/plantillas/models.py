#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from menu.models import *
from congresos.models import *
from smart_selects.db_fields import ChainedForeignKey 

# Create your models here.

class Templates(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Titulo')
    seccion = models.ForeignKey(Secciones,verbose_name='Categorias',null=True,blank=True)
    subseccion = ChainedForeignKey(Categorias,chained_field="seccion",chained_model_field="seccione",show_all=False,auto_choose=True,verbose_name='Sub-Secciones',null=True, blank=True)
    descripcion = models.TextField(blank=True,verbose_name='HTML')
    posicion = models.IntegerField(blank=True)
    class Meta:
        db_table = u'templates'
        verbose_name_plural='Plantillas Estaticas'
        verbose_name='Plantillas Estaticas'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
class TemplatesEventos(models.Model):
    evento = models.ForeignKey(Eventos,null=True, blank=True,verbose_name='Evento')
    nombre = models.CharField(max_length=150,verbose_name='Titulo')
    seccion = models.ForeignKey(Secciones,verbose_name='Categorias',null=True,blank=True)
    subseccion = ChainedForeignKey(Categorias,chained_field="seccion",chained_model_field="seccione",show_all=False,auto_choose=True,verbose_name='Sub-Secciones',null=True, blank=True)
    descripcion = models.TextField(blank=True,verbose_name='HTML')
    posicion = models.IntegerField(blank=True)
    class Meta:
        db_table = u'templatesEventos'
        verbose_name_plural='Plantillas Estaticas para Eventos'
        verbose_name='Plantillas Estaticas para Eventos'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
class TemplatesInfoLateral(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Titulo')
    descripcion = models.TextField(blank=True,verbose_name='HTML')
    seccion = models.ForeignKey(Secciones,verbose_name='Categorias',null=True,blank=True)
    subseccion = ChainedForeignKey(Categorias,chained_field="seccion",chained_model_field="seccione",show_all=False,auto_choose=True,verbose_name='Sub-Secciones',null=True, blank=True)
    activar = models.BooleanField(verbose_name='Activar en todas las paginas de la seccion')
    posicion = models.IntegerField(blank=True)
    class Meta:
        db_table = u'templates2'
        verbose_name_plural='Plantillas Informacion Lateral'
        verbose_name='Plantillas Informacion Lateral'
    def __unicode__(self):
        return u"%s" %(self.nombre)
