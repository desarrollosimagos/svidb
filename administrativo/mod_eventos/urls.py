# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mod_eventos',
    url(r'^inicio/$', 'views.index', name="registrar"),
)