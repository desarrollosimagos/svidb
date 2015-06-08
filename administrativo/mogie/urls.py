# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mogie',
    url(r'^admin$', 'views.admin', name="mogie"),
    
    url(r'^iniciar$', 'views.IniciarSesion', name="mogie"),
    
    url(r'^comentarios/guardar$', 'views.agregarComentario', name="mogie"),
    
    url(r'^salir$', 'views.logout', name="mogie"),
    
    url(r'^perfil$', 'views.editarPerfilUsuario', name="mogie"),
    
    url(r'^perfil/foto/guardar$', 'views.agregarFotoPerfil', name="mogie"),
    
    url(r'^perfil/datos/guardar$', 'views.GuardarPerfil', name="mogie"),
    
    url(r'^perfil/nuevo/crear$', 'views.RegistrarUsuarios', name="mogie"),
    
    url(r'^eventos/(\d+)$', 'views.verEvento', name="mogie"),
    
    url(r'^eventos/pagina/(\d+)$', 'views.eventos', name="mogie"),
    
    url(r'^eventos/pagina/activos/(\d+)$', 'views.eventosActivos', name="mogie"),
    
    url(r'^eventos/pagina/proximos/(\d+)$', 'views.eventosProximos', name="mogie"),
    
    url(r'^eventos/pagina/realizados/(\d+)$', 'views.eventosRealizados', name="mogie"),
    
    url(r'^eventos/detalle/(\d+)$', 'views.detalleEvento', name="mogie"),
    
    url(r'^eventos/preinscripcion/(\d+)$', 'views.preinscripcionEvento', name="mogie"),
    
    url(r'^eventos/preinscripcion/registro/(\d+)/(\d+)$', 'views.preinscripcionColaboracionEvento', name="mogie"),
    
    url(r'^eventos/resumenes/(\d+)/(\d+)$', 'views.postulacionResumenes', name="mogie"),
    
    url(r'^eventos/resumen/(\d+)$', 'views.SegundoPasoPostulacion', name="mogie"),
    
    url(r'^eventos/resumen/coautores/(\d+)$', 'views.TercerPasoPostulacion', name="mogie"),
    
    url(r'^eventos/resumen/institucion/(\d+)$', 'views.CuartoPasoPostulacion', name="mogie"),
    
    url(r'^eventos/resumen/previsual/(\d+)$', 'views.ResumenPrevisual', name="mogie"),
    
    url(r'^eventos/resumen/finalizar/(\d+)$', 'views.finalizarResumen', name="mogie"),
    
    url(r'^eventos/resumen/coautores/borrar/(\d+)/(\d+)$', 'views.coautoresBorrar', name="mogie"),
    
    url(r'^eventos/resumen/orden/coautores/(\d+)/(\d+)$', 'views.OrdenarCoautores', name="mogie"),
    
    url(r'^eventos/resumen/orden/instituciones/(\d+)/(\d+)$', 'views.OrdenarInstituciones', name="mogie"),
    
    url(r'^eventos/resumen/instituciones/borrar/(\d+)/(\d+)$', 'views.institucionesBorrar', name="mogie"),
    
    url(r'^$', 'views.publico', name='mogie'),
    
    url(r'^ajax/index_v2.html$', 'views.indexvs2', name='mogie'),
)