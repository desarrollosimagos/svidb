#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from import_export import resources
from import_export import fields
from django.utils.html import strip_tags



from listasTematicas.models import *

# Create your models here.

class Tipomiembros(models.Model):
    nombre = models.CharField(max_length=135)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'tipoMiembros'
        verbose_name_plural='Tipo Miembros'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
        verbose_name = 'Tipo Miembros'
    def __unicode__(self):
        return u"%s" %(self.nombre)

class TipoEventos(models.Model):
    nombre = models.CharField(max_length=135)
    descripcion = models.TextField()
    class Meta:
        db_table = u'tipoEventos'
        verbose_name = 'Tipo Eventos'
        verbose_name_plural='Tipo Eventos'
        #app_label = 'Eventos'
    def __unicode__(self):
        return u"%s" %(self.nombre)

class Modalidads(models.Model):
    nombre = models.CharField(max_length=135)
    genero = models.CharField(max_length=135,null=True,blank=True)
    textosuperior = models.CharField(max_length=135,null=True,blank=True)
    coletilla = models.CharField(max_length=135,null=True,blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    descripcion = models.TextField(verbose_name='Descripción')
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'modalidads'
        verbose_name_plural='Modalidades'
        verbose_name='Modalidades'
        #app_label = 'Eventos'
    def __unicode__(self):
        return u"%s" %(self.nombre)
# ALTER TABLE modalidads ADD COLUMN genero character varying(135);
#ALTER TABLE modalidads ADD COLUMN textosuperior character varying(135);
#ALTER TABLE modalidads ADD COLUMN coletilla character varying(135);        
 
		
class Tematicas(models.Model):
    nombre = models.CharField(max_length=135)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    descripcion = models.TextField(verbose_name='Descripción')
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'tematicas'
        verbose_name_plural='Temáticas'
        verbose_name='Temáticas'
        #app_label = 'Eventos'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
		
class TematicasResource(resources.ModelResource):
    class Meta:
        model = Tematicas


class Eventos(models.Model):
    eventpadre=models.ForeignKey('self',blank=True,null=True, verbose_name='Evento Padre',db_column='eventpadre_id')
    nombre = models.CharField(max_length=300)
    textosf = models.CharField(max_length=120, verbose_name='Textos Configuracion',db_column='texto1',null=True, blank=True)
    coletilla = models.CharField(max_length=120, verbose_name='Coletilla',db_column='coletilla',null=True, blank=True)
    tipoe = models.ForeignKey(TipoEventos,verbose_name='Tipo Eventos')
    lugar = models.CharField(max_length=100)
    descripcion = models.TextField()
    pai = models.ForeignKey(Pais,verbose_name=u'País',null=True)
    estado = ChainedForeignKey(Estados,chained_field="pai",chained_model_field="pai",show_all=False,auto_choose=True,verbose_name='Estado',null=True)
    municipio = ChainedForeignKey(Municipios,chained_field="estado",chained_model_field="estado",verbose_name='Municipio',null=True)
    parroquia = ChainedForeignKey(Parroquias,chained_field="municipio",chained_model_field="municipio",verbose_name='Parroquia',null=True)
	
    capcacidad = models.IntegerField(db_column='capcacidad',null=True,blank=True)
    modalidad = models.ManyToManyField(Modalidads)
    tematicas = models.ManyToManyField(Tematicas)
    pathimg = models.ImageField(upload_to='pathImg',db_column='pathImg',null=True, blank=True) 
    pathimgtop = models.ImageField(upload_to='pathImgTop',db_column='pathImgTop',null=True, blank=True,verbose_name='Header') 
    fecha = models.DateField(null=True, blank=True)
    fechaInicioInscripcion = models.DateField(null=True, blank=True, verbose_name='Fecha cierre de Pre-inscripción')
    fechaFinInscripcion = models.DateField(null=True, blank=True, verbose_name='Fecha cierre de Postulación de Trabajos')
    fechaFin = models.DateField(null=True, blank=True, verbose_name='Fecha fin del congreso',db_column='fechafin')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    bancoaudios = models.ManyToManyField(Bancoaudiovisuals,related_name='Bancos Audio Visuales',help_text=u"Por nombre",verbose_name='Banco Audio Visual',null=True, blank=True)
    biblio = models.ManyToManyField(Bibliotecas,related_name='Biblioteca',help_text=u"Por nombre",verbose_name='Bibliotecas',null=True, blank=True)
    userupdate = models.ForeignKey(User,null=True, blank=True,verbose_name='Usuario ')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente'),(3,'Realizado')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    opt0 = models.BooleanField(db_column='opt0', blank=True,verbose_name='Inscripcion de Trabajos')
    opt1 = models.BooleanField(db_column='opt1', blank=True,verbose_name='Necesita Inscripcion')
    class Meta:
        db_table = u'eventos'
        verbose_name_plural='Eventos'
        verbose_name='Eventos'
        #app_label = 'Eventos'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
class AportesEventos(models.Model):
    nombre = models.CharField(max_length=135)
    class Meta:
        verbose_name_plural='Aportes( Ejemplo: Aporte Financiero, Aporte Material, Aporte Logistico)'
        verbose_name = 'Aportes( Ejemplo: Aporte Financiero, Aporte Material, Aporte Logistico)'
    def __unicode__(self):
        return u"%s" %(self.nombre)
		
class TipoAportesEventos(models.Model):
    aporte = models.ForeignKey(AportesEventos,null=True, blank=True,verbose_name='Aporte')
    nombre = models.CharField(max_length=135)
    class Meta:
        verbose_name_plural='Tipo de Aporte (Ej: Transferencia, Deposito, Libros, Comida, Transporte)'
        verbose_name = 'Tipo de Aporte (Ej: Transferencia, Deposito, Libros, Comida, Transporte)'
    def __unicode__(self):
        return u"%s %s" %(self.aporte, self.nombre)
		
class AportesEventosConfiguracion(models.Model):
    evento = models.ForeignKey(Eventos,null=True, blank=True,verbose_name='Evento')
    aporte = models.ForeignKey(AportesEventos,null=True, blank=True,verbose_name='Aporte')
    tipo = models.ForeignKey(TipoAportesEventos,null=True, blank=True,verbose_name='Tipo de Aporte')
    activar1 = models.BooleanField(blank=True,verbose_name='Activar Campo #1')
    campo1 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #1')
    activar2 = models.BooleanField(blank=True,verbose_name='Activar Campo #2')
    campo2 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #2')
    activar3 = models.BooleanField(blank=True,verbose_name='Activar Campo #3')
    campo3 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #3')
    activar4 = models.BooleanField(blank=True,verbose_name='Activar Campo #4')
    campo4 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #4')
    activar5 = models.BooleanField(blank=True,verbose_name='Activar Campo #5')
    campo5 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #5')
    activar6 = models.BooleanField(blank=True,verbose_name='Activar Campo #6')
    campo6 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #6')
    activar7 = models.BooleanField(blank=True,verbose_name='Activar Campo #7')
    campo7 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #7')
    activar8 = models.BooleanField(blank=True,verbose_name='Activar Campo #8')
    campo8 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #8')
    activar9 = models.BooleanField(blank=True,verbose_name='Activar Campo #9')
    campo9 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #9')
    activar10 = models.BooleanField(blank=True,verbose_name='Activar Campo #10')
    campo10 = models.CharField(max_length=135,null=True, blank=True,verbose_name='Nombre del campo #10')
	
    class Meta:
        verbose_name_plural='Configuracion del Aporte'
        verbose_name = 'Configuracion del Aporte'
    def __unicode__(self):
        return u"%s %s" %(self.aporte, self.evento)
		
class Trabajoscongresos(models.Model):
    SHIRT_SIZES = (
        (1,'Aceptado'),(2,'Rechazado'),(3,'Aceptado con modificaciones'),
    )
    titulo = models.CharField(max_length=450)
    presento = models.BooleanField(blank=True,verbose_name='Presentado',db_column='presento')
    impreso = models.BooleanField(blank=True,verbose_name='Impreso',db_column='impreso')
    armado = models.BooleanField(blank=True,verbose_name='kit de Certificados Armado',db_column='armado')
    entregado = models.BooleanField(blank=True,verbose_name='Entregado',db_column='entregado')
    devueto = models.BooleanField(blank=True,verbose_name='Devuelto por Correcciones',db_column='devueto')
    fundamento = models.ForeignKey(Fundamentos,verbose_name=u'Fundamentos',null=True,blank=True,db_column='fundamentos_id')
    objetivoespecifico = ChainedForeignKey(Objetivoespecificos,chained_field="fundamento",chained_model_field="fundamento",show_all=False,auto_choose=True,verbose_name='Objetivos Especificos',null=True,blank=True,db_column='objetivos_id')
    accionesgenerale = ChainedForeignKey(Accionesgenerales,chained_field="objetivoespecifico",chained_model_field="objetivoespecifico",verbose_name='Acciones Generales',null=True,blank=True,db_column='acciongeneral_id')
    accespecifi = ChainedForeignKey(Accionesespecificas,chained_field="accionesgenerale",chained_model_field="accionesgenerale",verbose_name='Accion Especifica',null=True,blank=True)
    modalidad = models.ForeignKey(Modalidads)
    tematicas = models.ForeignKey(Tematicas,blank=True,null=True)
    resumen = models.TextField()
    evento = models.ForeignKey(Eventos,null=True, blank=True)
    directorio = models.ForeignKey(Directorios,null=True, blank=True,verbose_name='Autor')
    update = models.DateTimeField(default=datetime.now(),editable = False,null=True, blank=True)
    userupdate = models.ForeignKey(User,null=True, blank=True,verbose_name='Usuario')
    coautores = models.ManyToManyField(Directorios,null=True, blank=True,related_name='Co-Autores')
    palabrasclave = models.ManyToManyField(Pablabrasclaves,null=True, blank=True,related_name='Palabras Claves')
    colectivos = models.ManyToManyField(Actores,null=True, blank=True,related_name='Colectivos')
    estatu = models.IntegerField(choices=SHIRT_SIZES,verbose_name='Estatus' ,null=True,blank=True,db_column='estatu_id')
    ambitoaccion = models.CharField(choices=(('0','Global'),('1','Nacional'),('2','Regional'),('3','Municipal'),('3','Local')),max_length=10, blank=True,verbose_name='Ambito de Acción',null=True)
    class Meta:
        db_table = u'trabajosCongresos'
        verbose_name_plural='Trabajos Congreso'
        verbose_name='Trabajos Congreso'
        #app_label = 'Eventos'
    def __unicode__(self):
        return u"%s - %s" %(self.id, self.titulo)
    def titulo_html(self):
        return u" %s"%(self.titulo)	
    titulo_html.allow_tags = True
		
class TrabajoscongresosResource(resources.ModelResource):
    full_coautores = fields.Field()
    full_colectivo = fields.Field()
    full_titulo = fields.Field()
    full_resumen = fields.Field()
    class Meta:
        model = Trabajoscongresos
        fields = ('id','titulo','fundamento__nombre','objetivoespecifico__nombre','accionesgenerale__nombre','accespecifi__nombre','modalidad__nombre','tematicas__nombre','resumen','evento__nombre','full_coautores','full_colectivo','directorio__documentoidentidad','directorio__nombre','directorio__apellido','directorio__telefono1','directorio__correo','coautores','colectivos','estatu')

#        fields = ('id','full_titulo','full_resumen','full_coautores','full_colectivo','directorio__documentoidentidad','directorio__nombre','directorio__apellido','directorio__telefono1','directorio__correo','modalidad__nombre','tematicas__nombre','accespecifi__nombre',)
    def dehydrate_full_coautores(self, trabajoscongresos):
        return '; '.join([obj.nombre + ', ' +obj.apellido for obj in trabajoscongresos.coautores.all()])
    def dehydrate_full_colectivo(self, trabajoscongresos):
        return '; '.join([obj.nombre_completo for obj in trabajoscongresos.colectivos.all()])
    def dehydrate_full_titulo(self, trabajoscongresos):
        t = strip_tags(trabajoscongresos.titulo)
        return '%s' % (t)
    def dehydrate_full_resumen(self, trabajoscongresos):
        t = strip_tags(trabajoscongresos.resumen)
        return '%s' % (t)
		

class Grupotrabajocongresos(models.Model):
    directorio = models.ForeignKey(Directorios)
    trabajoscongreso = models.ForeignKey(Trabajoscongresos,db_column='trabajosCongreso_id')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'grupoTrabajoCongresos'
        verbose_name_plural='Grupos Trabajos Congresos'
        verbose_name='Grupos Trabajos Congresos'
        #app_label = 'Eventos'
    def __unicode__(self):
        return u"%s" %(self.directorio)

class Grupotrabajos(models.Model):
    grupo = models.CharField(max_length=300)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'grupoTrabajos'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
        verbose_name_plural='Grupos Trabajos'
        verbose_name='Grupos Trabajos'
    def __unicode__(self):
        return u"%s" %(self.grupo)

class RelacionGrupoTrabajoAccionEspecifica(models.Model):
    accionesespecifica = models.ForeignKey(Accionesespecificas,db_column='accionesEspecifica_id')
    grupostrabajos = models.ForeignKey(Grupotrabajos,db_column='grupotrabajo_id')
    class Meta:
        db_table = u'relaciongrupotrabajoaccionespecifica'
        verbose_name_plural='Relación Grupos Trabajos - Acción Específica'
        verbose_name='Relación Grupos Trabajos - Acción Específica'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
    def __unicode__(self):
        return u"%s" %(self.accionesespecifica)
		

class Miembrosgrupotrabajos(models.Model):
    tipomiembro = models.ForeignKey(Tipomiembros, null=True, db_column='tipoMiembro_id')
    directorio = models.ForeignKey(Directorios, null=True)
    grupotrabajo = models.ForeignKey(Grupotrabajos, null=True, db_column='grupoTrabajo_id')
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    estatu = models.IntegerField(choices=((0,'Activo'),(1,'Inactivo'),(2,'Pendiente')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'miembrosGrupoTrabajos'
        verbose_name_plural='Miembros Grupos de Trabajo'
        verbose_name='Miembros Grupos de Trabajo'
        #app_label = 'Estrategia_Nacional_y_Plan_de_Accion'
    def __unicode__(self):
        return u"%s" %(self.directorio)
		
		
class participacioEvento(models.Model):
    directorio = models.ForeignKey(Directorios,null=True, blank=True)
    evento = models.ForeignKey(Eventos,null=True, blank=True)
    estatu = models.IntegerField(choices=((0,'Sin evaluar'),(2,'Pre-inscrito'),(3,'Inscrito')),verbose_name='Estatus',null=True,blank=True,db_column='estatu_id')
    class Meta:
        db_table = u'participacioEvento'
        verbose_name_plural='Participacion de Eventos'
        verbose_name='Participacion de Eventos'
    def __unicode__(self):
        return u"%s - %s" %(self.directorio,self.evento)
    def participanteCedula(self):
        return self.directorio.documentoidentidad
    def participanteNombre(self):
        return self.directorio.nombre
    def participanteApellido(self):
        return self.directorio.apellido
    def participanteCorreo(self):
        return self.directorio.correo
    def participanteEstado(self):
        return self.directorio.estado
		
class participacioEventoVarios(models.Model):
    directorio = models.ForeignKey(Directorios,null=True, blank=True)
    evento = models.ForeignKey(Eventos,null=True, blank=True)
    certificado = models.BooleanField(blank=True,verbose_name='certificado')
    material = models.BooleanField(blank=True,verbose_name='material')
    observacion = models.TextField(blank=True,null=True)
    class Meta:
        verbose_name_plural='Participacion de Eventos - Varios'
        verbose_name='Participacion de Eventos - Varios'
    def ImprimirCertificado(self):
        return u"<a href='/panel/coord/certificados/participacion/%s/%s' target='_blank'>Generar Certificado</a>"%(self.evento.id,self.directorio.id)
    ImprimirCertificado.allow_tags = True
    def __unicode__(self):
        return u"%s - %s" %(self.directorio,self.evento)

class participacioEventoVariosResource(resources.ModelResource):
    class Meta:
        model = Trabajoscongresos
        fields = ('directorio__documentoidentidad','directorio__nombre','directorio__apellido','directorio__telefono1','directorio__correo','directorio__estado')
		
class SeguimientoTrabajos(models.Model):
    trabajo = models.ForeignKey(Trabajoscongresos,null=True, blank=True)
    impreso = models.BooleanField(blank=True,verbose_name='Impreso')
    armado = models.BooleanField(blank=True,verbose_name='kit de Certificados Armado')
    entregado = models.BooleanField(blank=True,verbose_name='Entregado')
    devueto = models.BooleanField(blank=True,verbose_name='Devuelto por Correcciones')
    class Meta:
        verbose_name_plural='Seguimiento de Trabajos'
        verbose_name='Seguimiento de Trabajos'
    def __unicode__(self):
        return u"%s" %(self.trabajo)


		
class participacioEventoAporte(models.Model):
    directorio = models.ForeignKey(Directorios,null=True, blank=True)
    evento = models.ForeignKey(Eventos,null=True, blank=True)
    campo1 = models.CharField(max_length=135,null=True, blank=True)
    campo2 = models.CharField(max_length=135,null=True, blank=True)
    campo3 = models.CharField(max_length=135,null=True, blank=True)
    campo4 = models.CharField(max_length=135,null=True, blank=True)
    campo5 = models.CharField(max_length=135,null=True, blank=True)
    campo6 = models.CharField(max_length=135,null=True, blank=True)
    campo7 = models.CharField(max_length=135,null=True, blank=True)
    campo8 = models.CharField(max_length=135,null=True, blank=True)
    campo9 = models.CharField(max_length=135,null=True, blank=True)
    campo10 = models.CharField(max_length=135,null=True, blank=True)
    class Meta:
        verbose_name_plural='Participacion de Eventos - Aporte'
        verbose_name='Participacion de Eventos - Aporte'
    def __unicode__(self):
        return u"%s - %s" %(self.directorio,self.evento)

class TipoLogistica(models.Model):
    evento = models.ForeignKey(Eventos,null=True, blank=True)
    nombre = models.CharField(max_length=135)
    class Meta:
        verbose_name_plural='Tipo de Logistica'
        verbose_name = 'Tipo de Logistica'
    def __unicode__(self):
        return u"%s" %(self.nombre)

class CoordinadorLogistica(models.Model):
    tipo = models.ForeignKey(TipoLogistica,null=True, blank=True)
    directorio = models.ForeignKey(Directorios,null=True, blank=True,verbose_name='Coordinador')
    descripcion = models.TextField()
    class Meta:
        verbose_name_plural='Coordinacion de Logistica'
        verbose_name = 'Coordinacion de Logistica'
    def __unicode__(self):
        return u"%s %s" %(self.tipo.nombre,self.directorio)
	
class MiembrosLogistica(models.Model):
    evento = models.ForeignKey(Eventos,null=True, blank=True)
    tipo = ChainedForeignKey(TipoLogistica,chained_field="evento",chained_model_field="evento",show_all=False,auto_choose=True,verbose_name='Tipo Logistica',null=True)
    coordinacion = ChainedForeignKey(CoordinadorLogistica,chained_field="tipo",chained_model_field="tipo",verbose_name='Coordinacion',null=True)
    directorio = models.ForeignKey(Directorios,null=True, blank=True,verbose_name='Miembro')
    class Meta:
        db_table = u'miembroslogistica'
        verbose_name_plural='Miembros de Logistica'
        verbose_name = 'Miembros de Logistica'
    def __unicode__(self):
        return u"%s %s" %(self.coordinacion,self.directorio)
		
		
class ProgramaCursos(models.Model):
    evento = models.ForeignKey(Eventos,null=True, blank=True)
    programa = models.TextField()
    class Meta:
        verbose_name_plural='Programa de Cursos'
        verbose_name = 'Programa de Cursos'
    def __unicode__(self):
        return u"%s" %(self.evento)
