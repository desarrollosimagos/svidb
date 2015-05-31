from django import forms
from models import *
from actores.models import *

class GuardarFoto(forms.ModelForm):
      class Meta:
          model = ExtensionPerfilUsuario
          fields = ('foto',)
          
class DatosResumen(forms.ModelForm):
      class Meta:
          model = Trabajoscongresos
          fields = ('titulo','resumen','tematicas','modalidad','directorio')
          
class GuardarDatosDirectorios(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('nombre','apellido','telefono1','movil','nacimiento','sexo','edocivil','pai','estado','municipio','parroquia','sector','ocupacion')
          
class GuardarDatosPersonas(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('nombre','apellido','tipodoci','documentoidentidad')
