#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from gestion.models import *
from datetime import datetime
from django.contrib.auth.models import User

from os import *
import uuid
import os
import shutil
from django.conf import settings
import Image

# Create your models here.
class Secciones(models.Model):
    titulo = models.CharField(max_length=180)
    descripcion = models.TextField()
    pathimg = models.ImageField(upload_to='pathImg/secciones',db_column='pathImg',blank=True,null=True) 
    pathimgtop = models.ImageField(upload_to='pathImgTop',db_column='pathImgTop',blank=True,null=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    posicion = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'secciones'
        verbose_name_plural='Secciones del Sistema'
        verbose_name='Secciones del Sistema'
        unique_together=('titulo','estatu')
    def __unicode__(self):
        return u" %s %s"%(self.titulo,self.estatu)

class Categorias(models.Model):
    titulo = models.CharField(max_length=180)
    descri = models.TextField()
    vinculo = models.TextField(blank=True)
    pathimg = models.ImageField(upload_to='pathImg/categorias',db_column='pathImg',blank=True,null=True)
    pathimgtop = models.ImageField(upload_to='pathImgTop',db_column='pathImgTop',blank=True,null=True)
    posicion = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    seccione = models.ForeignKey('Secciones')
    class Meta:
        db_table = u'categorias'
        verbose_name_plural='Categorías del Sistema'
        verbose_name='Categorías del Sistema'
        unique_together=('titulo','estatu')
    def __unicode__(self):
        return u" %s %s"%(self.titulo,self.estatu)
		

class SubTipoCategorias(models.Model):
    nombre = models.CharField(max_length=180,db_column='titulo')
    descri = models.TextField()
    vinculo = models.TextField(blank=True)
    pathimg = models.ImageField(upload_to='pathImg/subcategorias',db_column='pathImg',blank=True,null=True)
    pathimgtop = models.ImageField(upload_to='pathImgTop',db_column='pathImgTop',blank=True,null=True)
    posicion = models.IntegerField(null=True, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    categoria = models.ForeignKey(Categorias,verbose_name='Categoria')
    userupdate = models.ForeignKey(User,verbose_name='Usted es?')
    class Meta:
        db_table = u'subtipocategorias'
        verbose_name_plural='Subcategorias del Sistema'
        verbose_name='Subcategorias del Sistema'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
		
#YEARS = (
#    ("1990", "1990"),
#    ("1991", "1991"),
#    ("1992", "1992"),
    # P.e. generate a list from 1960 to date.today().year
    # The reason why they choice key and text value are the
    # same is that if you generate from 1960 to 2060 it will collide.
    #
    # E.g
    # from datetime import datetime
    # def tuplify(x): return (x,x)   # str(x) if needed
    # current_year = datetime.now().year
    # YEARS = map(tuplify, range(1930, current_year + 1))  # range(1,4) gives [1,2,3]
#)

#def tuplify(x): return (x,x)


#current_year = datetime.now().year
#YEARS = map(tuplify, range(1930, current_year + 1))  

#class anios(models.Model):
#    birthdate = models.IntegerField(max_length=2, choices=YEARS)
#    dates = models.DateField(default=datetime.date.today() - datetime.timedelta(days=6210))

		
class Mapas(models.Model):
    nombre = models.CharField(max_length=135, blank=True)
    fuente = models.TextField(blank=True)
    pathimg1 = models.ImageField(upload_to='mapas/imagenes',db_column='pathImg1',verbose_name='Imagen') 
    pathimg2 = models.FileField(upload_to='mapas/pdf',db_column='pathImg2',verbose_name='PDF') 
    pathimg3 = models.FileField(upload_to='mapas/capas',db_column='pathImg3',verbose_name='Capas') 
    basecartogra = models.TextField(blank=True,verbose_name='Base Cartográfica') 
    secciones = models.IntegerField(choices=((0,'Areas'),(1,'Especies'),(2,'Actores'),(3,'Biorregiones')),verbose_name='Secciones',null=True,blank=True,db_column='secciones_id')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuarios')
    estatu = models.IntegerField(choices=((0,'Con vínculo'),(1,'Sin vínculo')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    observaciones = models.TextField(blank=True)
    class Meta:
        db_table = u'mapas'
        verbose_name_plural='Mapas'
        verbose_name='Mapas'
        #app_label = 'Datos_Transversales'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
		
class ImagenesSistemas(models.Model):
    TIPO_BAN = (
        ('1','Fotografia'),('2','Banner'),('3','Iconos'),('4','botones')
    )
    titulo = models.CharField(blank=True,null=True,max_length=120)
    descripcion = models.TextField(blank=True,null=True,verbose_name='Descripción')
    tipo = models.CharField(choices=TIPO_BAN,max_length=135)
    pathimg = StdImageField(upload_to='imgs',size=None, thumbnail_size=(157,118), verbose_name='Archivo')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    seccion = models.CharField(choices=(('0','Areas'),('1','Especies'),('2','Actores'),('3','Manifestaciones Culturales'),('4','Biorregiones'),('5','Eventos y Actividades')),max_length=135, blank=True)
    def retorno_nombre(self):
        name, extension = os.path.splitext(self.pathimg.name)
        return name
    def retorno_extencion(self):
        name, extension = os.path.splitext(self.pathimg.name)
        return extension
    class Meta:
        db_table = u'ImagenesSistemas'
        verbose_name_plural='Imagenes Sistemas'
        verbose_name = 'Imagenes Sistemas'
        #app_label = 'Datos_Transversales'
    def __unicode__(self):
        return u"ID: %s " %(self.id)
		
