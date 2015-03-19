# -*- coding: UTF-8 -*-
from django import forms
from models import *
import re
from captcha.fields import ReCaptchaField
from django.utils.translation import ugettext, ugettext_lazy as _

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

class FormularioActualizarDatos1(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('nombre','apellido','nacimiento','sexo','pai','estado','municipio','parroquia')

class UserCreationFormSVIDB(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    username = forms.RegexField(label=_("Username"), max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text = _("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages = {
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password1_confirmation = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password1 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text = _("Enter the same password as above, for verification."))
		
    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password1(self):
        password1_confirmation = self.cleaned_data.get("password1_confirmation", "")
        password1 = self.cleaned_data["password1"]
        if password1_confirmation != password1:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password1
		
    def save(self, commit=True):
        user = super(UserCreationFormSVIDB, self).save(commit=False)
        user.set_password(self.cleaned_data["password1_confirmation"])
        if commit:
            user.save()
        return user

class PersonasRegForm(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('tipodoci','documentoidentidad','nombre','apellido')
          

class FormularioPersonaEventos(forms.ModelForm):
      class Meta:
          model = Directorios
          fields = ('tipodoci','documentoidentidad','nombre','apellido','sexo','nacimiento','pai','estado',
'municipio','parroquia')

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
