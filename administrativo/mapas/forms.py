from django import forms
from models import *

class AvistamientoForm(forms.ModelForm):
      class Meta:
          model = Avistamientos
          fields = ('persona','especie','fechaAvistamiento','desde','address','geolocation','pai','estado','municipio','parroquia','sector','puntor','gps','entorno','numero','tamaniop','medidasc','pathimg1','cuamedida','frecuencia','estatu','observaciones')
		  
class SistematizacionForm(forms.ModelForm):
      class Meta:
          model = Colaboradorespersonas
          fields = ('fecha','tipoColaboracion','taxon','titulo','descripcion','estatu')

