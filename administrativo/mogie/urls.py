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
    
    url(r'^$', 'views.publico', name='mogie'),
    
    url(r'^ajax/index_v2.html$', 'views.indexvs2', name='mogie'),
)