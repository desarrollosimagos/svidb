#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class TiposFundamentos(models.Model):
    tipo = models.CharField(max_length=135)
    descripcion = models.TextField(verbose_name='Descripción')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'tiposFundamentos'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
        verbose_name_plural='Tipos Fundamentos'
        verbose_name='Tipos Fundamentos'
    def __unicode__(self):
        return u"%s" %(self.tipo)


class Fundamentos(models.Model):
    tipo = models.ForeignKey(TiposFundamentos)
    nombre = models.CharField(max_length=450)
    objetivogeneral = models.TextField(db_column='objetivoGeneral',verbose_name='Objetivos Generales')
    numero = models.IntegerField()
    introduccion = models.TextField()
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'fundamentos'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
        verbose_name_plural='Fundamentos'
        verbose_name='Fundamentos'
    def __unicode__(self):
        return u"%s" %(self.nombre)


class Objetivoespecificos(models.Model):
    nombre = models.CharField(max_length=450)
    fundamento = models.ForeignKey(Fundamentos)
    numero = models.IntegerField()
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'objetivoEspecificos'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
        verbose_name_plural='Objetivos Específicos'
        verbose_name='Objetivos Especificos'
    def __unicode__(self):
        return u"%s" %(self.nombre)

class Accionesgenerales(models.Model):
    nombre = models.CharField(max_length=450)
    objetivoespecifico = models.ForeignKey(Objetivoespecificos,db_column='objetivoEspecifico_id',verbose_name='Objetivos Especificos')
    numero = models.IntegerField()
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'accionesGenerales'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
        verbose_name_plural='Acciones Generales'
        verbose_name='Acciones Generales'
    def __unicode__(self):
        return u"%s" %(self.nombre)

class Accionesespecificas(models.Model):
    nombre = models.CharField(max_length=450)
    indicador = models.TextField()
    accionesgenerale = models.ForeignKey(Accionesgenerales,db_column='accionesGenerale_id',verbose_name='Acciones Generales')
    numero = models.IntegerField()
    meta2012 = models.IntegerField(verbose_name='Metas 2012')
    meta2015 = models.IntegerField(verbose_name='Metas 2015')
    meta2020 = models.IntegerField(verbose_name='Metas 2020')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'accionesEspecificas'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
        verbose_name_plural='Acciones Específicas'
        verbose_name='Acciones Específicas'
    def __unicode__(self):
        return u"%s" %(self.nombre)

class Tareas(models.Model):
    nombre = models.CharField(max_length=450)
    acciones = models.ForeignKey(Accionesespecificas, verbose_name='Acciones Especificas',related_name='Accion Especifica')
    numero = models.IntegerField()
    class Meta:
        db_table = u'tareas'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
        verbose_name_plural='Tareas'
        verbose_name='Tareas'
    def __unicode__(self):
        return u"%s" %(self.nombre)