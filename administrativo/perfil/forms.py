from django import forms
from models import *

class SolicitudesNewForm(forms.ModelForm):
      class Meta:
          model = SistemaSolicitudes
          fields = ('remi','tipoSolicitud','destino','asunto','mensaje','personasinvol','prioridad','estatu')
		  