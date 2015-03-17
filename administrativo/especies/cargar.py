# -*- coding: utf8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from especies.models import *
from actores.models import *
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

def InstallStatus(request):
    respuesta = []
	#Estatus Taxon
    try:
        tabla = Tablas(nombre='taxon')
        tabla.save()
        try:
            tipoelemento = Tipoelementos(nombre='Elemento Taxon',tabla=tabla)
            tipoelemento.save()
            print 'Se completo'
            try:
                estatus = Estatus(nombre='Activo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Inactivo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Pendiente',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
            except estatus.DoesNotExist:
                estatus = None
                print 'No se pudo Completar'
        except tipoelemento.DoesNotExist:
            tipoelemento = None
            print 'No se pudo Completar'
    except tabla.DoesNotExist:
        tabla = None
        print 'No se pudo Completar'
    respuesta.append(tabla)
    respuesta.append(tipoelemento)
    respuesta.append(estatus)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	#Estatus TipoTaxon
    try:
        tabla = Tablas(nombre='tipotaxon')
        tabla.save()
        print 'Se completo'
        try:
            tipoelemento = Tipoelementos(nombre='Elemento Tipo Taxon',tabla=tabla)
            tipoelemento.save()
            print 'Se completo'
            try:
                estatus = Estatus(nombre='Activo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Inactivo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Pendiente',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
            except estatus.DoesNotExist:
                estatus = None
                print 'No se pudo Completar'
        except tipoelemento.DoesNotExist:
            tipoelemento = None
            print 'No se pudo Completar'
    except tabla.DoesNotExist:
        tabla = None
        print 'No se pudo Completar'
    respuesta.append(tabla)
    respuesta.append(tipoelemento)
    respuesta.append(estatus)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	#Estatus Estatus Peligros
    try:
        tabla = Tablas(nombre='estatusPeligros')
        tabla.save()
        print 'Se completo'
        try:
            tipoelemento = Tipoelementos(nombre='Elemento Estatus Peligro',tabla=tabla)
            tipoelemento.save()
            print 'Se completo'
            try:
                estatus = Estatus(nombre='Activo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Inactivo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Pendiente',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
            except estatus.DoesNotExist:
                estatus = None
                print 'No se pudo Completar'
        except tipoelemento.DoesNotExist:
            tipoelemento = None
            print 'No se pudo Completar'
    except tabla.DoesNotExist:
        tabla = None
        print 'No se pudo Completar'
    respuesta.append(tabla)
    respuesta.append(tipoelemento)
    respuesta.append(estatus)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	#Estatus Detalle Taxon
    try:
        tabla = Tablas(nombre='detalletaxon')
        tabla.save()
        print 'Se completo'
        try:
            tipoelemento = Tipoelementos(nombre='Elemento Detalle Taxon',tabla=tabla)
            tipoelemento.save()
            print 'Se completo'
            try:
                estatus = Estatus(nombre='Activo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Inactivo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Pendiente',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
            except estatus.DoesNotExist:
                estatus = None
                print 'No se pudo Completar'
        except tipoelemento.DoesNotExist:
            tipoelemento = None
            print 'No se pudo Completar'
    except tabla.DoesNotExist:
        tabla = None
        print 'No se pudo Completar'
    respuesta.append(tabla)
    respuesta.append(tipoelemento)
    respuesta.append(estatus)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	#Estatus Posicion Taxon
    try:
        tabla = Tablas(nombre='posicionTaxon')
        tabla.save()
        print 'Se completo'
        try:
            tipoelemento = Tipoelementos(nombre='Elemento Posicion Taxon',tabla=tabla)
            tipoelemento.save()
            print 'Se completo'
            try:
                estatus = Estatus(nombre='Activo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Inactivo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Pendiente',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
            except estatus.DoesNotExist:
                estatus = None
                print 'No se pudo Completar'
        except tipoelemento.DoesNotExist:
            tipoelemento = None
            print 'No se pudo Completar'
    except tabla.DoesNotExist:
        tabla = None
        print 'No se pudo Completar'
    respuesta.append(tabla)
    respuesta.append(tipoelemento)
    respuesta.append(estatus)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
	#Estatus Tipo Exoticas
    try:
        tabla = Tablas(nombre='tipoExoticas')
        tabla.save()
        print 'Se completo'
        try:
            tipoelemento = Tipoelementos(nombre='Elemento Tipo Exoticas',tabla=tabla)
            tipoelemento.save()
            print 'Se completo'
            try:
                estatus = Estatus(nombre='Activo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Inactivo',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
                estatus = Estatus(nombre='Pendiente',tipoelemento=tipoelemento)
                estatus.save()
                print 'Se completo'
            except estatus.DoesNotExist:
                estatus = None
                print 'No se pudo Completar'
        except tipoelemento.DoesNotExist:
            tipoelemento = None
            print 'No se pudo Completar'
    except tabla.DoesNotExist:
        tabla = None
        print 'No se pudo Completar'
    respuesta.append(tabla)
    respuesta.append(tipoelemento)
    respuesta.append(estatus)
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#
#fecha = datetime.now()
#u = User.objects.get(username ='admin')
#taxti=TipoTaxon(nombre='Imperio',prin=True,descripcion='Imperio',posicion=1,update=fecha,userupdate=u,estatu=0)
#========================================================================================================
#=============================  Imperio =================================================================
#========================================================================================================
	#Tipo Taxon
    fecha = datetime.now()
    u = User.objects.get(username ='admin')
    try:
        taxti = TipoTaxon(nombre='Imperio',prin=True,descripcion='Imperio',posicion=1,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Imperio'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Imperio'
    respuesta.append(taxti)
	
#========================================================================================================
#=============================  Reino =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Imperio')
        taxti = TipoTaxon(nombre='Reino',prin=True,tiptax=tiptaxx,descripcion='Reino',posicion=2,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Reino'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Reino'
    respuesta.append(taxti)	
	
	
#========================================================================================================
#=============================  Sub Reino =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Reino')
        taxti = TipoTaxon(nombre='Subreino',prin=False,descripcion='Subreino',posicion=3,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Subreino'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Subreino'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  Infra Reino =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Subreino')
        taxti = TipoTaxon(nombre='Infrareino',prin=False,tiptax=tiptaxx,descripcion='Infrareino',posicion=4,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Infrareino'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Infrareino'
    respuesta.append(taxti)
	
#========================================================================================================
#=============================  Super Phylum =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Infrareino')
        taxti = TipoTaxon(nombre='Superphylum',prin=False,tiptax=tiptaxx,descripcion='Superphylum',posicion=5,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Superphylum'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Superphylum'
    respuesta.append(taxti)
	
#========================================================================================================
#=============================  Phylum =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Superphylum')
        taxti = TipoTaxon(nombre='Phylum',prin=True,tiptax=tiptaxx,descripcion='Phylum',posicion=6,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Phylum'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Phylum'
    respuesta.append(taxti)
	
#========================================================================================================
#=============================  SubPhylum =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Phylum')
        taxti = TipoTaxon(nombre='Subphylum',prin=False,tiptax=tiptaxx,descripcion='Subphylum',posicion=7,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Subphylum'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Subphylum'
    respuesta.append(taxti)
	
#========================================================================================================
#=============================  InfraPhylum =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Subphylum')
        taxti = TipoTaxon(nombre='Infraphylum',prin=False,tiptax=tiptaxx,descripcion='Infraphylum',posicion=8,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Infraphylum'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Infraphylum'
    respuesta.append(taxti)
	
#========================================================================================================
#=============================  SuperClase =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Infraphylum')
        taxti = TipoTaxon(nombre='Superclase',prin=False,tiptax=tiptaxx,descripcion='Superclase',posicion=9,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo SuperClase'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar SuperClase'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  Clase =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Superclase')
        taxti = TipoTaxon(nombre='Clase',prin=True,tiptax=tiptaxx,descripcion='Clase',posicion=10,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Clase'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Clase'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  SubClase =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Clase')
        taxti = TipoTaxon(nombre='Subclase',prin=False,tiptax=tiptaxx,descripcion='Subclase',posicion=11,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo SubClase'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar SubClase'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  InfraClase =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Subclase')
        taxti = TipoTaxon(nombre='Infraclase',prin=False,tiptax=tiptaxx,descripcion='Infraclase',posicion=12,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo InfraClase'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar InfraClase'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  SuperOrden =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Infraclase')
        taxti = TipoTaxon(nombre='Superorden',prin=False,tiptax=tiptaxx,descripcion='Superorden',posicion=13,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo SuperOrden'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar SuperOrden'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  Orden =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Superorden')
        taxti = TipoTaxon(nombre='Orden',prin=True,tiptax=tiptaxx,descripcion='Orden',posicion=14,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Orden'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Orden'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  SubOrden =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Orden')
        taxti = TipoTaxon(nombre='Suborden',prin=False,tiptax=tiptaxx,descripcion='Suborden',posicion=15,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo SubOrden'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar SubOrden'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  InfraOrden =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Suborden')
        taxti = TipoTaxon(nombre='Infraorden',prin=False,tiptax=tiptaxx,descripcion='Infraorden',posicion=16,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo InfraOrden'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar InfraOrden'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  SuperFamilia =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Infraorden')
        taxti = TipoTaxon(nombre='Superfamilia',prin=False,tiptax=tiptaxx,descripcion='Superfamilia',posicion=17,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo SuperFamilia'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar SuperFamilia'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  Familia =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Superfamilia')
        taxti = TipoTaxon(nombre='Familia',prin=True,tiptax=tiptaxx,descripcion='Familia',posicion=18,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Familia'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Familia'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  SubFamilia =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Familia')
        taxti = TipoTaxon(nombre='Subfamilia',prin=False,tiptax=tiptaxx,descripcion='Subfamilia',posicion=19,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo SubFamilia'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar SubFamilia'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  InfraFamilia =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Subfamilia')
        taxti = TipoTaxon(nombre='Infrafamilia',prin=False,tiptax=tiptaxx,descripcion='Infrafamilia',posicion=20,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo InfraFamilia'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar InfraFamilia'
    respuesta.append(taxti)
	
#========================================================================================================
#=============================  Tribu =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Infrafamilia')
        taxti = TipoTaxon(nombre='Tribu',prin=False,tiptax=tiptaxx,descripcion='Tribu',posicion=21,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Tribu'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Tribu'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  SubTribu =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Tribu')
        taxti = TipoTaxon(nombre='Subtribu',prin=False,tiptax=tiptaxx,descripcion='Subtribu',posicion=22,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo SubTribu'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar SubTribu'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  Genero =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Subtribu')
        taxti = TipoTaxon(nombre='Genero',prin=True,tiptax=tiptaxx,descripcion='Genero',posicion=23,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Genero'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Genero'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  SubGenero =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Genero')
        taxti = TipoTaxon(nombre='Subgenero',prin=False,tiptax=tiptaxx,descripcion='Subgenero',posicion=24,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo SubGenero'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar SubGenero'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  Grex =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Subgenero')
        taxti = TipoTaxon(nombre='Grex',prin=False,tiptax=tiptaxx,descripcion='Grex',posicion=25,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Grex'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Grex'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  Especie =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Grex')
        taxti = TipoTaxon(nombre='Especie',prin=True,tiptax=tiptaxx,descripcion='Especie',posicion=26,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Especie'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Especie'
    respuesta.append(taxti)	
	
#========================================================================================================
#=============================  SubEspecie =================================================================
#========================================================================================================
    try:
        tiptaxx = TipoTaxon.objects.get(nombre='Especie')
        taxti = TipoTaxon(nombre='Subespecie',prin=False,tiptax=tiptaxx,descripcion='Subespecie',posicion=27,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo SubEspecie'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar SubEspecie'
    respuesta.append(taxti)
	
#========================================================================================================
#=============================  Variedad =================================================================
#========================================================================================================
    try:
        taxti = TipoTaxon(nombre='Variedad',prin=False,tiptax=tiptaxx,descripcion='Variedad',posicion=28,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Variedad'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Variedad'
    respuesta.append(taxti)
	
#========================================================================================================
#=============================  Raza =================================================================
#========================================================================================================
    try:
        taxti = TipoTaxon(nombre='Raza',prin=False,tiptax=tiptaxx,descripcion='Raza',posicion=29,update=fecha,userupdate=u,estatu=0)
        taxti.save()
        print 'Se completo Raza'
    except taxti.DoesNotExist:
        taxti = None
        print 'No se pudo Completar Raza'
    respuesta.append(taxti)	
	
    return render_to_response("especies/preCargar.html",{'resp':respuesta}, context_instance=RequestContext(request)) 
	

#========================================================================================================
#=============================  Funcion Lista Escalera ==================================================
#========================================================================================================
def listasEscalera(request):
    try:
       escalera = TipoTaxon.objects.filter(estatu=0)
    except escalera.DoesNotExist:
       escalera = None
    return render_to_response("especies/escalera.html",{'escalera':escalera}, context_instance=RequestContext(request))