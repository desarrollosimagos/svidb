from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to #redirecciona el url a otro
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from django.contrib import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'menu.views.laPlataforma', name='home'),
    
    url(r'^mogie/', include('mogie.urls')),

#    url(r'^', 'pagina.views.error', name='home'),
    url(r'^autocat/undefined', 'menu.views.ajax', name='home'),
    url(r'^autocompletado/actores/undefined', 'menu.views.ajax2', name='home'),
    url(r'^plataforma', 'menu.views.elSistema', name='plataforma'),
    url(r'^colaboradores', 'actores.views.colaboradores', name='colaboradores'),
    url(r'^avances', 'actores.views.Avances', name='Avances'),
    url(r'^construccion', 'menu.views.ConstruccionColectiva', name='construccion'),
    url(r'^estrategia/$', 'menu.views.LaEstrategia', name='estrategias'),
    url(r'^funpza', 'menu.views.FUNZA', name='estrategias'),
    url(r'^licencias', 'documentos.views.licencias', name='licencias'),
	
    url(r'^panel/coord/index/(\d+)$', 'perfil.views.panelCoordinacion', name='Coordinacion'),
    url(r'^panel/coord/assoc/(\d+)/(\d+)$', 'perfil.views.panelCursosIndex', name='Coordinacion'),
    url(r'^panel/coord/assoc/inscribir/(\d+)$', 'perfil.views.panelCursosInscribir', name='Coordinacion'),
	

    url(r'^panel/coord/index/buscar/(\d+)/(\w+)$', 'perfil.views.buscarCedula', name='Coordinacion'),
    url(r'^panel/coord/index/buscar2/(\d+)/(\w+)$', 'perfil.views.buscarCedula', name='Coordinacion'),
    url(r'^panel/coord/index/opcion/(\d+)/(\w+)$', 'perfil.views.panelOpciones', name='Coordinacion'),
    url(r'^panel/coord/index/colaboracion/(\d+)/(\w+)$', 'perfil.views.panelColaboracion', name='Coordinacion'),
	
	
    #url(r'^chat/', include('djangoChat.urls')),
    url(r'^panel/coord/consultas/sql/instituciones$', 'consultassql.views.listaInstitucionesCongresos', name='Consultas'),
	
    url(r'^validarcorreo', 'perfil.views.validarCorreo', name='Perfil'),

#    url(r'^buscador', 'especies.views.buscador', name='buscador'),
    url(r'^buscador$', 'gestion.views.buscadorCompleto', name='buscador'),
    url(r'^buscador2$', 'gestion.views.buscadorCompleto2', name='buscador'),
    url(r'^autocompletado/search/$', 'especies.views.search_view', name='buscador'),


    url(r'^estadisticas/congresos/graph$', 'estadisticas.views.asistenciaCongresos', name='estadisticas'),
    url(r'^panel/estadisticas/eventos/activos$', 'congresos.views.eventos_activos_estadisticas', name='estadisticas'),
    url(r'^panel/estadisticas/eventos/activos/(\d+)/$', 'congresos.views.eventos_activos_estadisticas2', name='incidencias'),
    url(r'^panel/estadisticas/eventos/activos/inscripcion/(\d+)/$', 'estadisticas.views.InscripcionesCongresos', name='incidencias'),
    url(r'^panel/estadisticas/eventos/activos/trabajos/(\d+)/$', 'estadisticas.views.TrabajosEstadisticas', name='incidencias'),
	
    url(r'^panel/eventos/mensajes/(\d+)$', 'congresos.views.mensajesArbitraje', name='incidencias'),
	
    url(r'^panel/documentos/reportes/trabajos/eventos/(\d+)$', 'documentos.views.ReportesCongresosTrabajos', name='documentos'),
    url(r'^panel/coord/certificados/(\d+)$', 'documentos.views.ReportesCongresosCertificados', name='documentos'),
    url(r'^panel/coord/certificados/todos/(\d+)$', 'documentos.views.ReportesCongresosCertificadosTodos', name='documentos'),
    url(r'^panel/coord/certificados/personalizada/(\d+)$', 'documentos.views.ReportesCongresosCertificadosPersonalizada', name='documentos'),
    url(r'^panel/coord/certificados/participacion/(\d+)/(\d+)$', 'documentos.views.ReportesCongresosCertificadosParticipacion', name='documentos'),
	
	url(r'^panel/coord/trabajos/seguimiento/(\d+)/(\w+)/(\d+)$', 'perfil.views.GuardarTrabajosEntregados', name='seguimiento'),
	
	
    url(r'^panel/coord/certificados/trabajos/individual/(\d+)/(\d+)$', 'documentos.views.ReportesCongresosCertificadosSeleccion', name='documentos'),
    url(r'^panel/coord/certificados/trabajos/todos/(\d+)$', 'documentos.views.ReportesCongresosCertificadosSeleccionTodos', name='documentos'),
	
	url(r'^panel/coord/certificados/evento/todos/(\d+)$', 'documentos.views.EventosMasivosPDF', name='documentos'),
	
	
    url(r'^panel/arbitraje/eventos/activos$', 'congresos.views.eventos_activos_arbitraje', name='arbitraje'),
    url(r'^panel/arbitraje/eventos/activos/(\d+)$', 'congresos.views.trabajos_eventos_arbitraje', name='arbitraje'),

    url(r'^panel/coordinador/eventos/activos/(\d+)$', 'congresos.views.trabajos_eventos_coordinador', name='arbitraje'),

    url(r'^panel/trabajos/publicados/congreso/(\d+)$', 'congresos.views.listado_trabajos_publicacion', name='arbitraje'),
    url(r'^panel/trabajos/publicados/congreso2/(\d+)$', 'congresos.views.listado_trabajos_publicacion2', name='arbitraje'),
	
	
	
    url(r'^panel/coordinador/eventos/activos/(\d+)/arbitro/(\d+)/$', 'congresos.views.trabajos_eventos_coordinador_filtro_arbitro', name='arbitraje'),
	
    url(r'^panel/coordinador/eventos/activos/filtro/(\d+)/(\d+)$', 'congresos.views.trabajos_eventos_coordinador_filtro', name='arbitraje'),
    url(r'^panel/coordinador/eventos/activos/filtro/(\d+)/estatus/(\d+)/arbitro/(\d+)/$', 'congresos.views.trabajos_eventos_coordinador_filtro_arbitro2', name='arbitraje'),

    url(r'^panel/arbitraje/eventos/activos/filtro/(\d+)/(\d+)$', 'congresos.views.trabajos_eventos_arbitraje_filtro', name='arbitraje'),
    url(r'^panel/arbitraje/trabajos/estatus/(\d+)$', 'arbitraje.views.CambiarEstatus', name='arbitraje'),
    url(r'^panel/arbitraje/trabajos/estatus/publicacion/(\d+)$', 'congresos.views.CambiarEstatusPublicacion', name='arbitraje'),
    url(r'^panel/arbitraje/trabajos/modificaciones/(\d+)$', 'arbitraje.views.Historial', name='arbitraje'),
	
    url(r'^panel/eventos/trabajos/previsual/(\d+)$', 'congresos.views.previsualizarTrabajos', name='arbitraje'),
	

    url(r'^estadisticas/especies/graph1$', 'estadisticas.views.estadisticataxon1', name='estadisticas'),
    url(r'^estadisticas/especies/graph2$', 'estadisticas.views.estadisticataxon2', name='estadisticas'),
    url(r'^estadisticas/especies/graph5$', 'estadisticas.views.detalleTipoTaxon', name='estadisticas'),

    url(r'^estadisticas/especies/exoticas/01$', 'estadisticas.views.exoticasreport', name='estadisticas'),
    url(r'^estadisticas/especies/exoticas/02$', 'estadisticas.views.ExoticasReportesPorEstados', name='estadisticas'),
		
    url(r'^estadisticas/actores/graph4$', 'estadisticas.views.actoresporCategoria', name='estadisticas'),
    url(r'^estadisticas/actores/01$', 'estadisticas.views.actoresTotalCargados', name='estadisticas'),
	
    url(r'^estadisticas/areas/01$', 'estadisticas.views.areasTotalCargados', name='estadisticas'),

#    url(r'^report_builder/', include('report_builder.urls')),
    url(r'^reportes/', include('django_qbe.urls')),

    url(r'^panel/especies/colaboraciones/(\d+)/(\d+)/$', 'mapas.views.listaColaboraciones', name='estadisticas'),
    url(r'^panel/areas/colaboraciones/(\d+)/(\d+)/$', 'mapas.views.listaColaboracionesAreas', name='estadisticas'),
    url(r'^panel/actores/colaboraciones/(\d+)/(\d+)/$', 'mapas.views.listaColaboracionesActores', name='estadisticas'),
	
    url(r'^panel/incidencias/taxon/(\d+)/$', 'mapas.views.incidencias', name='incidencias'),
	
	
    url(r'^panel/especies/colaboraciones/change/publicar/(\d+)/(\d+)/$', 'mapas.views.validarEstatusEspecie', name='estadisticas'),
    url(r'^panel/especies/colaboraciones/change/contribuir/(\d+)/(\d+)/$', 'mapas.views.validarColaboracion', name='estadisticas'),

    url(r'^panel/actores/colaboraciones/change/publicar/(\d+)/(\d+)/$', 'mapas.views.validarEstatusActores', name='estadisticas'),
    url(r'^panel/actores/colaboraciones/change/contribuir/(\d+)/(\d+)/$', 'mapas.views.validarColaboracion', name='estadisticas'),

    url(r'^panel/areas/colaboraciones/change/publicar/(\d+)/(\d+)/$', 'mapas.views.validarEstatusAreas', name='estadisticas'),
    url(r'^panel/areas/colaboraciones/change/contribuir/(\d+)/(\d+)/$', 'mapas.views.validarColaboracion', name='estadisticas'),
#    url(r'^panel/especies/colaboraciones/change/estatus/(\d+)/(\d+)/$', 'mapas.views.validarColaboracion', name='estadisticas'),

	
    url(r'^actores$', 'menu.views.secActores', name='Actores'),

	
    url(r'^actores/(\d+)/$', 'menu.views.detActores', name='fundamentos'),
    url(r'^list_actores/(\d+)/$', 'menu.views.listaActores', name='fundamentos'),

    url(r'^actores/ficha/(\d+)/$', 'actores.views.ficha', name='fundamentos'),
    url(r'^areas/ficha/(\d+)/$', 'areas.views.ficha', name='fundamentos'),
	
    url(r'^especies/ficha/(\d+)/(\d+)/$', 'especies.views.ficha', name='fundamentos'),
    url(r'^especies/ficha/ext/(\d+)/$', 'especies.views.extficha', name='fundamentos'),
    url(r'^especies/ficha/cont/(\d+)/$', 'especies.views.contficha', name='fundamentos'),
	
	
    url(r'^google/maps/(-?\d+\.\d+\,\-?\d+\.\d+)$', 'actores.views.ver_mapas', name='glosario'),

    url(r'^glosario/(\w+)/(\d+)/$', 'gestion.views.glosario', name='glosario'),
    url(r'^buscar/(\w+)/(\d+)/$', 'gestion.views.buscar', name='glosario'),
	
    url(r'^biblioteca/(\d+)/$', 'actores.biblioteca.Biblioteca', name='biblioteca'),
    url(r'^buscar_biblioteca/(\d+)/(\w+)/$', 'actores.biblioteca.buscar', name='biblioteca'),
    url(r'^buscar_2/(\d+)/$', 'actores.biblioteca.buscar2', name='biblioteca'),
    url(r'^panel/biblioteca$', 'actores.biblioteca.index', name='biblioteca'),
    url(r'^panel/biblioteca/lista$', 'actores.biblioteca.lista', name='biblioteca'),
    url(r'^panel/biblioteca/add$', 'actores.biblioteca.agregar', name='biblioteca'),
	
    url(r'^panel/bancoaudio$', 'actores.bancoaudio.index', name='biblioteca'),
    url(r'^panel/bancoaudio/lista$', 'actores.bancoaudio.lista', name='biblioteca'),
    url(r'^panel/bancoaudio/add$', 'actores.bancoaudio.agregar', name='biblioteca'),
    url(r'^panel/bancoaudio/galeria/(\w+)/(\d+)/$', 'actores.bancoaudio.galeria', name='bancoaudio'),
    url(r'^panel/bancoaudio/galeriaPag/(\w+)/(\d+)/(\d+)/$', 'actores.bancoaudio.PaginadorGaleria', name='bancoaudio'),
    url(r'^panel/bancoaudio/visual/(\d+)/(\d+)/$', 'actores.bancoaudio.PaginadorGaleria2', name='bancoaudio'),
    url(r'^panel/bancoaudio/ver/(\d+)/$', 'actores.bancoaudio.bancoVer', name='bancoaudio'),

    url(r'^panel/mapas/visual/(\d+)/(\d+)/$', 'menu.views.PaginadorGaleria2', name='bancoaudio'),
    url(r'^panel/mapas/ver/(\d+)/$', 'menu.views.bancoVer', name='bancoaudio'),
	
	
    url(r'^panel/avistamientos$', 'mapas.avistamientos.index', name='biblioteca'),
    url(r'^panel/avistamientos/lista$', 'mapas.avistamientos.lista', name='biblioteca'),
    url(r'^panel/avistamientos/add/(\d+)/$', 'mapas.avistamientos.agregar', name='biblioteca'),
    url(r'^panel/avistamientos/mostrar/(\d+)/$', 'mapas.avistamientos.mostrar', name='glosario'),
	
    url(r'^panel/eventos/trabajos/actores/(\d+)/$', 'actores.views.actor_paso1', name='actores'),
    url(r'^panel/eventos/trabajos/actores/paso/2/(\d+)$', 'actores.views.paso2_colectivos', name='actores'),
    url(r'^panel/eventos/trabajos/actores/paso/3/(\d+)/(\d+)/$', 'actores.views.paso3_colectivos', name='actores'),
    url(r'^panel/eventos/trabajos/actores/paso/4/(\d+)/(\d+)/$', 'actores.views.paso4_colectivos', name='actores'),
    url(r'^panel/eventos/trabajos/actores/paso/5/(\d+)/(\d+)/$', 'actores.views.paso5_colectivos', name='actores'),
    url(r'^panel/eventos/trabajos/actores/paso/6/(\d+)/(\d+)/$', 'actores.views.paso6_colectivos', name='actores'),
    url(r'^panel/eventos/trabajos/actores/paso/7/(\d+)/$', 'actores.views.paso7_colectivos', name='actores'),
    url(r'^panel/actores/ajax/paso2$', 'actores.views.ajax_2', name='actores'),
	
    url(r'^panel/cuenta/modulo/(\d+)/$', 'actores.views.PermisosSubModulosPublicos', name='actores'),
    url(r'^panel/verificacion/$', 'perfil.views.verificacion', name='perfil'),
    url(r'^panel/activacion/$', 'perfil.views.activacion', name='perfil'),
    url(r'^panel/pass/cambiar$', 'perfil.views.recuperacion', name='perfil'),
    url(r'^panel/pass/restart$', 'perfil.views.cambiar', name='perfil'),
    url(r'^panel/verificacion/reenviar$', 'perfil.views.renValidacion', name='perfil'),
	
	

    url(r'^ajaxexample$', 'actores.views.main'),
    url(r'^ajaxexample_json$', 'actores.views.ajax'),
	
    url(r'^areas$', 'menu.views.secAreas', name='Areas'),
    url(r'^areas/(\d+)/$', 'menu.views.detAreas', name='fundamentos'),
    url(r'^list_areas/(\d+)/$', 'menu.views.listaAreas', name='fundamentos'),
    url(r'^areas/complemento/(\d+)/(\d+)/$', 'menu.views.listaComplementoAreas', name='fundamentos'),
    url(r'^actores/complemento/(\d+)/(\d+)/$', 'menu.views.listaComplementoActores', name='fundamentos'),
	
    url(r'^especies$', 'menu.views.secTaxon', name='Actores'),

    url(r'^exoticas/(\d+)/$', 'menu.views.listaexoticas', name='fundamentos'),
    url(r'^exoticas/complemento/(\d+)/(\d+)/(\d+)/$', 'menu.views.listaexoticaComplemento', name='fundamentos'),
	
    url(r'^comercio/(\d+)/$', 'menu.views.listatraficos', name='fundamentos'),
    url(r'^comercio/complemento/(\d+)/(\d+)/(\d+)/$', 'menu.views.listatraficosComplemento', name='fundamentos'),
	
    url(r'^extincion/(\d+)/$', 'menu.views.listapeligroext', name='fundamentos'),
    url(r'^extincion/complemento/(\d+)/(\d+)/(\d+)/$', 'menu.views.listapeligroextComplemento', name='fundamentos'),
	
    url(r'^agropecuaria/(\d+)/$', 'menu.views.listaagricolas', name='fundamentos'),
    url(r'^agropecuaria/complemento/(\d+)/(\d+)/(\d+)/$', 'menu.views.listaagricolasComplemento', name='fundamentos'),
	
    url(r'^salud/(\d+)/$', 'menu.views.listasalud', name='fundamentos'),
    url(r'^salud/complemento/(\d+)/(\d+)/(\d+)/$', 'menu.views.listasaludComplemento', name='fundamentos'),
	
    url(r'^sustentables/(\d+)/$', 'menu.views.listasustentable', name='fundamentos'),
    url(r'^sustentables/complemento/(\d+)/(\d+)/(\d+)/$', 'menu.views.listasustentableComplemento', name='fundamentos'),
	
    url(r'^fichaEspecies/(\d+)/$', 'especies.views.ficha', name='fundamentos'),

    url(r'^omg', 'menu.views.OMG', name='estrategias'),
    url(r'^recob', 'menu.views.RECOB', name='estrategias'),
    url(r'^msiidb', 'menu.views.MSIIDB', name='estrategias'),

    url(r'^organizaciones', 'actores.views.organizaciones', name='organizaciones'),
    url(r'^personas', 'actores.views.personas', name='personas'),
    url(r'^perfil', 'actores.views.perfil', name='perfil'),
    url(r'^nuevo_usuario', 'actores.views.nuevo_usuario', name='nuevo_usuario'),
    url(r'^panel/datos', 'actores.views.mis_datos', name='mis_datos'),
    url(r'^salir', 'actores.views.logout', name='cerrar_sesion'),
	
    url(r'^eventos/activos', 'congresos.views.eventos_list', name='eventos'),
    url(r'^eventos/listas', 'congresos.views.eventoslista', name='eventos'),
    url(r'^eventos/ver/(\d+)/$', 'congresos.views.ver_eventos', name='ver_congresos'),
    url(r'^panel/eventos/ver/(\d+)/$', 'congresos.views.ver_congresos', name='ver_congresos'),

    url(r'^panel/publicaciones', 'congresos.views.ver_todos_trabajos', name='ver_congresos'),
    url(r'^registro_trabajos.php/(\d+)/$', 'congresos.views.form_trabajos', name='form_trabajos'),
    url(r'^panel/eventos/registro/paso/1/(\d+)/$', 'congresos.views.seleccionfundamentos', name='fundamentos'),
    url(r'^panel/eventos/registro/paso/2/(\d+)/(\d+)/$', 'congresos.views.objetivosespecificos', name='registro'),
    url(r'^panel/eventos/registro/paso/3/(\d+)/(\d+)/$', 'congresos.views.accionesgenerales', name='registro'),
    url(r'^panel/eventos/registro/paso/4/(\d+)/(\d+)/$', 'congresos.views.accionesespecificas', name='registro'),
#    url(r'^panel/eventos/registro/paso/5/(\d+)/(\d+)/$', 'congresos.views.form_trabajos', name='registro'),
    url(r'^panel/eventos/registro/(\d+)/$', 'congresos.views.form_trabajos', name='registro'),
    url(r'^panel/eventos/trabajos/editar/(\d+)/$', 'congresos.views.form_editar', name='fundamentos'),
    url(r'^panel/eventos/trabajos/coautor/agregar/(\d+)/$', 'actores.views.coautor', name='coautor'),
    url(r'^insti.php/(\d+)/$', 'actores.views.instituciones', name='instituciones'),
	
    url(r'^inscribir_evento/(\d+)/$', 'congresos.views.patrticipacion', name='patrticipacion'),
    url(r'^avistamiento/registrar/punto/(\d+)/(\d+)/$', 'especies.views.patrticipacion', name='patrticipacion'),
	
    url(r'^listas$', 'especies.views.listas', name='listas'),
    url(r'^vertax/(\d+)/$', 'especies.views.vertaxon', name='vertax'),
    url(r'^list/(\d+)/$', 'especies.views.list', name='list'),
    url(r'^reino/(\d+)/$', 'especies.views.reino', name='reino'),
    url(r'^phylum/(\d+)/$', 'especies.views.phylum', name='phylum'),
    url(r'^clase/(\d+)/$', 'especies.views.clase', name='clase'),
    url(r'^orden/(\d+)/$', 'especies.views.orden', name='orden'),
    url(r'^familia/(\d+)/$', 'especies.views.familia', name='familia'),
    url(r'^genero/(\d+)/$', 'especies.views.genero', name='genero'),
    url(r'^PreCargaEstatus.php', 'especies.cargar.InstallStatus', name='PreCarga'),
    url(r'^escalerataxon.php', 'especies.cargar.listasEscalera', name='Escalera'),
	
    url(r'^mensajes.php', 'actores.views.mensajes', name='Mensajes'),
    url(r'^vermsn.php/(\d+)/$', 'actores.views.vermensajes', name='genero'),
    url(r'^redactar.php', 'actores.views.redactar', name='Mensajes'),
    url(r'^solicitudes.php', 'actores.views.solicitudes', name='Mensajes'),
	
    #documentos
    url(r'^panel/documentos/eventos/planillas/preinscripcion/(\d+)/$', 'documentos.views.libro_pdf', name='preinscripcion'),
    url(r'^panel/documentos/eventos/planillas/resumen/(\d+)/$', 'documentos.views.resumen_pdf', name='preinscripcion'),
    url(r'^panel/documentos/trabajos/resumen/(\d+)/$', 'documentos.views.previsualizarTrabajosPdf', name='preinscripcion'),


    # url(r'^administrativo/', include('administrativo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^manager/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/js'}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'media'}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static'}),
	

#    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()
