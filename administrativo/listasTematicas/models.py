#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from inicio.models import *

#from gestion.models import *
#from areas.models import *

class TipoAgricola(models.Model):
    titulo = models.CharField(max_length=135)
    descripcion =  models.TextField()
    class Meta:
        db_table = u'sptipoagricola'
        verbose_name_plural='Tipo Especies Agrícolas'
        verbose_name='Tipo Especies Agrícolas'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.titulo)

class Spagricolas(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    tipo = models.ManyToManyField(TipoAgricola,blank=True, null=True)
    alternativas = models.TextField(verbose_name='Alternativas Ecológicas',blank=True, null=True)
    impactoagricola = models.TextField(db_column='impactoAgricola', blank=True,null=True,verbose_name='Impacto sobre la producción agropecuaria')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table= u'spAgricolas'
        verbose_name_plural='Especies de impacto sobre la produción agropecuaria'
        verbose_name='Especies de impacto sobre la produción agropecuaria'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)


class TipoAprovechable(models.Model):
    titulo = models.CharField(max_length=135,verbose_name='Titulo')
    descripcion =  models.TextField(verbose_name='Descripción')
    class Meta:
        db_table = u'sptipoaprovechable'
        verbose_name_plural='Tipo Especies Aprovechables'
        verbose_name='Tipo Especies Aprovechables'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.titulo)

class Spaprovechables(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    usoaprovecha = models.TextField(db_column='usoAprovecha', null=True,blank=True,verbose_name='Uso Aprovechable')
    tipo = models.ForeignKey(TipoAprovechable,blank=True, null=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuarios')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'spAprovechables'
        verbose_name_plural='Especies Aprovechables'
        verbose_name='Especies Aprovechables'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)

class Spaprovechamientosustentables(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    tipoaprosus = models.ManyToManyField(tipoAprovechamientoSustentable,verbose_name='Tipo Aprovechamiento Sustentable',blank=True, null=True)
    usoaprovecha = models.TextField(db_column='usoAprovecha', blank=True,null=True,verbose_name='Uso y Aprovechamiento')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'spAprovechamientoSustentables'
        verbose_name_plural='Especies para el Aprovechamiento Sustentable'
        verbose_name='Especies para el Aprovechamiento Sustentable'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)

class Spexoticas(models.Model):
    exotica = models.ManyToManyField(Tipoexoticas,related_name='tipexo2',blank=True, null=True)
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    impacto = models.TextField(blank=True,verbose_name='Impacto sobre la diversidad biológica',null=True)
    esppeligr = models.BooleanField(verbose_name='Traslocada Regional')
    metodoinic = models.TextField(db_column='metodoInic', blank=True,verbose_name='Métodos para su control',null=True)
    inicontrol = models.TextField(blank=True,verbose_name='Iniciativas para su Control',null=True) 
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'spExoticas'
        verbose_name_plural='Especies Exóticas'
        verbose_name='Especies Exóticas'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)

class Sppeligros(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    amenazas = models.TextField(blank=True,null=True)
    metoconserv = models.TextField(blank=True,verbose_name='Metodos para su Conservación',null=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    estatuspeligro = models.ForeignKey(Estatuspeligros, null=True, db_column='estatusPeligro_id', blank=True,verbose_name='Estatus peligro')
    class Meta:
        db_table = u'spPeligros'
        verbose_name_plural='Especies en Peligro de Extinción'
        verbose_name='Especies en Peligro de Extinción'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)

class Sprepresentativaas(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    area = models.ForeignKey(Areas, null=True, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'spRepresentativaAs'
        verbose_name_plural='Especies Representativas'
        verbose_name='Especies Representativas'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)
		
class Spsaludtipos(models.Model):
    tipo = models.CharField(max_length=135)
    descripcion = models.TextField()
    class Meta:
        db_table = u'spSaludTipos'
        verbose_name_plural='Tipos de Especie Salud'
        verbose_name='Tipos de Especie Salud'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.tipo)

class Spsaluds(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    importanciasalud = models.TextField(db_column='importanciaSalud', blank=True,null=True,verbose_name='Importancia para la salud')
    metodoinic = models.TextField(db_column='metodoInic', blank=True, null=True,verbose_name='Iniciativas para su control y/o propagación') 
    metocontrol = models.TextField(verbose_name='Metodos para su control y/o propagación',blank=True,null=True) 
    tipo = models.ManyToManyField(Spsaludtipos,related_name='Tipos1',blank=True, null=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'spSaluds'
        verbose_name_plural='Especies de impacto para la Salud Humana'
        verbose_name='Especies de impacto para la Salud Humana'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)

class Sptraficos(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    finestraficlic = models.TextField(db_column='finesTraficLic', blank=True, null=True,verbose_name='Fines del tráfico ilícito')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'spTraficos'
        verbose_name_plural='Especies sometidas al tráfico ilícito'
        verbose_name='Especies sometidas al tráfico ilícito'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)


#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::: SISTEMA DE CONTROL DE MODIFICACIONES DE TAXONES :::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Spagricolamods(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    tipo = models.ManyToManyField(TipoAgricola)
    alternativas = models.TextField(verbose_name='Alternativas Ecológicas')
    impactoagricola = models.TextField(db_column='impactoAgricola', blank=True,verbose_name='Impacto sobre la producción agropecuaria')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    spagricola = models.ForeignKey(Spagricolas, null=True, db_column='spAgricola_id', blank=True)
    class Meta:
        db_table = u'spAgricolaMods'
        verbose_name_plural='Especies de impacto sobre la produción agropecuaria - Modificaciones'
        verbose_name='Especies de impacto sobre la produción agropecuaria - Modificaciones'
        #app_label = 'Sistema_de_Modificaciones_Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)


class Spaprovechablemods(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    usoaprovecha = models.TextField(db_column='usoAprovecha', blank=True,verbose_name='Uso Aprovechable')
    tipo = models.ForeignKey(TipoAprovechable)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuarios')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    spaprovechable = models.ForeignKey(Spaprovechables, null=True, db_column='spAprovechable_id', blank=True)
    class Meta:
        db_table = u'spAprovechableMods'
        verbose_name_plural='Especies Aprovechables - Modificiaciones'
        verbose_name='Especies Aprovechables - Modificiaciones'
        #app_label = 'Sistema_de_Modificaciones_Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)

class Spaprovechamientosustentablemods(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    tipoaprosus = models.ManyToManyField(tipoAprovechamientoSustentable,blank=True, verbose_name='Tipo Aprovechamiento Sustentable')
    usoaprovecha = models.TextField(db_column='usoAprovecha', blank=True,verbose_name='Uso y Aprovechamiento')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    spaprovechamientosustentable = models.ForeignKey(Spaprovechamientosustentables, null=True, db_column='spAprovechamientoSustentable_id', blank=True)
    class Meta:
        db_table = u'spAprovechamientoSustentableMods'
        verbose_name_plural='Especies para el Aprovechamiento Sustentable'
        verbose_name='Especies para el Aprovechamiento Sustentable'
        #app_label = 'Sistema_de_Modificaciones_Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)


class Spexoticamods(models.Model):
    exotica = models.ManyToManyField(Tipoexoticas,related_name='tipexo1')
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    impacto = models.TextField(blank=True,verbose_name='Impacto sobre la diversidad biológica')
    esppeligr = models.BooleanField(verbose_name='Traslocada Regional')
    metodoinic = models.TextField(db_column='metodoInic', blank=True,verbose_name='Métodos para su control')
    inicontrol = models.TextField(blank=True,verbose_name='Iniciativas para su Control') 
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    spexotica = models.ForeignKey(Spexoticas, null=True, db_column='spExotica_id', blank=True)
    class Meta:
        db_table = u'spExoticaMods'
        verbose_name_plural='Especies Exóticas'
        verbose_name='Especies Exóticas - Modificaciones'
        #app_label = 'Sistema_de_Modificaciones_Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)


class Sppeligromods(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    amenazas = models.TextField(blank=True)
    metoconserv = models.TextField(blank=True,verbose_name='Metodos para su Conservación')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    estatuspeligro = models.ForeignKey(Estatuspeligros, null=True, db_column='estatusPeligro_id', blank=True,verbose_name='Estatus peligro')
    sppeligro = models.ForeignKey(Sppeligros, null=True, db_column='spPeligro_id', blank=True)
    class Meta:
        db_table = u'spPeligroMods'
        verbose_name_plural='Especies en Peligro de Extinción - Modificaciones'
        verbose_name='Especies en Peligro de Extinción - Modificaciones'
        #app_label = 'Sistema_de_Modificaciones_Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)


class SprepresentativaasMods(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    area = models.ForeignKey(Areas, null=True, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    sprepresentativa = models.ForeignKey(Sprepresentativaas,verbose_name='Id especie Representativa')
    class Meta:
        db_table = u'spRepresentativaAsMods'
        verbose_name_plural='Especies Representativas - Modificaciones'
        verbose_name='Especies Representativas - Modificaciones'
        #app_label = 'Sistema_de_Modificaciones_Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)


class Spsaludmods(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    importanciasalud = models.TextField(db_column='importanciaSalud', blank=True,verbose_name='Importancia para la salud')
    metodoinic = models.TextField(db_column='metodoInic', blank=True,verbose_name='Iniciativas para su control y/o propagación') 
    metocontrol = models.TextField(verbose_name='Metodos para su control y/o propagación',blank=True) 
    tipo = models.ManyToManyField(Spsaludtipos,related_name='Tipos2')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'spSaludMods'
        verbose_name='Especies de impacto para la Salud Humana - Modificaciones'
        verbose_name_plural='Especies de impacto para la Salud Humana - Modificaciones'
        #app_label = 'Sistema_de_Modificaciones_Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)


class Sptraficomods(models.Model):
    especie = models.ForeignKey(DetalleTaxon,verbose_name='Taxón')
    finestraficlic = models.TextField(db_column='finesTraficLic', blank=True) # Field name made lowercase.
    iniconserv = models.TextField(db_column='iniConserv', blank=True) # Field name made lowercase.
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    sptrafico = models.ForeignKey(Sptraficos, null=True, db_column='spTrafico_id', blank=True) # Field name made lowercase.
    pathimg = models.ImageField(upload_to='pathImg',db_column='pathImg') 
    class Meta:
        db_table = u'spTraficoMods'
        verbose_name_plural='Especies sometidas al tráfico ilícito - Modificaciones'
        verbose_name='Especies sometidas al tráfico ilícito - Modificaciones'
        #app_label = 'Sistema_de_Modificaciones_Detalle_Especie'
    def __unicode__(self):
        return u"%s" %(self.especie)

