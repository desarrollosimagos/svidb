#!/usr/bin/python -u
# -*- coding: utf-8 -*-
import os
from inicio.models import *
#from areas.models import *
#from actores.models import *
from django import forms
from django.contrib import admin
from mapas.models import Colaboradorespersonas

from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

from posiciones.autocomplete.widgets import *

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)

            splitted_filename = list(os.path.splitext(file_name))
            splitted_filename.insert(1, '.59_59')
            file_nombre_59_59 = ''.join(splitted_filename)
            
            splitted_filename = list(os.path.splitext(file_name))
            splitted_filename.insert(1, '.118_118')
            file_nombre_118_118 = ''.join(splitted_filename)

            splitted_filename = list(os.path.splitext(file_name))
            splitted_filename.insert(1, '.157_118')
            file_nombre_157_118 = ''.join(splitted_filename)

            output.append(u'<table><tr><td>Normal - redimencion: 300 x 400</td><td>157 x 118</td><td>118 x 118</td><td>59 x 59</td><tr><tr><td><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td width="15" background="/media/imgs/esqsi.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latsup.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqsd.png" style="background-repeat:no-repeat;"></td></tr><tr><td width="15" background="/media/imgs/latizq.png" style="background-repeat:repeat-y;"></td><td><a href="%s" target="_blank"><img src="%s" alt="%s" width="300px" height="400px" /></a></td><td width="32" background="/media/imgs/latder.png" style="background-repeat:repeat-y;"></td></tr><tr><td width="15" background="/media/imgs/esqid.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latinf.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqii.png" style="background-repeat:no-repeat;"></td></tr></table>  </td><td><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td width="15" background="/media/imgs/esqsi.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latsup.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqsd.png" style="background-repeat:no-repeat;"></td></tr><tr><td width="15" background="/media/imgs/latizq.png" style="background-repeat:repeat-y;"></td><td><a href="/media/%s" target="_blank"><img src="/media/%s" alt="%s" /></a></td><td width="32" background="/media/imgs/latder.png" style="background-repeat:repeat-y;"></td></tr><tr><td width="15" background="/media/imgs/esqid.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latinf.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqii.png" style="background-repeat:no-repeat;"></td></tr></table></td><td><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td width="15" background="/media/imgs/esqsi.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latsup.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqsd.png" style="background-repeat:no-repeat;"></td></tr><tr><td width="15" background="/media/imgs/latizq.png" style="background-repeat:repeat-y;"></td><td><a href="/media/%s" target="_blank"><img src="/media/%s" alt="%s" /></a></td><td width="32" background="/media/imgs/latder.png" style="background-repeat:repeat-y;"></td></tr><tr><td width="15" background="/media/imgs/esqid.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latinf.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqii.png" style="background-repeat:no-repeat;"></td></tr></table></td><td><table align="left" border="0" cellpadding="0" cellspacing="0"><tr><td width="15" background="/media/imgs/esqsi.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latsup.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqsd.png" style="background-repeat:no-repeat;"></td></tr><tr><td width="15" background="/media/imgs/latizq.png" style="background-repeat:repeat-y;"></td><td><a href="/media/%s" target="_blank"><img src="/media/%s" alt="%s" /></a></td><td width="32" background="/media/imgs/latder.png" style="background-repeat:repeat-y;"></td></tr><tr><td width="15" background="/media/imgs/esqid.png" style="background-repeat:no-repeat;"></td><td background="/media/imgs/latinf.png" style="background-repeat:repeat-x;"><div>&nbsp;</div></td><td width="32" background="/media/imgs/esqii.png" style="background-repeat:no-repeat;"></td></tr></table></td></tr></table>' % \
                (image_url, image_url, file_name, file_nombre_157_118, file_nombre_157_118, file_nombre_157_118,file_nombre_118_118, file_nombre_118_118, file_nombre_118_118,file_nombre_59_59, file_nombre_59_59, file_nombre_59_59))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))

#=================================================================================================
class ColaboradorespersonasAdmin(AutocompleteTabularInline):
      model = Colaboradorespersonas
      extra = 1
      related_search_fields = { 
	           'cultural' : ('id','titulo',),
	           'colectivos' : ('id','nombre_completo',),
	           'areas' : ('id','nombre',),
	           'etnias' : ('id','nombre',),
	           'mapas' : ('id','nombre',),
	           'taxon' : ('id','nombre',),
	           'persona' : ('id','documentoidentidad','nombre','apellido',),
      }
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ColaboradorespersonasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
		  
#=================================================================================================
class TipocolaboradorsAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TipocolaboradorsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 


admin.site.register(Tipocolaboradors,TipocolaboradorsAdmin)


#=====================================================================================================
class TipocolaboracionAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(TipocolaboracionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 


admin.site.register(Tipocolaboracion,TipocolaboradorsAdmin)

#=================================================================================================
class ColaboradoresinstitutesAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(ColaboradoresinstitutesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 


admin.site.register(Colaboradoresinstitutes,ColaboradoresinstitutesAdmin)



#=================================================================================================
class EquiposAdmin(AutocompleteModelAdmin):
      related_search_fields = { 
                'directorio': ('id','documentoidentidad','nombre','apellido'),
      }
      list_display = ('directorio','funciones',)
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(EquiposAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 


admin.site.register(Equipos,EquiposAdmin)



#=================================================================================================
class DirectoriotipoareaaccionsAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(DirectoriotipoareaaccionsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 


admin.site.register(Directoriotipoareaaccions,DirectoriotipoareaaccionsAdmin)

#=================================================================================================
class PersonalasociadosAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(PersonalasociadosAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Personalasociados,PersonalasociadosAdmin)

#=================================================================================================
class RedessocialesAdmin(admin.ModelAdmin):
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(RedessocialesAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 


admin.site.register(Redessociales,RedessocialesAdmin)


#=================================================================================================
class VinculacionactoresAdmin(admin.ModelAdmin):
      list_display = ('actore','fundamento')
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(VinculacionactoresAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs) 
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js') 

admin.site.register(Vinculacionactores,VinculacionactoresAdmin)


#-===========================================================================
class NoticiasAdmin(admin.ModelAdmin):      
      def formfield_for_foreignkey(self, db_field, request, **kwargs):
          if db_field.name == "userupdate":
             kwargs["queryset"] = User.objects.filter(id=request.user.id)
          return super(NoticiasAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
      class Media:
		js = ('/js/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Noticias,NoticiasAdmin) 

