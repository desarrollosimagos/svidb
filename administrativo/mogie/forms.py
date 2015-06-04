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
          fields = ('titulo','resumen','tematicas','modalidad','directorio','evento')
          
class DatosResumen1(forms.ModelForm):
      class Meta:
          model = Trabajoscongresos
          fields = ('titulo','resumen','tematicas','modalidad')

class DatosResumenCoautores(forms.ModelForm):
      class Meta:
          model = RelacionPersonasTrabajos
          fields = ('trabajo','institucionestxt')   
          
class DatosResumenInstituciones(forms.ModelForm):
      class Meta:
          model = ActoresHistorico
          fields = ('rif','nombre','nombre_completo','telefono')         
          
class GuardarDatosDirectorios(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('nombre','apellido','telefono1','movil','nacimiento','sexo','edocivil','pai','estado','municipio','parroquia','sector','ocupacion')
          
class GuardarDatosPersonas(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('nombre','apellido','tipodoci','documentoidentidad')
