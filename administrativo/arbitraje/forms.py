from django import forms
from models import *

class CambiarEstatusForm(forms.ModelForm):
      class Meta:
          model = TrabajosArbitros
          fields = ('arbitro','trabajos','estatu',)
		  