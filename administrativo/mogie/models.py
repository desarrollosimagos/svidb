#!/usr/bin/python -u
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from perfil.models import *
from congresos.models import *


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
        

class ColaboracionConf(models.Model):
    titulo = models.CharField(max_length=150,verbose_name='Titulo')
    evento = models.ForeignKey(Eventos,null=True, blank=True,verbose_name='Evento')
    metodo = models.IntegerField(choices=((0,'Inscripcion'),(1,'Pre-inscripcion'),(2,'Postulacion Resumenes')),verbose_name='Metodo',null=True,blank=True)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo')),verbose_name='Estatus',null=True,blank=True)
    class Meta:
        verbose_name_plural='Colaboracion Conf'
        verbose_name='Colaboracion Conf'
        unique_together=('titulo','evento','metodo','estatu')
    def __unicode__(self):
        return u"%s" %(self.titulo)
        
class ValoresDefectoSeleccion(models.Model):
    valor = models.CharField(max_length=150,verbose_name='Titulo')
    class Meta:
        verbose_name_plural='Valores Defecto Seleccion'
        verbose_name='Valores Defecto Seleccion'
    def __unicode__(self):
        return u"%s" %(self.valor)
        
class DetalleColaboracionConf(models.Model):
    colaboracion = models.ForeignKey(ColaboracionConf,verbose_name='Formulario Colaboracion',null=True, blank=True)
    titulo = models.CharField(max_length=150,verbose_name='Titulo',null=True, blank=True)
    tipo = models.IntegerField(choices=((0,'Texto'),(1,'Numero'),(2,'Fecha'),(3,'Booleano'),(4,'Seleccion'),(5,'Imagen'),(6,'Archivo')),verbose_name='Tipo',null=True,blank=True)
    valorDefaultSelect = models.ManyToManyField(ValoresDefectoSeleccion,related_name='valordefaultselect',verbose_name='Valores por Defecto de Seleccion',blank=True,null=True)
    valorDefault = models.CharField(max_length=150,verbose_name='Valor por defecto Textos',null=True, blank=True)
    requerido = models.BooleanField(verbose_name='Requerido', blank=True)
    validacion = models.CharField(max_length=150,verbose_name='Validacion',null=True, blank=True)
    class Meta:
        verbose_name_plural='Detalle Colaboracion Conf'
        verbose_name='Detalle Colaboracion Conf'
        unique_together=('colaboracion','titulo','tipo')
    def __unicode__(self):
        return u"%s" %(self.titulo)
        
class ColaboracionPersonas(models.Model):
    colaboracionconf = models.ForeignKey(ColaboracionConf,null=True, blank=True,verbose_name='Colaboracion Conf')
    personas = models.ForeignKey(Directorios,null=True, blank=True,verbose_name='Personas')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    estatu = models.IntegerField(choices=((0,'Procesada'),(1,'Por procesar'),(2,'Rechazada')),verbose_name='Estatus',null=True,blank=True)
    class Meta:
        verbose_name_plural='Colaboracion Personas'
        verbose_name='Colaboracion Personas'
        unique_together=('colaboracionconf','personas')
    def __unicode__(self):
        return u"%s" %(self.personas)
        
class ColaboracionInformacion(models.Model):
    colaboracionconf = models.ForeignKey(ColaboracionConf,null=True, blank=True,verbose_name='Colaboracion Conf')
    colaboracionpersonas = models.ForeignKey(ColaboracionPersonas,null=True, blank=True,verbose_name='Colaboracion Personas')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    textos = models.CharField(max_length=300,verbose_name='Textos',null=True, blank=True)
    foto = models.ImageField(upload_to='colaboracion/image',null=True, blank=True)
    archivo = models.FileField(upload_to='colaboracion/files',verbose_name='Archivo',blank=True,null=True)
    class Meta:
        verbose_name_plural='Colaboracion Informacion'
        verbose_name='Colaboracion Informacion'
        unique_together=('colaboracionconf','colaboracionpersonas','textos','foto','archivo','update')
    def __unicode__(self):
        return u"%s" %(self.colaboracionpersonas)  
        
class RelacionPersonasTrabajos(models.Model):
    trabajo = models.ForeignKey(Trabajoscongresos,null=True, blank=True,verbose_name='Traba')
    personas = models.ForeignKey(Directorios,null=True, blank=True,verbose_name='Coautor Persona')
    instituciones = models.ForeignKey(ActoresHistorico,null=True, blank=True,verbose_name='Coautor Institucion')
    institucionestxt = models.CharField(max_length=300,verbose_name='Institucion Nombre',null=True, blank=True)
    orden = models.IntegerField(verbose_name='Orden',null=True, blank=True)
    class Meta:
        verbose_name_plural='Relacion personas Trabajos'
        verbose_name='Relacion personas Trabajos'
        unique_together=('trabajo','personas','instituciones',)
    def __unicode__(self):
        return u"%s" %(self.trabajo) 

class RelacionActoresTrabajos(models.Model):
    trabajo = models.ForeignKey(Trabajoscongresos,null=True, blank=True,verbose_name='Traba')
    instituciones = models.ForeignKey(ActoresHistorico,null=True, blank=True,verbose_name='Coautor Institucion')
    orden = models.IntegerField(verbose_name='Orden',null=True, blank=True)
    class Meta:
        verbose_name_plural='Relacion Actores Trabajos'
        verbose_name='Relacion Actores Trabajos'
        unique_together=('trabajo','instituciones',)
    def __unicode__(self):
        return u"%s" %(self.trabajo) 
        
class DetalleResumenConfiguracion(models.Model):
    evento = models.ForeignKey(Eventos,null=True, blank=True,verbose_name='Evento')
    header = models.ImageField(upload_to='eventos/header',null=True, blank=True)
    firma = models.ImageField(upload_to='eventos/firmas',null=True, blank=True)
    class Meta:
        verbose_name_plural='Detalle Configuracion de Previsual'
        verbose_name='Detalle Configuracion de Previsual'
    def __unicode__(self):
        return u"%s" %(self.evento)

    
