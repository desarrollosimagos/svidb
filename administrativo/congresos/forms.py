from django import forms
from congresos.models import Eventos,Trabajoscongresos

class TrabajosFormGuardar(forms.ModelForm):
      class Meta:
          model = Trabajoscongresos
          fields = ('titulo','modalidad','tematicas','resumen','evento','directorio')
#          fields = ('titulo','accespecifi','modalidad','tematicas','resumen','evento','directorio')

class TrabajosFormGuardarArbitro(forms.ModelForm):
      class Meta:
          model = Trabajoscongresos
          fields = ('titulo','fundamento','objetivoespecifico','accionesgenerale','accespecifi','modalidad','tematicas','resumen','evento','directorio')

class TrabajosForm(forms.ModelForm):
      class Meta:
          model = Trabajoscongresos
          fields = ('titulo','accespecifi','modalidad','resumen')
		  
class EstatusPublicacion(forms.ModelForm):
      class Meta:
          model = Trabajoscongresos
          fields = ('estatu',)
		  
class TrabajosEditar(forms.ModelForm):
      class Meta:
          model = Trabajoscongresos
          fields = ('modalidad','resumen')