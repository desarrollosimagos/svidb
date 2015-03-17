#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from congresos.models import *
from perfil.models import *

# Create your models here.

class coordinador(models.Model):
    coordinador = models.ForeignKey(Directorios,null=True, blank=True,verbose_name='Coordinador')
    evento = models.ForeignKey(Eventos,null=True, blank=True)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True)
    class Meta:
        verbose_name_plural='Coordinadores por eventos'
        verbose_name='Coordinadores por eventos'
    def __unicode__(self):
        return u"%s" %(self.coordinador)
	  
class arbitros(models.Model):
    coordinador = models.ForeignKey(coordinador,null=True, blank=True,verbose_name='Coordinador')
    arbitro = models.ForeignKey(Directorios,null=True, blank=True,verbose_name='Arbitro')
    evento = models.ForeignKey(Eventos,null=True, blank=True)
    accespecifi = models.ManyToManyField(Accionesespecificas,blank=True,null=True)
    modalidad = models.ManyToManyField(Modalidads,blank=True,null=True)
    tematicas = models.ManyToManyField(Tematicas,blank=True,null=True)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True)
    class Meta:
        verbose_name_plural='Arbitros'
        verbose_name='Arbitro'
    def __unicode__(self):
        return u"%s" %(self.arbitro)
	
class TrabajosArbitros(models.Model):
    arbitro = models.ForeignKey(arbitros,null=True, blank=True,verbose_name='Arbitro')
    trabajos = models.ForeignKey(Trabajoscongresos,null=True, blank=True)
    estatu = models.IntegerField(choices=((1,'Aprobado'),(2,'Rechazado'),(3,'Arbitrando')),verbose_name='Estatus',null=True,blank=True)
    class Meta:
        verbose_name_plural='Trabajos asignados por arbitros'
        verbose_name='Trabajos asignados por arbitros'
    def __unicode__(self):
        return u"%s" %(self.trabajos)

class HistorialModificacionesTrabajos(models.Model):
    userupdate = models.ForeignKey(PerfilPublico,verbose_name='Remitente',null=True,blank=True)
    campo = models.CharField(max_length=50,verbose_name='Campo')
    modificacion = models.TextField(blank=True,verbose_name='Modificacion')
    trabajos = models.ForeignKey(Trabajoscongresos)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    class Meta:
        verbose_name_plural='Historial de Modificaciones de Resumenes'
        verbose_name='Historial de Modificaciones de Resumenes'
    def __unicode__(self):
        return u"%s %s" %(self.campo,self.userupdate)		
		
class MensajeTrabajosArbitraje(models.Model):
    userupdate = models.ForeignKey(PerfilPublico,verbose_name='Remitente',null=True,blank=True)
    mensaje = models.TextField(blank=True,verbose_name='Descripción')
    trabajos = models.ForeignKey(Trabajoscongresos)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    class Meta:
        verbose_name_plural='Mensajes Arbitraje'
        verbose_name='Mensajes Arbitraje'
    def __unicode__(self):
        return u"%s %s" %(self.userupdate,self.trabajos)