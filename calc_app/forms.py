from django import forms
from django.forms import HiddenInput
from django.contrib.auth.models import User
from .models import Ciclo, UserProfileInfo


import logging
logger = logging.getLogger(__name__)

botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,)

# basic validation
def clean_botcatcher(self):
	botcatcher = self.cleaned_data['botcatcher']
	if len(botcatcher) > 0:
		raise forms.ValidationError("GOTCHA BOT")
	return botcatcher


#Formulario Usuario
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username', 'email', 'password')


# Formulario que hereda del modelo propio creado
# class UserProfileInfoForm(forms.ModelForm):
# 	class Meta():
# 		model = UserProfileInfo


#Formulario Ciclo
class CicloForm(forms.Form):
	"""
	Formulario para crear un nuevo ciclo
	cicloName -> nombre del ciclo
	"""
	__cicloName = forms.CharField(label="Nombre del ciclo", max_length=200)

	@property
	def cicloName(self):
		print("Estoy en el getter")
		return self.__cicloName

	@cicloName.setter
	def cicloName(self, nuevoValor):
		print("Estoy en el setter")
		self.__cicloName = nuevoValor


#Formulario Modulo
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
	__moduloName = forms.CharField(label="Nombre del módulo", max_length=200)
	__siglasModulo = forms.CharField(label="Siglas del módulo", max_length=10)
	__numRA = forms.IntegerField(label="Números de RA")
	__numRACE = forms.CharField(widget=HiddenInput(), required=False)
	__idCiclo = forms.TypedChoiceField(choices=[])


	#GETTER Y SETTER de moduloName
	@property
	def moduloName(self):
		print("Estoy en el getter")
		return self.moduloName

	@moduloName.setter
	def moduloName(self, nuevoValor):
		print("Estoy en el setter")
		self.__moduloName = nuevoValor

	# GETTER Y SETTER de siglasModulo
	@property
	def siglasModulo(self):
		print("Estoy en el getter")
		return self.siglasModulo

	@moduloName.setter
	def siglasModulo(self, nuevoValor):
		print("Estoy en el setter")
		self.__siglasModulo = nuevoValor

	# GETTER Y SETTER de numRA
	@property
	def numRA(self):
		print("Estoy en el getter")
		return self.numRA

	@numRA.setter
	def numRA(self, nuevoValor):
		print("Estoy en el setter")
		self.__numRA = nuevoValor

	# GETTER Y SETTER de numRACE
	@property
	def numRACE(self):
		print("Estoy en el getter")
		return self.numRACE

	@numRACE.setter
	def numRACE(self, nuevoValor):
		print("Estoy en el setter")
		self.__numRACE = nuevoValor

	# GETTER Y SETTER de idCiclo
	@property
	def idCiclo(self):
		print("Estoy en el getter")
		return self.idCiclo

	@idCiclo.setter
	def idCiclo(self, nuevoValor):
		print("Estoy en el setter")
		self.__idCiclo = nuevoValor

	# Inicializa la lista desplegable
	def __init__(self, *args, **kwargs):
		super(ModuloForm, self).__init__(*args, **kwargs)
		self.fields['_ModuloForm__idCiclo'].choices = [(choice.id_ciclo, choice.descripcionCiclo,) for choice in Ciclo.objects.all()]


#Formulario Actividad
class ActForm(forms.Form):
	"""

	"""
	__numActividades = forms.IntegerField(widget=forms.TextInput(
		attrs={'class':'form-control'}),
		label="",
		error_messages={
			'invalid':"Debe introducir un número",
			'required': "Este campo es necesario",
		}
	)
	@property
	def numActividades(self):
		print("Estoy en el getter")
		return self.numActividades

	@numActividades.setter
	def numActividades(self, nuevoValor):
		print("Estoy en el setter")
		self.__numActividades = nuevoValor
