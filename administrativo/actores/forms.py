from django import forms
from models import *

class MiembrosInstForm(forms.ModelForm):
      class Meta:
          model = MiembrosdeInstituciones
          fields = ('institucion','miembros','estatu')
		  
class RedactarForm(forms.ModelForm):
      class Meta:
          model = SistemaMensajeria
          fields = ('remi','destino','asunto','mensaje','estatu')

class OrganizacionesForm(forms.ModelForm):
      class Meta:
          model = Actores
          fields = ('tiposAreasAccion','actoresrex','bancoaudio','horarios','fund','url','ambitoaccion','principalesorgfinan','objetivos','publicacionesPeriodicas','aniofundacion','telefono','fax','address','geolocation','rif','siglas','nombre','nombre_completo','direccion','pai','estado','municipio','parroquia','correo','reseniahistorica','pubp','grupobio','logotipo','categoriact','tipocolec','particularidades','estrOrganz','actinteres','coord','estrucorg','tipoorganizacion','userupdate','areasesconserv','directorio','estatu')

class PersonasForm(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('documentoidentidad','nombre','apellido','correo','telefono1','telefono2','movil','fax','pai','estado',
'municipio','parroquia','sector','gruposespecie','areasaccion')

class PersonasRegForm(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('tipodoci','documentoidentidad','nombre','apellido','correo')

class PersonasEditForm(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('id','nombre','apellido','sexo','edocivil','nacimiento','correo','telefono1','telefono2','movil','fax','pai','estado',
'municipio','parroquia','sector','gruposespecie','areasaccion')

class PersonasEditFormNew(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('tipodoci','documentoidentidad','nombre','apellido','sexo','edocivil','nacimiento','correo','telefono1','telefono2','movil','fax','pai','estado',
'municipio','parroquia','sector','gruposespecie','areasaccion')

class PersonasEditForm2(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('id','nombre','apellido','sexo','nacimiento','correo','telefono1','telefono2','movil','fax','pai','estado',
'municipio','parroquia','sector','gruposespecie','areasaccion')

class coautorform(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('tipodoci','documentoidentidad','nombre','apellido','movil')
		  
		  
class InstitucionesForm(forms.ModelForm):
      class Meta:
          model = Actores
          fields = ('tipoorganizacion','nombre_completo','telefono','fax','siglas','correo','pai','estado','direccion',
'rif','ambitoaccion')

class AgregarBibliotecaPublic(forms.ModelForm):
      class Meta:
          model = Bibliotecas
          fields = ('titulo','fecha','autores','directorio','editorial','ibsn','edicion','numerovolumen','resumen','observaciones',
'tipodocs','userupdate','estatu','idioma','numeropaginas','repositoriolinea','licencia')


class AgregarBancoaudiovisualsPublic(forms.ModelForm):
      class Meta:
          model = Bancoaudiovisuals
          fields = ('directorio','fecha','lugar','descripcion','tipo','pathimg','licencia','observaciones','userupdate','estatu',
'seccion')
