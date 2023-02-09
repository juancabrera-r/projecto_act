from django.core import validators
from django import forms
from .models import Ciclo, Modulo

import logging
logger = logging.getLogger(__name__)

botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,)

# basic validation
def clean_botcatcher(self):
	botcatcher = self.cleaned_data['botcatcher']
	if len(botcatcher) > 0:
		raise forms.ValidationError("GOTCHA BOT")
	return botcatcher

#
class ModuloForm(forms.Form):
	"""
	Formulario para crear un nuevo módulo
		moduloName -> nombre del módulo
		siglasModulo -> abreviatura/siglas del módulo
		id_modulo -> identificación del módulo, se genera automático, único
		numRA -> nº de Resultados de Aprendizaje
		numCE -> nº de Criterios de Evaluación
	"""
	#Accede a la base de datos, obtiene todos los vamores y crea una lista de tuplas (id,curso)

	moduloName = forms.CharField(label="Nombre del módulo", max_length=200)
	siglasModulo = forms.CharField(label="Siglas del módulo", max_length=10)
	numRA = forms.IntegerField(label="Números de RA")
	numCE = forms.IntegerField(label="Números de CE")
	choice = forms.TypedChoiceField(choices=[])

	#Inicializa la lista desplegable
	def __init__(self, *args, **kwargs):
		super(ModuloForm, self).__init__(*args, **kwargs)
		self.fields['domain'].choices = [(choice.id_ciclo, choice.descripcionCiclo,) for choice in Ciclo.objects.all()]

class CicloForm(forms.Form):
	"""
	Formulario para crear un nuevo ciclo
	cicloName -> nombre del ciclo
	"""
	cicloName = forms.CharField(label="Nombre del ciclo", max_length=200)



class ActForm(forms.Form):
	"""

	"""





