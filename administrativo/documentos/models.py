#!/usr/bin/python -u
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from datetime import datetime
from gestion.models import *

# Create your models here.
class Licencias(models.Model):
    tipo = models.CharField(max_length=150, blank=True,verbose_name='nombre')
    descripcion = models.TextField(blank=True)
    url = models.URLField(blank=True,null=True)
    pathimg1 = models.ImageField(upload_to='pathImg',db_column='pathImg1',blank=True,null=True) 
    pathimg2 = models.ImageField(upload_to='pathImg',db_column='pathImg2',blank=True,null=True) 
    pathimg3 = models.ImageField(upload_to='pathImg',db_column='pathImg3',blank=True,null=True) 
    siglas = models.CharField(max_length=45, blank=True)
    update = models.DateTimeField(default=datetime.now(),editable = False)
    userupdate = models.ForeignKey(User,verbose_name='Usuario')
    class Meta:
        db_table = u'licencias'
        verbose_name_plural='Licencias'
        verbose_name='Licencias'
        #app_label = 'Datos_Transversales'
    def __unicode__(self):
        return u"%s  %s" %(self.tipo, self.siglas)


