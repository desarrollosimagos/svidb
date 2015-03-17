#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models

from os import *
import uuid
import os
import shutil

import Image
from listasTematicas.models import *
from datetime import datetime
from django.db.models import Q


from smart_selects.db_fields import ChainedForeignKey 
# Create your models here.

class GeoLocalizaion(models.Model):
    address = AddressField(max_length=100,verbose_name='Direccion')
    geolocation = GeoLocationField(blank=True,verbose_name='Coordenadas')
    class Meta:
        verbose_name_plural='GeoPortal'
        verbose_name='GeoPortal'
        ##app_label = 'Pruebas'
	

class Avistamientos(models.Model):
    fecha = models.DateTimeField(default=datetime.now(),editable = False)
    persona = models.ForeignKey(Directorios, null=True, blank=True,verbose_name='Cedula')
    especie = models.ForeignKey(Taxon)
    fechaAvistamiento = models.DateTimeField(verbose_name='Fecha de Avistamiento')
    desde = models.CharField(max_length=180,verbose_name='Desde')
    address = AddressField(max_length=100,verbose_name='lugar',help_text='Para agregar un lugar escriba una ciudad y localidad, haga clic fuera del mapa y arrastre el indicador a la ubicación precisa. Las coordenadas de la ubicación apareceran en el campo inferior.')
    geolocation = GeoLocationField(blank=True,verbose_name='coordenadas')
    pai = models.ForeignKey(Pais,verbose_name='Pais',blank=True,null=True)
    estado = ChainedForeignKey(Estados,chained_field="pai",chained_model_field="pai",show_all=False,auto_choose=True,verbose_name='Estado',null=True,blank=True)
    municipio = ChainedForeignKey(Municipios,chained_field="estado",chained_model_field="estado",verbose_name='Municipio',null=True,blank=True)
    parroquia = ChainedForeignKey(Parroquias,chained_field="municipio",chained_model_field="municipio",verbose_name='Parroquia',null=True,blank=True)
    sector = models.CharField(max_length=180,verbose_name='Sector')
    puntor = models.CharField(max_length=180,verbose_name='Punto de Referencia',blank=True,null=True)
    gps = models.CharField(max_length=180,verbose_name='Datos de GPS',blank=True,null=True)
    entorno = models.CharField(max_length=180,verbose_name='Entorno', blank=True, null=True)
    numero = models.IntegerField(verbose_name='Numero de Individuos',blank=True, null=True)
    tamaniop = models.IntegerField(verbose_name='Tamaño Promedio (cm)',blank=True, null=True)
    medidasc = models.CharField(choices=(('0','si'),('1','no')),max_length=2, blank=True,verbose_name='Utilizo Medidas de Control')
    pathimg1 = models.ImageField(upload_to='avistamientos',db_column='pathImg1',verbose_name='Imagen',null=True,blank=True) 
    cuamedida = models.CharField(max_length=180,verbose_name='Cuales?',blank=True, null=True)
    frecuencia = models.CharField(choices=(('0','Mensual'),('1','Semanal'),('2','Diaria'),('2','Esporádica')),max_length=2, blank=True,verbose_name='Frecuencia de la Medida de Control')
    estatu = models.IntegerField(choices=((0,'Validados'),(1,'Reportes Web'),(2,'Pendiente'),(3,'Denegado')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    observaciones = models.TextField(blank=True,null=True)
    class Meta:
        db_table = u'avistamientos'
        verbose_name_plural='Avistamientos Especies Exóticas'
        verbose_name='Avistamientos Especies Exóticas'
        ##app_label = 'Reporte_de_Avistamiento_de_Especies'
    def save(self, *args, **kwargs):
        super(Avistamientos, self).save()
        if self.pathimg1:
           # Create the system paths we need.
           orignal_nzb = u'%(1)s%(2)s' % {'1': settings.MEDIA_ROOT, '2': self.pathimg1}
           na,ext = os.path.splitext(self.pathimg1.name)
           renamed_nzb = u'%(1)savistamientos/%(2)s_%(3)s%(4)s' % {'1': settings.MEDIA_ROOT, '2': 'avistamiento', '3': self.pk,'4' : ext}
           # Rename the file.
           if orignal_nzb not in renamed_nzb:
               if os.path.isfile(renamed_nzb):
                  os.remove(renamed_nzb)
               # Fails when name is updated.
               os.rename(orignal_nzb, renamed_nzb)
           self.pathimg1 = 'avistamientos/%(1)s_%(2)s%(3)s' % {'1': 'avistamiento', '2': self.pk, '3' : ext}
           super(Avistamientos, self).save()
    def delete(self, *args, **kwargs):
        if self.pathimg1:
           self.pathimg1.delete()
           super(Avistamientos, self).delete(*args, **kwargs)
    def lat(self):
        lats = self.geolocation.lat
        return lats
    def lng(self):
        lngs = self.geolocation.lon
        return lngs
    def positivo(self):
        pos = puntosAvistamientos.objects.filter(Q(avistamiento=self) & Q(opinion=0)).count()
        return pos
    def negativo(self):
        neg = puntosAvistamientos.objects.filter(Q(avistamiento=self) & Q(opinion=1)).count()
        return neg
    def __unicode__(self):
        return u"%s %s" %(self.especie.nombre, self.persona)


		
class puntosAvistamientos(models.Model):
    update = models.DateTimeField(default=datetime.now(),editable = False)
    avistamiento = models.ForeignKey(Avistamientos, null=True, blank=True,verbose_name='Avistamiento')
    persona = models.ForeignKey(Directorios, null=True, blank=True,verbose_name='Persona')
    opinion = models.IntegerField(choices=((0,'Verdad'),(1,'Falso')),verbose_name='Opinion')
    class Meta:
        verbose_name_plural='Calificaciones Avistamientos'
        verbose_name='Calificaciones Avistamientos'
    def __unicode__(self):
        return u"%s" %(self.avistamiento)

class Etnias(models.Model):
    nombre = models.CharField(max_length=150)
    otrosnombre = models.TextField(db_column='otrosNombre', blank=True) # Field name made lowercase.
    descripcion = models.TextField(blank=True)
    descripcionge = models.TextField(blank=True,verbose_name='Descripción General')
    vivienda = models.TextField(null=True, blank=True)
    subsistencia = models.TextField(null=True, blank=True)
    vidasosial = models.TextField(null=True, blank=True)
    distribucion = models.TextField(blank=True,null=True)
    idioma = models.TextField(blank=True,null=True)

    especierepre = models.ManyToManyField(Taxon,related_name='Taxon',help_text=u"Por nombre",null=True, blank=True)
    actvinc = models.ManyToManyField(Actores,related_name='Actores Vinculados',verbose_name='Actores Vinculados',help_text=u"Por nombre",null=True, blank=True)
    bancaudio = models.ManyToManyField(Bancoaudiovisuals,related_name='Banco AudioVisuales', verbose_name='Banco AudioVisual',help_text=u"Por nombre",null=True, blank=True)
    biblio = models.ManyToManyField(Bibliotecas,related_name='bibliotk',verbose_name='Bibliotecas',help_text=u"Por nombre",null=True, blank=True)
    bibliogra = models.ManyToManyField(Bibliotecas,related_name='Bibliografias',verbose_name='Bibliografia',help_text=u"Por nombre",null=True, blank=True)
    enlaces = models.ManyToManyField(EnlacesExternos,related_name='Enlaces Externos', verbose_name='Enlaces Externos', help_text=u"Por nombre",null=True, blank=True)
    url = models.ManyToManyField(EnlacesExternos,related_name='url6', verbose_name='Paginas Web', help_text=u"Por nombre",null=True, blank=True)
    manisfes = models.ManyToManyField(Manifestacionesculturales,related_name='manifs', verbose_name='Manifestaciones Culturales', help_text=u"Por nombre",null=True, blank=True)

    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'etnias'
        ##app_label = 'Datos_Transversales'
        verbose_name_plural='Etnias'
        verbose_name='Etnias'
    def __unicode__(self):
        return u"%s" %(self.nombre)

class Etniaareas(models.Model):
    etnia = models.ForeignKey(Etnias, null=True, blank=True)
    area = models.ForeignKey(Areas, null=True, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'etniaAreas'
        verbose_name_plural='Relación Areas-Etnias'
        verbose_name='Relación Areas-Etnias'
        ##app_label = 'Areas_Estrategicas_para_la_Conservacion'
    def __unicode__(self):
        return u"%s" %(self.etnia)
		
#class Mapasareas(models.Model):
#    mapas = models.ForeignKey(Mapas, null=True, blank=True)
#    area = models.ForeignKey(Areas, null=True, blank=True)
#    update = models.DateTimeField(default=datetime.now(),editable = False)
#    userupdate = models.ForeignKey(User,verbose_name='Usuario')
#    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
#    class Meta:
#        db_table = u'mapasAreas'
#        verbose_name_plural='Relación Areas-Mapas'
#        verbose_name='Relación Areas-Mapas'
#        ##app_label = 'Areas_Estrategicas_para_la_Conservacion'
#    def __unicode__(self):
#        return u"%s" %(self.etnia)

		
class Colaboradorespersonas(models.Model):
    fecha = models.DateField()
    tipoColaboracion = models.ForeignKey(Tipocolaboracion)
    cultural = models.ForeignKey(Manifestacionesculturales,blank=True,null=True)
    colectivos = models.ForeignKey(Actores,blank=True,null=True)
    areas = models.ForeignKey(Areas,blank=True,null=True)
    etnias = models.ForeignKey(Etnias,blank=True,null=True)
    mapas = models.ForeignKey(Mapas,blank=True,null=True)
    bioregiones = models.ForeignKey(Bioregions,blank=True,null=True)
    taxon = models.ForeignKey(Taxon,blank=True,null=True)
    titulo= models.CharField(max_length=150)
    descripcion = models.TextField(null=True,blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    persona = models.ForeignKey(Directorios,verbose_name='Persona')
    solisgcc = models.IntegerField(verbose_name='SGCC',blank=True,null=True)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente'),(3,u'Colaboracion Web')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'colaboradoresPersonas'
        verbose_name_plural='Sistematización de Contribuciones'
        verbose_name='Sistematización de Contribuciones'
        ##app_label = 'Construccion_Colectiva'

    def Estatus(self):
        if self.estatu:
           if self.estatu == 0:
              esta = "<img src='/static/admin/img/admin/icon-yes.gif' alt='Activo'> Activo"
           if self.estatu == 1:
              esta = "<img src='/static/admin/img/admin/icon-no.gif' alt='Inactivo'> Inactivo"
           if self.estatu == 2:
              esta = "<img src='/media/librerias/imgs/icon-pendiente.gif' alt='Pendiente'> Pendiente"
           if self.estatu == 3:
              esta = "<img src='/media/librerias/imgs/icon-pendiente1.gif' alt='Pendiente'> Pendiente"
        else:
           esta = "<img src='/media/librerias/imgs/icon-pendiente1.gif' alt='Pendiente'> Sin estatus" 
        return u"%s"%(esta)
    Estatus.allow_tags = True
    def __unicode__(self):
        return u"%s" %(self.persona)
		
class contriBiblioteca(models.Model):
    contribucion = models.ForeignKey(Colaboradorespersonas)
    boblioteca = models.ForeignKey(Bibliotecas)
    def __unicode__(self):
        return u"%s" %(self.contribucion)

class contriAudio(models.Model):
    contribucion = models.ForeignKey(Colaboradorespersonas)
    audio = models.ForeignKey(Bancoaudiovisuals)
    def __unicode__(self):
        return u"%s" %(self.contribucion)

class contriAvistamiento(models.Model):
    contribucion = models.ForeignKey(Colaboradorespersonas)
    avistamiento = models.ForeignKey(Avistamientos)
    def __unicode__(self):
        return u"%s" %(self.contribucion)