# -*- coding: utf8
from django.db import models
from actores.models import *


from os import path
import Image

TINY_SIZE = (80,80)



from django.conf import settings

# Create your models here.

class Estatuspeligros(models.Model):
    tipo = models.CharField(max_length=135)
    descripcion = models.TextField()
    class Meta:
        db_table = u'estatusPeligros'
        verbose_name_plural='Estatus de Peligros'
        verbose_name='Estatus de Peligros'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u" %s %s"%(self.tipo,self.descripcion)


class TipoTaxon(models.Model):
    nombre = models.CharField(max_length=150)
    prin = models.BooleanField(verbose_name='Principal')
    tiptax=models.ForeignKey('self',blank=True,null=True, verbose_name='Dependencia Tipo Taxon')
    descripcion = models.TextField(blank=True,null=True)
    posicion = models.IntegerField(blank=True,null=True)
    update = models.DateTimeField(default=datetime.now(),editable = False,blank=True,null=True)
    userupdate = models.ForeignKey(User,blank=True,null=True)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'tipotaxon'
        verbose_name_plural='Tipo Taxón'
        verbose_name='Tipo Taxón'
        unique_together=('nombre','estatu')
        #app_label = 'Especies_y_Taxones'
    def __unicode__(self):
        return u" %s %s"%(self.nombre,self.estatu)

		
class DetalleTaxon(models.Model):
#    taxon = models.ForeignKey(Taxon,verbose_name='Taxón')
    descripcionmorfologica = models.TextField(db_column='descripcionMorfologica', blank=True, verbose_name='Descripción Morfologica')
    bancoaudio = models.ManyToManyField(Bancoaudiovisuals,related_name='Bancos Audiovisuales para Especies',help_text=u"Por nombre",verbose_name='Banco AudioVisual',null=True, blank=True)
    habitad = models.TextField(blank=True,verbose_name='Hábitat')
    distribucion = models.TextField(blank=True,verbose_name='Distribución')
	
    esptraf = models.BooleanField(verbose_name='Especies Sometidas al Tráfico o Comercio Ilícito')
    espaprove = models.BooleanField(verbose_name='Especies para el Aprovechamiento Sustentable')
    espsalud = models.BooleanField(verbose_name='Especies de Impacto sobre la Salud Humana')
    esppeligr = models.BooleanField(verbose_name='Especies de Animales en Peligro de Extinción y Árboles en Veda')
    espexot = models.BooleanField(verbose_name='Especies Exóticas o Introducidas')
    espagrico = models.BooleanField(verbose_name='Especies de Impacto sobre la Producción Agropecuaria y Forestal')
	
    habitos = models.TextField(blank=True,verbose_name='Hábitos')
    particularidades = models.TextField(blank=True)
    bibliografia = models.ManyToManyField(Bibliotecas, blank=True,null=True,verbose_name='Bibliografía')
    mapas = models.ManyToManyField(Mapas, blank=True,null=True)
    enlaces = models.ManyToManyField(EnlacesExternos,blank=True, verbose_name='Enlaces',related_name='url2')
    aspectoslegales = models.TextField(db_column='aspectosLegales', blank=True,verbose_name='Aspectos Legales')
    reproduccion = models.TextField(blank=True,verbose_name='Reproducción y/o Longevidad')

    iniconserv = models.TextField(blank=True,verbose_name='Iniciativas para su Conservación')
    maniscultura = models.ManyToManyField(Manifestacionesculturales,verbose_name='Manifestaciones Culturales',null=True, blank=True,related_name='Manifestaciones Culturales')
    glosario = models.ManyToManyField(Glosario,verbose_name='Glosario',related_name='Glosario',null=True, blank=True)
    bioregion = models.ManyToManyField(Bioregions,verbose_name='Biorregiones',null=True, blank=True,related_name='Bio-regiones')
    docasocia = models.ManyToManyField(Bibliotecas, blank=True,verbose_name='Documentos Asociados',related_name='Doc. Asociados')
    url = models.ManyToManyField(EnlacesExternos,null=True, blank=True,verbose_name='Paginas Web',related_name='url1')	
    userupdate = models.ForeignKey(User,verbose_name='Usted es?',null=True,blank=True)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'detalletaxon'
        verbose_name_plural='Detalle Taxón'
        verbose_name='Detalle Taxón'
        #app_label = 'Especies_y_Taxones'
    def Taxones(self):
        try:
           tax = Taxon.objects.get(detalletaxon=self)
        except Taxon.DoesNotExist:
           tax = None
        return u" %s <span style='font-style:italic;'>(%s %s)</span>"%(tax.nombrecomun,tax.taxonrelax.nombre,tax.nombre)	
    Taxones.allow_tags = True

    def VerTaxon(self):
        try:
           tax = Taxon.objects.get(detalletaxon=self)
        except Taxon.DoesNotExist:
           tax = None
        return u"<a href='/manager/especies/taxon/%s'>Ver Taxon</a>"%(tax.id)
    VerTaxon.allow_tags = True

    def Estatus(self):
        esta = ""
        if self.estatu:
           if self.estatu == 0:
              esta = "<img src='/static/admin/img/admin/icon-yes.gif' alt='Activo'> Activo"
           if self.estatu == 1:
              esta = "<img src='/static/admin/img/admin/icon-no.gif' alt='Inactivo'> Inactivo"
           if self.estatu == 2:
              esta = "<img src='/media/imgs/icon-pendiente.gif' alt='Pendiente'> Pendiente"
        else:
           esta = "<img src='/media/imgs/icon-pendiente.gif' alt='Pendiente'> Sin estatus"
        return u"%s"%(esta)
    Estatus.allow_tags = True

    def __unicode__(self):
        return u" %s"%(self.id)	
		
class Taxon(models.Model):
    subtipo = models.ForeignKey(TipoTaxon,verbose_name='Nivel Taxón',null=True,blank=True)
    otroNombreNivel = models.CharField(max_length=135,blank=True, null=True,verbose_name='Otro nombre Nivel Taxón',db_column='otronombrenivel')
    nombre = models.CharField(max_length=135,blank=True, null=True)
    autorespecie = models.CharField(max_length=135, db_column='autorEspecie', blank=True,verbose_name='Autor')
    nombrecomun = models.CharField(max_length=600, db_column='nombreComun', blank=True,verbose_name='Nombre Común')
    otrosnombrec = models.CharField(max_length=150, db_column='otrosNombreC', blank=True, verbose_name='Otros Nombres Comunes')
    actor = models.ManyToManyField(Actores,verbose_name='Organizaciones',blank=True,null=True)
    direct = models.ManyToManyField(Directorios,verbose_name='Personas',blank=True, null=True)
    comentariotaxonomico = models.TextField(db_column='comentarioTaxonomico', blank=True,verbose_name='Comentario Taxonómico')
    filogenia = models.IntegerField(blank=True,null=True,verbose_name='Filogenia')
    endemica = models.BooleanField(blank=True, verbose_name='Endémica')
    extinto = models.BooleanField(verbose_name='Extinto')
    taxonrelax=models.ForeignKey('self',blank=True,null=True, verbose_name='Relación Taxón')
    detalletaxon = models.ForeignKey(DetalleTaxon,verbose_name='Detalle Taxon',db_column='datelletaxontt_id',blank=True, null=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'taxon'
        verbose_name_plural='Taxón'
        verbose_name='Taxón'
        #app_label = 'Especies_y_Taxones'
    def __unicode__(self):
        return u" %s %s"%(self.subtipo, self.nombre)
#    def get_image_filename(self):
#        return '%s%s' % (settings.MEDIA_ROOT, self.pathimg, )
#    def get_image_url(self):
#        return '%s%s' % (settings.MEDIA_URL, self.pathimg, )
#    def show_thumb(self):
#        tiny = path.join(path.dirname(self.get_image_filename()), 'tiny', str(self.pathimg))
#        if not path.exists(tiny):
#           im = Image.open(self.get_image_filename())
#           im.thumbnail(TINY_SIZE, Image.ANTIALIAS)
#           if not path.exists(path.dirname(tiny)):
#               from os import makedirs
#               makedirs(path.dirname(tiny))
#           im.save(tiny, 'JPEG')
#        tiny_url = path.join(path.dirname(self.get_image_url()), 'tiny', str(self.pathimg))
#        return '<a href="%s/"><img src="%s" alt="tiny thumbnail image"/></a>' % (self.id, tiny_url)
#    show_thumb.allow_tags = True
#    show_thumb.short_description = ''
	

class tipoAprovechamientoSustentable(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True,null=True)
    class Meta:
        db_table = u'tipoaprovechasustentable'
        verbose_name_plural='Tipo de Aprovechamiento Sustentable'
        verbose_name='Tipo de Aprovechamiento Sustentable'
        #app_label = 'Detalle_Especie'
    def __unicode__(self):
        return u" %s"%(self.tipo)


class Tipoexoticas(models.Model):
    nombre = models.CharField(max_length=180)
    tipo = models.CharField(max_length=20, choices=(('1','Tipo de Especie Exótica'),('2','Distribución Ecológica'),('3','Impacto'),('4','Tipo de Introducción')))
    descripcion = models.TextField(verbose_name='Descripcion',blank=True,null=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'tipoExoticas'
        #app_label = 'Detalle_Especie'
        verbose_name_plural='Tipo Exóticas'
        verbose_name='Tipo Exóticas'
    def __unicode__(self):
        return u" %s %s"%(self.nombre,self.tipo)

class MatrixRelacionTaxon(models.Model):
    imperio = models.ForeignKey(Taxon,verbose_name='Imperio',null=True,blank=True,related_name='imperio')
    reino = models.ForeignKey(Taxon,verbose_name='Reino',null=True,blank=True,related_name='reino')
    subreino = models.ForeignKey(Taxon,verbose_name='Sub-Reino',null=True,blank=True,related_name='subreino')
    infrareino = models.ForeignKey(Taxon,verbose_name='Infra-Reino',null=True,blank=True,related_name='infrareino')
    superphylum = models.ForeignKey(Taxon,verbose_name='Super-Phylum',null=True,blank=True,related_name='superphylum')
    phylum = models.ForeignKey(Taxon,verbose_name='Phylum',null=True,blank=True,related_name='phylum')
    subphylum = models.ForeignKey(Taxon,verbose_name='Sub-Phylum',null=True,blank=True,related_name='subphylum')
    infraphylum = models.ForeignKey(Taxon,verbose_name='Infra-Phylum',null=True,blank=True,related_name='infraphylum')
    superclase = models.ForeignKey(Taxon,verbose_name='SuperClase',null=True,blank=True,related_name='superclase')
    clase = models.ForeignKey(Taxon,verbose_name='Clase',null=True,blank=True,related_name='clase')
    subclase = models.ForeignKey(Taxon,verbose_name='Sub-Clase',null=True,blank=True,related_name='subclase')
    infraclase = models.ForeignKey(Taxon,verbose_name='Infra-Clase',null=True,blank=True,related_name='infraclase')
    superorden = models.ForeignKey(Taxon,verbose_name='Super-Orden',null=True,blank=True,related_name='superorden')
    orden = models.ForeignKey(Taxon,verbose_name='Orden',null=True,blank=True,related_name='orden')
    suborden = models.ForeignKey(Taxon,verbose_name='Sub-Orden',null=True,blank=True,related_name='suborden')
    infraorden = models.ForeignKey(Taxon,verbose_name='Infra-Orden',null=True,blank=True,related_name='infraorden')
    superfamilia = models.ForeignKey(Taxon,verbose_name='Super-Familia',null=True,blank=True,related_name='superfamilia')
    familia = models.ForeignKey(Taxon,verbose_name='Familia',null=True,blank=True,related_name='familia')
    subfamilia = models.ForeignKey(Taxon,verbose_name='Sub-Familia',null=True,blank=True,related_name='subfamilia')
    infrafamilia = models.ForeignKey(Taxon,verbose_name='Infra-Familia',null=True,blank=True,related_name='infrafamilia')
    tribu = models.ForeignKey(Taxon,verbose_name='Tribu',null=True,blank=True,related_name='tribu')
    subtribu = models.ForeignKey(Taxon,verbose_name='Sub-Tribu',null=True,blank=True,related_name='subtribu')
    genero = models.ForeignKey(Taxon,verbose_name='Genero',null=True,blank=True,related_name='genero')
    subgenero = models.ForeignKey(Taxon,verbose_name='Sub-Genero',null=True,blank=True,related_name='subgenero')
    grex = models.ForeignKey(Taxon,verbose_name='Grex',null=True,blank=True,related_name='grex')
    especie = models.ForeignKey(Taxon,verbose_name='Especie',null=True,blank=True,related_name='especie')
    subespecie = models.ForeignKey(Taxon,verbose_name='Sub-Especie',null=True,blank=True,related_name='subespecie')
    variedad = models.ForeignKey(Taxon,verbose_name='Variedad',null=True,blank=True,related_name='variedad')
    raza = models.ForeignKey(Taxon,verbose_name='Raza',null=True,blank=True,related_name='raza')
    class Meta:
        verbose_name_plural='Matriz de Relacion de Taxon'
        verbose_name='Matriz de Relacion de Taxon'
    def __unicode__(self):
        return u" %s"%(self.especie)
    
