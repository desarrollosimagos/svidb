#!/usr/bin/python -u
# -*- coding: utf-8 -*-
#01
from django.db import models
from django.db.models import Max
from demografia.models import *
from linea.models import *
from documentos.models import *
from menu.models import *

from os import *
import uuid
import os
import shutil
from django.conf import settings
import Image

TINY_SIZE = (80,80)

from datetime import datetime
from django.contrib.auth.models import User
from stdimage import StdImageField

from django_google_maps.fields import AddressField, GeoLocationField



class Tipoareaaccions(models.Model):
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    descripcion = models.TextField(blank=True,verbose_name='Descripción')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usted es?')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'tipoAreaAccions'
        verbose_name_plural='Áreas de Acción'
        verbose_name = 'Áreas de Acción'

    def __unicode__(self):
        return u"%s" %(self.nombre)

class Directorios(models.Model):
    tipodoci = models.IntegerField(choices=((0,'Venezolano'),(1,'Extranjero'),(2,'Pasaporte'),(3,u'Cédula Escolar')), verbose_name='Tipo de Documento')
    sexo = models.IntegerField(choices=((0,'Masculino'),(1,'Femenino'),(2,u'Diversidad Sexual')), verbose_name='Género', blank=True,null=True)
    edocivil = models.IntegerField(choices=((0,'Soltero(a)'),(1,'Casado(a)'),(2,'Divorciado(a)'),(3,'Viudo(a)')), verbose_name='Estado Civil',null=True)
    nacimiento = models.DateField(verbose_name='Fecha de Nacimiento (DD/MM/AAAA)')
#    documentoidentidad = models.IntegerField(verbose_name='Documento de Identidad',unique=True,help_text=u"Ingrese un numero de documento de Identidad Valido..")
    documentoidentidad = models.CharField(max_length=75,verbose_name='Documento de Identidad',unique=True,help_text=u"Ingrese un número de documento de Identidad Válido.")
    areasaccion = models.ManyToManyField(Tipoareaaccions,related_name='Areas de Accion',help_text=u"Seleccione las principales áreas de acción de su trabajo. Para seleccionar más de una opción Manten presionado Control, o Command.",verbose_name=u'Áreas de Acción',blank=True)
    nombre = models.CharField(max_length=180,verbose_name='Nombre')
    apellido = models.CharField(max_length=180,verbose_name='Apellido')
#    correo = models.EmailField(verbose_name='Correo Electrónico',unique=True,null=True,blank=True )
    correo = models.EmailField(max_length=250,verbose_name='Correo Electrónico (Solo para Notificaciones)',null=True,blank=True)
    telefono1 = models.CharField(max_length=135, blank=True,verbose_name='Teléfono #1')
    telefono2 = models.CharField(max_length=135, blank=True, verbose_name='Teléfono #2')
    fax = models.CharField(max_length=135, blank=True,verbose_name='Fax')
    movil = models.CharField(max_length=135, blank=True,verbose_name='Celular')
    sector = models.TextField(blank=True,verbose_name='Sector')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    pai = models.ForeignKey(Pais,verbose_name=u'País',null=True)
    estado = ChainedForeignKey(Estados,chained_field="pai",chained_model_field="pai",show_all=False,auto_choose=True,verbose_name='Estado',null=True)
    municipio = ChainedForeignKey(Municipios,chained_field="estado",chained_model_field="estado",verbose_name='Municipio',null=True)
    parroquia = ChainedForeignKey(Parroquias,chained_field="municipio",chained_model_field="municipio",verbose_name='Parroquia',null=True)
    suscritobool = models.BooleanField(db_column='suscritoBool', blank=True,verbose_name='Suscribir?')
    organizacion = models.CharField(max_length=135,blank=True,null=True)
    gruposespecie = models.TextField(db_column='gruposEspecie', blank=True, verbose_name='Especies o grupos biológicos con los que trabaja principalmente')
    localidadesaccion = models.TextField(db_column='localidadesAccion', blank=True, verbose_name='Localidad de Accion')
    listacorreos = models.ManyToManyField(ListasCorreos,related_name='listascrreos',verbose_name='Listas de Correos',blank=True,null=True)
    ocupacion = models.CharField(blank=True,null=True,max_length=50)
    userupdate = models.ForeignKey(User,verbose_name='Usted es?',null=True,blank=True)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    fund = models.ManyToManyField(Fundamentos,verbose_name='Fundamentos',null=True,blank=True)
    class Meta:
        db_table = u'directorios'
        verbose_name_plural='Personas'
        verbose_name = 'Persona'
        #app_label = 'Actores'
    def __unicode__(self):
        return u"%s  - %s - %s " %(self.nombre, self.apellido, self.correo)
    def AreasAccion(self):
        return ', '.join([obj.nombre for obj in self.areasaccion.all()])


class Bancoaudiovisuals(models.Model):
    TIPO_BAN = (
        ('0','Fotografia'),('1','Video'),('2','Audio'),('3','Ilustracion')
    )
    directorio = models.ForeignKey(Directorios, null=True, blank=True,verbose_name='Autor')
    fecha = models.CharField(max_length=135,blank=True,null=True)
    lugar = models.TextField(blank=True)
    descripcion = models.TextField(blank=True,verbose_name='Descripción')
    tipo = models.CharField(choices=TIPO_BAN,max_length=135)
    pathimg = StdImageField(upload_to='Bancoaudiovisuals',size=None, thumbnail_size=(157,118), verbose_name='Archivo')
#    pathimg = StdImageField(upload_to='Bancoaudiovisuals',size=None, thumbnail_size=(157,118), micro_size=(59,59), mini_size=(118,118),verbose_name='Archivo')
    licencia = models.ForeignKey(Licencias)
    observaciones = models.TextField(blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Pendiente'),(1,'Activo sin vínculo'),(2,'Activo con vínculo')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    url = models.ForeignKey(EnlacesExternos,null=True, blank=True)
    seccion = models.CharField(choices=(('0','Areas'),('1','Especies'),('2','Actores'),('3','Manifestaciones Culturales'),('4','Biorregiones'),('5','Eventos y Actividades')),max_length=135, blank=True)
    def retorno_nombre(self):
        name, extension = os.path.splitext(self.pathimg.name)
        return name
    def retorno_extencion(self):
        name, extension = os.path.splitext(self.pathimg.name)
        return extension
    class Meta:
        db_table = u'bancoAudiovisuals'
        verbose_name_plural='Bancos Audiovisual'
        verbose_name = 'Banco Audiovisual'
        #app_label = 'Datos_Transversales'
    def __unicode__(self):
        return u"ID: %s " %(self.id)
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
#        return '<a href="%s/"><img src="pathImg/Bancoaudiovisuals/pathimg_%s" alt="tiny thumbnail image"/></a>' % (self.id, tiny_url)
#        return '<a href="%s/"><img src="/media/Bancoaudiovisuals/pathimg_%s.jpeg" alt="tiny thumbnail image"/></a>' % (self.id,self.id)
#        return '<a href="%s/"><img src="/media/Bancoaudiovisuals/pathimg_%s.59_59.jpeg" alt="tiny thumbnail image"/></a>' % (self.id,self.id)
#    show_thumb.allow_tags = True
#    show_thumb.short_description = ''
#    def mostrar_html(self):
 #       return '%s' % (self.descripcion)
  #  mostrar_html.allow_tags = True
#    mostrar_html.short_description = ''


class Actores(models.Model):
    tiposAreasAccion = models.ManyToManyField(Tipoareaaccions,related_name='Areas de Acciones',help_text=u"Por nombre",verbose_name='Areas de Accion', blank=True)
    actoresrex=models.ForeignKey('self',blank=True,null=True, verbose_name='Actores Relación')
    bancoaudio = models.ManyToManyField(Bancoaudiovisuals,related_name='Banco Audiovisual',help_text=u"Por nombre",verbose_name='Banco AudioVisual',null=True, blank=True)
    horarios = models.TextField(blank=True,null=True)
    fund = models.ManyToManyField(Fundamentos,verbose_name='Fundamentos',null=True, blank=True)
    url = models.ManyToManyField(EnlacesExternos,null=True, blank=True,verbose_name='Paginas Web')
    ambitoaccion = models.CharField(choices=(('0','Global'),('1','Nacional'),('2','Regional'),('3','Municipal'),('3','Local')),max_length=10, blank=True,verbose_name='Ambito de Acción',null=True)
    principalesorgfinan = models.TextField(db_column='principalesOrgFinan', blank=True,verbose_name='Princ. Organismos Financieros',null=True)
    objetivos = models.TextField(blank=True,verbose_name='Objetivos',null=True)
    publicacionesPeriodicas = models.TextField(blank=True,verbose_name='Publicaciones Periodicas',null=True)
    aniofundacion = models.CharField(max_length=5,null=True, db_column='anioFundacion', blank=True,verbose_name='Año de Fundación')
    telefono = models.CharField(max_length=60, blank=True,verbose_name='Teléfono',null=True)
    fax = models.CharField(max_length=60, blank=True,verbose_name='Fax',null=True)
    address = AddressField(max_length=100,verbose_name='Ubicación en Mapa',null=True, blank=True)
    geolocation = GeoLocationField(blank=True,verbose_name='Coordenadas')
    rif = models.CharField(max_length=135,verbose_name='RIF',blank=True,null=True)
    siglas = models.CharField(max_length=135, blank=True,verbose_name='Siglas',null=True)
    nombre = models.CharField(max_length=135,blank=True,verbose_name='Razón Social',null=True)
    nombre_completo = models.CharField(max_length=135,verbose_name='Nombre Completo',null=True, blank=True)
    direccion = models.TextField(blank=True,verbose_name='Dirección')
    pai = models.ForeignKey(Pais,verbose_name='País',null=True, blank=True)
    estado = ChainedForeignKey(Estados,chained_field="pai",chained_model_field="pai",show_all=False,auto_choose=True,verbose_name='Estado',null=True, blank=True)
    municipio = ChainedForeignKey(Municipios,chained_field="estado",chained_model_field="estado",verbose_name='Municipio',null=True, blank=True)
    parroquia = ChainedForeignKey(Parroquias,chained_field="municipio",chained_model_field="municipio",verbose_name='Parroquia',null=True, blank=True)
    correo = models.CharField(max_length=150, blank=True,verbose_name='Correo Electronico',null=True)
    reseniahistorica = models.TextField(db_column='reseniaHistorica', blank=True, verbose_name='Reseña Histórica',null=True)
    pubp = models.TextField(db_column='pubp', blank=True, verbose_name='Publicaciones Periódicas',null=True)
    grupobio = models.TextField(db_column='grupoBio', blank=True, verbose_name='Grupo Biológico',null=True)
    logotipo = models.ImageField(blank=True, verbose_name='logotipo',upload_to='media/actores',null=True)
    categoriact = models.ForeignKey(Categorias,verbose_name='Categorias',null=True,blank=True)
    tipocolec = ChainedForeignKey(SubTipoCategorias,chained_field="categoriact",chained_model_field="categoria",show_all=False,auto_choose=True,verbose_name='Subcategorias',null=True, blank=True)
    particularidades = models.TextField(blank=True,verbose_name='Particularidades',null=True)
    estrOrganz = models.TextField(blank=True,verbose_name='Estructura Organizativa',null=True)
    actinteres = models.TextField(db_column='actInteres', blank=True, verbose_name='Programas y Proyectos',null=True)
    numeromiembros = models.IntegerField(null=True, db_column='numeroMiembros', blank=True, verbose_name='Número de Miembros')
    coord = models.CharField(max_length=100, verbose_name='Datos de GPS',blank=True,null=True)
    estrucorg = models.TextField(verbose_name='Estructura Organizativa', blank=True, null=True)
    tipoorganizacion = models.ForeignKey(Tipoorganizacions, null=True, db_column='tipoOrganizacion_id', blank=True,verbose_name='Tipo de Organización')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usted es?',null=True,blank=True)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    areasesconserv = models.TextField(verbose_name='Áreas Estrategicas para la Conservación',null=True,blank=True)
    directorio = models.ForeignKey(Directorios,verbose_name='Responsable Autorizado',null=True,blank=True)
    class Meta:
        db_table = u'actores'
        verbose_name_plural='Actores Colectivos'
        #app_label = 'Actores'
        verbose_name = 'Actores Colectivos'
    def __unicode__(self):
        return u"%s %s" %(self.siglas, self.nombre)

class ActoresCCModificados(models.Model):
    actorbase = models.OneToOneField(Actores,related_name='actor0')
    actorupdate = models.OneToOneField(Actores,related_name='actor1')	
    class Meta:
        db_table = u'actores_modificaciones'
        verbose_name_plural='Actores Colectivos Modificaciones'
        verbose_name = 'Actores ColectivosModificaciones'
    def __unicode__(self):
        return u"%s %s" %(self.actorbase, self.actorupdate)	


class DetalleBiblioteca(models.Model):
    actore = models.ForeignKey(Actores)
    lugar = models.CharField(max_length=135, blank=True,verbose_name='Coleccion')
    estante = models.CharField(max_length=135, blank=True,verbose_name='Estante')
    cota = models.CharField(max_length=25, blank=True,verbose_name='Cota')
    presta = models.BooleanField(verbose_name='Prestamos')
    fecha = models.DateField(verbose_name='Fecha de Devolucion',blank=True,null=True)
    class Meta:
        db_table = u'detallebiblioteca'
        verbose_name_plural='Detalles Bibliotecas'
        verbose_name = 'Detalle Biblioteca'
        #app_label = 'Datos_Transversales'
    def __unicode__(self):
        return u"%s %s" %(self.lugar, self.estante)


def tuplify(x): return (x,x)


current_year = datetime.now().year
YEARS = map(tuplify, range(1700, current_year + 1)) 


class Bibliotecas(models.Model):
    titulo = models.CharField(max_length=450)
    fecha = models.IntegerField(max_length=2, choices=YEARS, verbose_name='Fecha de Publicación')
    autores = models.CharField(max_length=450, blank=True)
    directorio = models.ForeignKey(Directorios,related_name='Persona',help_text=u"Por nombre",verbose_name='Persona',blank=True, null=True)
    editorial = models.TextField(blank=True)
    ibsn = models.CharField(max_length=135, blank=True)
    edicion = models.CharField(max_length=45, blank=True)
    numerovolumen = models.CharField(max_length=45, db_column='numeroVolumen', blank=True)
    resumen = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    biblioteca = models.ManyToManyField(DetalleBiblioteca,related_name='Biblioteca',help_text=u"Por nombre",verbose_name='Bibliotecas',null=True, blank=True)
    tipodocs = models.IntegerField(choices=((0,'Libro'),(1,'Tesis de Grado'),(2,'Documentos Legales'),(3,'Documentos Sub-Legales'),(4,'Diccionarios'),(5,'Informes Tecnicos'),(6,'Articulos en Revistas'),(7,'Revistas Cientificas'),(8,'Revistas Divulgativas'),(9,'Boletines'),(10,'Presentaciones'),(11,'Carteles'),(12,'Atlas'),(13,'Afiches'),(14,'Carteles'),(15,'Guias'),(16,u'Material Divulgativo')),verbose_name='Tipo Documentos',null=True,blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    autorinstitucional = models.TextField(db_column='autorInstitucional', blank=True)
    idioma = models.CharField(max_length=60, blank=True)
    numeropaginas = models.IntegerField(null=True, db_column='numeroPaginas', blank=True,verbose_name='Paginas')
    repositoriolinea = models.FileField(upload_to='bibliotecas',verbose_name='Archivo',blank=True,null=True,help_text="Solo se permiten documentos en formato PDF.")
    licencia = models.ForeignKey(Licencias, null=True, blank=True)
    class Meta:
        db_table = u'bibliotecas'
        verbose_name_plural='Biblioteca'
        #app_label = 'Datos_Transversales'
        verbose_name = 'Biblioteca'
#    def save(self, *args, **kwargs):
#        from os import *
#        na,ext = os.path.splitext(self.repositoriolinea.name)
#        #print self.repositoriolinea
#        bob = Bibliotecas.objects.aggregate(Max('id'))
#        max = bob['id__max'] + 1
#        nombrefile = u"biblioteca_%s%s" %(max, ext)
#        self.id = max
#        os.rename(self.repositoriolinea, nombrefile)
        #super(Blog, self).save(*args, **kwargs)
    def save(self, *args, **kwargs):
        super(Bibliotecas, self).save()
        if self.repositoriolinea:
           orignal_nzb = u'%(1)s%(2)s' % {'1': settings.MEDIA_ROOT, '2': self.repositoriolinea}
           renamed_nzb = u'%(1)sbibliotecas/%(2)s_%(3)s.pdf' % {'1': settings.MEDIA_ROOT, '2': 'biblioteca', '3': self.pk}
           if orignal_nzb not in renamed_nzb:
              if os.path.isfile(renamed_nzb):
                 os.remove(renamed_nzb)
              os.rename(orignal_nzb, renamed_nzb)
           self.repositoriolinea = 'bibliotecas/%(1)s_%(2)s.pdf' % {'1': 'biblioteca', '2': self.pk}
           super(Bibliotecas, self).save()

    def delete(self, *args, **kwargs):
        if self.repositoriolinea:
           self.repositoriolinea.delete()
           super(Bibliotecas, self).delete(*args, **kwargs)

    def __unicode__(self):
        return u"%s %s" %(self.fecha, self.autores)
		
class DocAsocActores(models.Model):
    actores = models.ForeignKey(Actores)
    blibliote = models.ForeignKey(Bibliotecas)
    class Meta:
        db_table = u'docasocactores'
        verbose_name_plural='Documentos Asociados'
        app_label = 'Datos_Transversales'

        verbose_name = 'Documentos Asociados'
    def __unicode__(self):
        return u"%s %s" %(self.actores, self.blibliote)

		
class Manifestacionesculturales(models.Model):
    titulo = models.CharField(max_length=300)
    descripcion = models.TextField(verbose_name='Descripción')
    bancoaudio = models.ManyToManyField(Bancoaudiovisuals,related_name='Bancos AudioVisuales',help_text=u"Por nombre",verbose_name='Banco AudioVisual',null=True, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    biblio = models.ManyToManyField(Bibliotecas, related_name='biblios',verbose_name='Bibliografía',blank=True, null = True)
    bibliog = models.ManyToManyField(Bibliotecas, related_name='bibliog',verbose_name='Documentos Asociados',blank=True, null = True)
    url = models.ManyToManyField(EnlacesExternos,null=True, blank=True,verbose_name='Paginas Web',related_name='url8')
    tipo = models.ForeignKey(TiposManifestaciones) 
    userupdate = models.ForeignKey(User, verbose_name='Usuario') 
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'manifestacionesCulturales'
        verbose_name_plural='Manifestaciones Culturales'
        #app_label = 'Datos_Transversales' 
        verbose_name = 'Manifestaciones Culturales'
    def __unicode__(self):
        return u" %s %s"%(self.titulo,self.estatu)


class Bioregions(models.Model):
    nombre = models.CharField(max_length=100)
    superficie =  models.CharField(max_length=20,blank=True,null=True)
    ubicacion = models.TextField(blank=True,null=True)
    altitud = models.CharField(max_length=20,blank=True,null=True)
    geologia = models.TextField(blank=True,null=True)
    geomorfologia = models.TextField(blank=True,null=True)
    hidrografia = models.TextField(blank=True,null=True)
    clima = models.TextField(blank=True,null=True)
    suelos = models.TextField(blank=True,null=True)
    ecosistemas = models.TextField(blank=True,null=True)
    impactos_antropicos = models.TextField(blank=True,null=True)
	
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
	
    bancoaudio = models.ManyToManyField(Bancoaudiovisuals,related_name='Bancos3',help_text=u"Por nombre",verbose_name='Banco Audiovisual',null=True, blank=True)
    mapas = models.ManyToManyField(Mapas,related_name='mapas2',verbose_name='Mapas',blank=True)
    docasocia = models.ManyToManyField(Bibliotecas,related_name='docasocs1',verbose_name='Documentos Asociados',blank=True,null=True)
    glosar = models.ManyToManyField(Glosario,related_name='glosari',verbose_name='Glosario',blank=True)
    manisf = models.ManyToManyField(Manifestacionesculturales,related_name='manisff1',verbose_name='Manifestaciones Culturales',blank=True)
    enlaces = models.ManyToManyField(EnlacesExternos,null=True, blank=True,verbose_name='Enlaces',related_name='url5')
	
    bibliografia = models.ManyToManyField(Bibliotecas,related_name='Bibliografia',help_text=u"Por nombre",verbose_name='Bibliografias',blank=True,null=True)
    url = models.ManyToManyField(EnlacesExternos,null=True, blank=True,verbose_name='Paginas Web',related_name='url4')
	
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'bioRegions'
        verbose_name_plural='Biorregiones'
        #app_label = 'Datos_Transversales'
        verbose_name = 'Biorregiones'
    def __unicode__(self):
        return u"%s" %(self.nombre)


class MiembrosdeInstituciones(models.Model):
    institucion = models.ForeignKey(Actores)
    miembros = models.ManyToManyField(Directorios, related_name='bibliogd',verbose_name='Miembros',blank=True, null = True)
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        verbose_name_plural='Miembros de Actores Colectivos'
        #app_label = 'Datos_Transversales' 
        verbose_name = 'Miembros de Actores Colectivos'
    def __unicode__(self):
        return u" %s %s"%(self.institucion,self.estatu)
		
		
class SistemaMensajeria(models.Model):
    remi = models.ForeignKey(Directorios,verbose_name='Remitente')
    destino = models.ManyToManyField(Directorios, related_name='bibliogw',verbose_name='Destinatarios',blank=True, null = True)
    asunto = models.CharField(max_length=120,blank=True,null=True)
    mensaje = models.TextField(blank=True,null=True)
    estatu = models.IntegerField(choices=((0,'Borrador'),(1,'Enviado'),(2,'Leido')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    fecha = models.DateTimeField(default=datetime.now(),editable = False)
    class Meta:
        verbose_name_plural='Sistema de Mensajeria'
        #app_label = 'Datos_Transversales' 
        verbose_name = 'Sistema de Mensajeria'
    def __unicode__(self):
        return u" %s %s"%(self.remi,self.estatu)
