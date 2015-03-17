#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from especies.models import *



# Create your models here.



class Areas(models.Model):
    nombre = models.CharField(max_length=300)
    areasrex=models.ForeignKey('self',blank=True,null=True, verbose_name='Relacion Areas')
    datecreado = models.DateField(null=True, db_column='dateCreado', blank=True,verbose_name='Fecha de Creación')
    biblioteca = models.ManyToManyField(Bibliotecas,verbose_name='Documentos de Creación',related_name='doccre',blank=True,null=True)
    objetocreado = models.TextField(db_column='objetoCreado', blank=True,verbose_name='Objetivo de Creación')
    geomorfo = models.TextField(blank=True,verbose_name='Geomorfología')
    clima = models.TextField(blank=True,verbose_name='Clima')
    hidrografia = models.TextField(blank=True,verbose_name='Hidrografía')
    particuld = models.TextField(blank=True,verbose_name='Particularidades')
    ubicpol = models.ManyToManyField(Parroquias,related_name='Ubicacion Politico T.',help_text=u"Por nombre",verbose_name='Ubicacion Politico Territorial',null=True, blank=True)
    geologia = models.TextField(blank=True,verbose_name='Geología')
    suelos = models.TextField(blank=True,verbose_name='Suelos')
    comolle = models.TextField(blank=True,verbose_name='Como llegar')
    ecosistema = models.TextField(blank=True,verbose_name='Ecosistemas')
    categoriact = models.ForeignKey(Categorias,verbose_name='Categorias',null=True,blank=True)
    subtipoas = ChainedForeignKey(SubTipoCategorias,chained_field="categoriact",chained_model_field="categoria",show_all=False,auto_choose=True,verbose_name='Subcategoria',null=True, blank=True)
    altitud = models.CharField(blank=True,max_length=300,verbose_name='Altitud')
    superficie = models.CharField(blank=True,max_length=300,verbose_name='Superficie')
    bancoaudio = models.ManyToManyField(Bancoaudiovisuals,related_name='Bancos AudioVisuales para Areas',help_text=u"Por nombre",verbose_name='Banco Audiovisual',null=True, blank=True)
    descricion = models.TextField(blank=True,verbose_name='Descripción General')
    asentahumanos = models.TextField(db_column='asentaHumanos', blank=True,verbose_name='Asentamientos Humanos')
    planorden = models.ManyToManyField(Bibliotecas,related_name='planorden',verbose_name='Plan de Orden y/o Reglamentos de Uso',blank=True,null=True)
    servic = models.ManyToManyField(Servicios,verbose_name='Servicios',related_name='servi',blank=True,null=True)
    horario = models.TextField(blank=True,null=True,verbose_name='Horario')
    comollegar = models.TextField(db_column='comoLlegar', blank=True,verbose_name='¿Cómo llegar?')
    bibliografia = models.ManyToManyField(Bibliotecas, blank=True,related_name='bibliogra',verbose_name='Bibliografías')
    concesiones = models.TextField(blank=True,verbose_name='Concesiones')
    bioregion = models.ManyToManyField(Bioregions, null=True, blank=True,verbose_name='Ubicación Biorregional')
    siglas = models.CharField(max_length=135, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    actore = models.ManyToManyField(Actores, null=True, blank=True,verbose_name='Organismos de Adscripción',related_name='OrgAdsc')
    orgcolab = models.ManyToManyField(Actores, null=True, blank=True,verbose_name='Actores Colaboradores',related_name='OrgCola')
    personacolab = models.ManyToManyField(Directorios, null=True, blank=True,verbose_name='Directorio Colaboradores',related_name='DirCola')
    esprepretxt = models.TextField(verbose_name='Especies Representativas Textos',blank=True)
    esprepre = models.ManyToManyField(Taxon,related_name='esperes',verbose_name='Especies Representativas',blank=True)
    impacantro = models.TextField(verbose_name='Impactos Antrópicos',blank=True)
    inicpart = models.TextField(verbose_name='Iniciativas y Participación Social',blank=True)
    tipoyusrecur = models.TextField(verbose_name='Tipo y Uso de Recursos Naturales',blank=True)
    enlancs = models.ManyToManyField(EnlacesExternos,related_name='enlacse',verbose_name='Enlaces Externos',blank=True)
    docasocia = models.ManyToManyField(Bibliotecas,related_name='docasocs',verbose_name='Documentos Asociados',blank=True,null=True)
    manisf = models.ManyToManyField(Manifestacionesculturales,related_name='manisff',verbose_name='Manifestaciones Culturales',blank=True)
    mapas = models.ManyToManyField(Mapas,related_name='mapas3',verbose_name='Mapas',blank=True)
    glosar = models.ManyToManyField(Glosario,related_name='glosar',verbose_name='Glosario',blank=True)
    url = models.ManyToManyField(EnlacesExternos,null=True, blank=True,verbose_name='Paginas Web',related_name='url3')	
    class Meta:
        db_table = u'areas'
        verbose_name_plural='Áreas'        
        #app_label = 'Areas_Estrategicas_para_la_Conservacion'
        verbose_name = 'Áreas'
    def __unicode__(self):
        return u"%s %s" %(self.nombre, self.siglas)

class RedessocialesAreas(models.Model):
    area = models.ForeignKey(Areas, null=True, blank=True)
    red = models.ForeignKey(Reds, null=True, blank=True)
    url = models.URLField(max_length=300)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'redesSocialesAreas'
        verbose_name_plural='Redes Sociales'
        verbose_name = 'Redes Sociales'
    def __unicode__(self):
        return u"%s %s" %(self.red,self.area)

class ServiciosArea(models.Model):
    area = models.ForeignKey(Areas, null=True, blank=True)
    servicios = models.ForeignKey(Servicios, null=True, blank=True)
    class Meta:
        db_table = u'serviciosArea'
        verbose_name_plural='Relación Áreas-Servicios'        
        #app_label = 'Areas_Estrategicas_para_la_Conservacion'
        verbose_name = 'Relación Áreas-Servicios'
    def __unicode__(self):
        return u"%s" %(self.area)

class Ubicacions(models.Model):
    area = models.ForeignKey(Areas, null=True, blank=True)
    parroquia = models.ForeignKey(Parroquias, null=True, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'ubicacions'
        verbose_name_plural='Relación Áreas-Demografía'
        verbose_name = 'Relación Áreas-Demografía'
        #app_label = 'Areas_Estrategicas_para_la_Conservacion'
    def __unicode__(self):
        return u"%s" %(self.area)

