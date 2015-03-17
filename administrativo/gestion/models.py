#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from stdimage import StdImageField
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey 

# Create your models here.

class Tablas(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Nombre',help_text='Ingrese el Nombre de una de las tablas que maneja la base de datos del Sistema, <b>Tenga presente que su uso es delicado.</b>',unique=True)
    class Meta:
        db_table = u'tablas'
        #app_label = 'Gestion'
        verbose_name_plural='Tablas del Sistema'
        verbose_name='Tablas del Sistema'
        #unique_together=('name')
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
class Tipoelementos(models.Model):
    nombre = models.CharField(max_length=150,verbose_name='Nombre',help_text=u'Ingrese el nombre de un elemento. Los elementos van a ser una relacion directa con las tablas o menus del sistema.')
    tabla = models.ForeignKey(Tablas,db_column='tabla_id',verbose_name='Tabla',help_text=u'Es importante que seleccione una tabla del sistema.')
    class Meta:
        db_table = u'tipoElementos'
        verbose_name_plural='Tipo de Elementos'
        verbose_name='Tipo de Elementos'
        unique_together=('nombre','tabla')
        #app_label = 'Gestion'
    def __unicode__(self):
        return u"%s" %(self.nombre)

class Estatus(models.Model):
    nombre = models.CharField(max_length=135)
    tipoelemento = models.ForeignKey(Tipoelementos, null=True, db_column='tipoElemento_id') 
    class Meta:
        db_table = u'estatus'
        verbose_name_plural='Estatus'
        verbose_name='Estatus'
        unique_together=('nombre','tipoelemento')
        #app_label = 'Gestion'

    def __unicode__(self):
        return u"%s  %s" %(self.nombre, self.tipoelemento.nombre)
		
		
class Glosario(models.Model):
    nombre = models.CharField(max_length=135)
    definicion = models.TextField(verbose_name='Definición')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'glosario'
        verbose_name_plural='Glosario'
        verbose_name='Glosario'
        #app_label = 'Datos_Transversales'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
class Tsauro(models.Model):
    nombre = models.CharField(max_length=135)
    definicion = models.TextField(verbose_name='Definición')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'tsauro'
        verbose_name_plural='Tesauro'
        verbose_name='Tesauro'
        #app_label = 'Gestion'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
class Tipoorganizacions(models.Model):
    nombre = models.CharField(max_length=135,unique=True)
    userupdate = models.ForeignKey(User,verbose_name='Usuario') 
    update = models.DateTimeField(default=datetime.now(),editable = False)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'tipoOrganizacions'
        verbose_name_plural='Tipo de Organizaciones'
        verbose_name='Tipo de Organizaciones'
        #app_label = 'Actores'
    def __unicode__(self):
        return u"%s" %(self.nombre)

class Documentosgenerados(models.Model):
    codigo = models.CharField(max_length=135, unique=True)
    fecha = models.DateField()
    validez = models.CharField(max_length=135)
    fechacaduc = models.DateField(null=True, db_column='fechaCaduc', blank=True) 
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'documentosGenerados'
        verbose_name_plural='Documentos Generados'
        verbose_name='Documentos Generados'
        #app_label = 'Gestion'
    def __unicode__(self):
        return u"Documento Codigo:%s de fecha: %s valido hasta: %s" %(self.codigo, self.fecha,self.fechacaduc)


class Pablabrasclaves(models.Model):
    palabrasclave = models.CharField(max_length=135, db_column='palabrasClave',unique=True) 
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario') 
    class Meta:
        db_table = u'pablabrasClaves'
        verbose_name_plural='Palabras Claves'
        verbose_name='Palabras Claves'
        #app_label = 'Gestion'
    def __unicode__(self):
        return u" %s"%(self.palabrasclave)

class TiposManifestaciones(models.Model):
    tipo = models.CharField(max_length=150)
    estandares = models.CharField(max_length=300)
    class Meta:
        db_table = u'tiposManifestaciones'
        verbose_name_plural = 'Tipos Manifestaciones Culturales'
        verbose_name = 'Tipos Manifestaciones Culturales'
        #app_label = 'Datos_Transversales'
    def __unicode__(self):
        return u"%s"%(self.tipo)

class Servicios(models.Model):
    servicios = models.CharField(max_length=135, unique=True)
    pathimg = models.ImageField(upload_to='pathImg',db_column='pathImg')
    class Meta:
        db_table = u'servicios'
        verbose_name_plural='Servicios'
        verbose_name='Servicios'
        #app_label = 'Areas_Estrategicas_para_la_Conservacion'
    def __unicode__(self):
        return u"%s" %(self.servicios)

class Reds(models.Model):
    nombre = models.CharField(max_length=135, unique=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    pathimg = models.ImageField(upload_to='redes',db_column='logo',null=True, blank=True)
    userupdate = models.ForeignKey(User,verbose_name='Usuario') 
    class Meta:
        db_table = u'reds'
        verbose_name_plural='Tipos de Redes Sociales'
        verbose_name='Tipos de Redes Sociales'
        #app_label = 'Datos_Transversales'
    def __unicode__(self):
        return u"%s " %(self.nombre)


class PreguntasFrecuentes(models.Model):
    pregunta = models.CharField(max_length=300)
    respuesta = models.TextField()
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'preguntas_frecuentes'
        #app_label = 'Gestion'
        verbose_name_plural='Preguntas Frecuentes'
        verbose_name='Preguntas Frecuentes'
        #unique_together=('pregunta','respuesta')
    def __unicode__(self):
        return u"%s %s" %(self.pregunta, self.estatu)

class EnlacesExternos(models.Model):
    nombre = models.CharField(max_length=300, blank=True, null=True)
    enlaces = models.URLField(max_length=300)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    class Meta:
        db_table = u'enlacesExternos'
        #app_label = 'Datos_Transversales'
        verbose_name_plural='Enlaces Externos'
        verbose_name='Enlaces Externos'
        #unique_together=('pregunta','respuesta')
    def __unicode__(self):
        return u"%s" %(self.nombre)

#class Glosario(models.Model):
#    nombre = models.CharField(max_length=135)
#    definicion = models.TextField(verbose_name='Definición')
#    update = models.DateTimeField(default=datetime.now(),editable = False)
#    class Meta:
#        db_table = u'glosarios'
#        verbose_name_plural='Glosario'
#        verbose_name='Glosario'
#        #app_label = 'Datos_Transversales'
#    def __unicode__(self):
#        return u"%s" %(self.nombre)
		
class ListasCorreos(models.Model):
    nombre = models.CharField(max_length=135,verbose_name='Listas')
    definicion = models.TextField(verbose_name='Descripción')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    class Meta:
        db_table = u'listascorreos'
        verbose_name_plural='Listas de Correos MailMan'
        verbose_name='Listas de Correos MailMan'
        #app_label = 'Gestion'
    def __unicode__(self):
        return u"%s" %(self.nombre)

		
		
