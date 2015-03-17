#!/usr/bin/python -u
# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from mapas.models import *
from actores.models import *

class PerfilPublico(models.Model):
    user = models.OneToOneField(User,verbose_name='Usuario')
    persona = models.OneToOneField(Directorios)
    class Meta:
        db_table = u'perfilpublico'
        verbose_name_plural='Perfil Público'
        verbose_name='Perfil Público'
        unique_together=('user','persona')
        #app_label = 'Sistematizacion_de_modulos_publicos'
    def __unicode__(self):
        return u"%s" %(self.persona.nombre)
		
class SeccionesPanelPublico(models.Model):
    panel = models.CharField(max_length=180,verbose_name='Modulo')
    descripcion = models.TextField()
#    modulos = models.ManyToManyField(ModulosPublicos,related_name='Modulos Principales',verbose_name='Modulos',blank=True)
    activo = models.BooleanField(verbose_name="Activo")
    is_admmin = models.BooleanField(verbose_name="Solo para Administradores")
    posicion = models.IntegerField(verbose_name="Posicion")
    class Meta:
        verbose_name_plural='Secciones del Panel Publico'
        verbose_name='Secciones del Panel Publico'
    def __unicode__(self):
        return u"%s" %(self.panel)

class ModulosPublicos(models.Model):
    paneles = models.ForeignKey(SeccionesPanelPublico)
    modulo = models.CharField(max_length=180,verbose_name='Modulo')
    url = models.CharField(max_length=180,verbose_name='URL',blank=True,null=True)
    boton = models.ImageField(upload_to='modulos')
#    submodulos = models.ManyToManyField(SubModulosPublicos,related_name='Submodulos',verbose_name='Sub Modulos',blank=True)
    descripcion = models.TextField()
    is_admmin = models.BooleanField(verbose_name="Solo para Administradores")
    activo = models.BooleanField(verbose_name="Activo")
    posicion = models.IntegerField(verbose_name="Posicion")
    target = models.CharField(max_length=40,choices=(('_blank',u'Abre el documento vinculado en una nueva ventana o pestaña'),('_self',u'Abre el documento vinculado en el mismo marco que se ha hecho clic'),('_parent',u'Abre el documento vinculado en el marco padre'),('_top',u'Abre el documento vinculado en el pleno de la ventana')),verbose_name='Target del Vinculo')
    class Meta:
        verbose_name_plural='Módulos Públicos'
        verbose_name='Módulos Públicos'
        #app_label = 'Sistematizacion_de_modulos_publicos'
    def __unicode__(self):
        return u"%s - %s" %(self.paneles.panel, self.modulo)
		
    def logo(self):
        logo = ""
        if self.boton:
           esta = "<img src='" + self.boton.url +"' alt='Activo' height='150px'>"
        else:
           esta = "<img src='/media/imgs/icon-pendiente.gif' alt='Pendiente'> sin imagen"
        return u"%s"%(esta)
    logo.allow_tags = True

class SubModulosPublicos(models.Model):
    modulos = models.ForeignKey(ModulosPublicos)
    titulo = models.CharField(max_length=180,verbose_name='Modulo')
    url = models.CharField(max_length=180,verbose_name='URL',blank=True,null=True)
    boton = models.ImageField(upload_to='modulos') 	  
    descripcion = models.TextField()
    is_admmin = models.BooleanField(verbose_name="Solo para Administradores")
    activo = models.BooleanField(verbose_name="Activo")
    posicion = models.IntegerField(verbose_name="Posicion")
    target = models.CharField(max_length=40,choices=(('_blank',u'Abre el documento vinculado en una nueva ventana o pestaña'),('_self',u'Abre el documento vinculado en el mismo marco que se ha hecho clic'),('_parent',u'Abre el documento vinculado en el marco padre'),('_top',u'Abre el documento vinculado en el pleno de la ventana')),verbose_name='Target del Vinculo')
    class Meta:
        verbose_name_plural='Sub Módulos Públicos'
        verbose_name='Sub Módulos Públicos'
    def __unicode__(self):
        return u"%s %s %s" %(self.modulos.paneles.panel, self.modulos.modulo,self.titulo)
    def logo(self):
        logo = ""
        if self.boton:
           esta = "<img src='" + self.boton.url +"' alt='Activo' height='150px'>"
        else:
           esta = "<img src='/media/imgs/icon-pendiente.gif' alt='Pendiente'> sin imagen"
        return u"%s"%(esta)
    logo.allow_tags = True


class PerfilModulos(models.Model):
    perfil = models.ForeignKey(PerfilPublico)
    modulos = models.ForeignKey(ModulosPublicos,verbose_name='Modulos')
    ver = models.BooleanField(verbose_name="Ver")
    add = models.BooleanField(verbose_name="Agregar")
    edit = models.BooleanField(verbose_name="Modificar")
    activo = models.BooleanField(verbose_name="Activo")
    class Meta:
        db_table = u'perfilmodulos'
        verbose_name_plural='Permisos Perfiles Módulos'
        unique_together=('perfil','modulos','activo')
        verbose_name='Permisos Perfiles Módulos'
        #app_label = 'Sistematizacion_de_modulos_publicos'
    def __unicode__(self):
        return u"%s %s" %(self.perfil.persona.nombre,self.modulos.modulo)
		
class PerfilSubModulos(models.Model):
    perfil = models.ForeignKey(PerfilPublico)
    submodulos = models.ForeignKey(SubModulosPublicos,verbose_name='SubModulos')
    ver = models.BooleanField(verbose_name="Ver")
    add = models.BooleanField(verbose_name="Agregar")
    edit = models.BooleanField(verbose_name="Modificar")
    activo = models.BooleanField(verbose_name="Activo")
    class Meta:
        verbose_name_plural='Permisos Perfiles Sub Módulos'
        verbose_name='Permisos Perfil Sub Módulos'
        unique_together=('perfil','submodulos','activo')
        #app_label = 'Sistematizacion_de_modulos_publicos'
    def __unicode__(self):
        return u"%s %s" %(self.perfil.persona.nombre,self.submodulos.titulo)
		
#class PerfilPaneles(models.Model):
#    perfil = models.ForeignKey(PerfilPublico)
#    modulos = models.ManyToManyField(SeccionesPanelPublico,verbose_name='Paneles')
#    class Meta:
#        verbose_name_plural='Perfil Paneles'
#        verbose_name='Perfil Paneles'
#    def __unicode__(self):
#        return u"%s %s" %(self.perfil.persona.nombre,self.perfil.persona.documentoidentidad)

class TipoSolicitud(models.Model):
    tipo = models.CharField(max_length=180,verbose_name='Tipo')
    descripcion = models.TextField()
    class Meta:
        verbose_name_plural='Tipo de Solicitud'
        verbose_name='Tipo de Solicitud'
    def __unicode__(self):
        return u"%s" %(self.tipo)
		
		
class SistemaSolicitudes(models.Model):
    remi = models.ForeignKey(Directorios,verbose_name='Remitente')
    tipoSolicitud = models.ForeignKey(TipoSolicitud,verbose_name='Tipo de Solicitud',blank=True, null = True)
    destino = models.ManyToManyField(Directorios, related_name='destinodirect',verbose_name='Destinatarios',blank=True, null = True)
    destinoinst = models.ManyToManyField(Actores, related_name='destinoactor',verbose_name='Destinatarios Instituciones',blank=True, null = True)
    asunto = models.CharField(max_length=120,blank=True,null=True)
    mensaje = models.TextField(blank=True,null=True)
    fecha = models.DateTimeField(default=datetime.now(),editable = False)
    fechainicio = models.DateTimeField(verbose_name='Fecha de Inicio',blank=True,null=True)
    fechaentrega = models.DateTimeField(verbose_name='Fecha de Entrega',blank=True,null=True)
    fechaculminacion = models.DateTimeField(verbose_name='Fecha de Culminación',blank=True,null=True)
    fechaprorroga = models.DateTimeField(verbose_name='Prorroga',blank=True,null=True)
    proyect = models.BooleanField(verbose_name='Es Proyectable?')
    estrucorg = models.TextField(verbose_name='Recursos', blank=True, null=True)

    personasinvol = models.ManyToManyField(Directorios, related_name='persoinvol',verbose_name='Personas Involucradas',blank=True, null = True)
    personasinvoltext = models.TextField(verbose_name='Personas Involucradas, no registradas', blank=True, null=True)

    instituinvol = models.ManyToManyField(Actores, related_name='instiinvol',verbose_name='Instituciones Involucradas',blank=True, null = True)
    instituinvoltext = models.TextField(verbose_name='Institutos Involucrados, no registrados', blank=True, null=True)
	
    especies = models.ManyToManyField(Taxon, related_name='tax',verbose_name='Especies Involucradas',blank=True, null = True)
    especiestext = models.TextField(verbose_name='Especies Involucradas, no registradas', blank=True, null=True)

    areas = models.ManyToManyField(Areas, related_name='ar',verbose_name='Areas Involucradas',blank=True, null = True)
    areastext = models.TextField(verbose_name='Areas Involucradas, no registradas', blank=True, null=True)
	
    datos = models.FileField(upload_to='solicitudes',verbose_name='Datos Adjuntos',blank=True,null=True)
    prioridad = models.IntegerField(choices=((0,'Urgente'),(1,'Normal'),(2,'Especial')),verbose_name='Prioridad',null=True,blank=True)
    estatu = models.IntegerField(choices=((0,'Abierto'),(1,'Cerrado'),(2,'Pausado')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        verbose_name_plural='Sistema de Solicitudes'
        #app_label = 'Datos_Transversales' 
        verbose_name = 'Sistema de Solicitudes'
    def __unicode__(self):
        return u" %s %s"%(self.remi,self.estatu)
		
#    def VerEspecies(self):
#        try:
#           espe = Taxon.objects.get(detalletaxon=self)
#        except Taxon.DoesNotExist:
#           espe = None
#        return u"<a href='/manager/especies/taxon/%s'>Ver Taxon</a>"%(tax.id)
#    VerTaxon.allow_tags = True

class Seguimiento(models.Model):
    solicitud = models.ForeignKey(SistemaSolicitudes,verbose_name='Solicitud',blank=True, null = True)
    persona = models.ForeignKey(Directorios,verbose_name='Persona',blank=True, null = True,editable = False)
    mensaje = models.TextField()
    fecha = models.DateTimeField(default=datetime.now(),editable = False)
    class Meta:
        verbose_name_plural='Seguimiento'
        verbose_name='Seguimiento'
    def __unicode__(self):
        return u"%s" %(self.solicitud)

class validaciones(models.Model):
    usuario = models.ForeignKey(PerfilPublico,verbose_name='Usuario')
    codigo = models.CharField(max_length=120)
    estatu = models.IntegerField(choices=((0,'Validacion'),(1,'Recuperacion'),(2,'Eliminacion')),verbose_name='Tipo',null=True,blank=True)
    fecha = models.DateTimeField(default=datetime.now(),editable = False)
    estado = models.BooleanField(verbose_name="Activo")
    class Meta:
        verbose_name_plural='Validacion de Cuentas'
        #app_label = 'Datos_Transversales' 
        verbose_name = 'Validacion de Cuentas'
    def __unicode__(self):
        return u" %s %s"%(self.usuario,self.estatu)
		
class GruposPermisos(models.Model):
    nombre = models.CharField(max_length=120)
    estado = models.BooleanField(verbose_name="Activo")
    class Meta:
        verbose_name_plural='Grupos de Permisos de Perfil'
        verbose_name = 'Grupos de Permisos de Perfil'
    def __unicode__(self):
        return u" %s %s"%(self.nombre,self.estado)
		
class DetalleGruposPermisos(models.Model):
    grupo = models.ForeignKey(GruposPermisos,verbose_name='Grupo')
    seccion = models.ForeignKey(SeccionesPanelPublico,verbose_name='Panel')
    modulo = ChainedForeignKey(ModulosPublicos,chained_field="seccion",chained_model_field="paneles",show_all=False,auto_choose=True,verbose_name='Modulo',null=True,blank=True)
    #modulo = models.ForeignKey(ModulosPublicos,verbose_name='Modulo')
    submodulo = ChainedForeignKey(SubModulosPublicos,chained_field="modulo",chained_model_field="modulos",show_all=False,auto_choose=True,verbose_name='SubModulo',null=True,blank=True)
    #submodulo = models.ForeignKey(SubModulosPublicos,verbose_name='SubModulo')
    estado = models.BooleanField(verbose_name="Activo")
    class Meta:
        verbose_name_plural='Detalle Grupos de Permisos de Perfil'
        verbose_name = 'Detalle Grupos de Permisos de Perfil'
    def __unicode__(self):
        return u" %s %s"%(self.grupo,self.estado)

