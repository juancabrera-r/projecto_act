from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ModuloForm, CicloForm
from .models import Ciclo, Modulo
from django.shortcuts import get_list_or_404

import logging
logger = logging.getLogger(__name__)


# Create your views here.

#Vista de la página Index
def index(request):
    return render(request, 'index.html')

#Vista de la página donde se muestra el formulario para crear un ciclo
def ciclo_view(request):
    form = CicloForm()
    return render(request, 'ciclo.html', {'form': form})
#
# def relative(request):
#     return render(request, 'relative_url_template.html')

#Vista de la página donde se muestra el formulario para crear un módulo
def modulo_view(request):
    form = ModuloForm()
    return render(request, 'modulo.html', {'form':form})

#Formulario para crear un nuevo módulo
def modulo_new(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModuloForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            moduloName = request.POST['moduloName']
            sigla = request.POST['siglasModulo']
            ra = request.POST['numRA']
            ce = request.POST['numCE']
            curso_id = int(request.POST['curso_id'])

            info = Modulo.objects.create(
                siglasModulo=sigla,
                descripcionModulo=moduloName,
                numRA=ra,
                numCE=ce,
                ciclo_id=curso_id,
                )
            return HttpResponseRedirect(reverse('index'))


    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModuloForm()

    return render(request, 'admin.html', {'form': form})

#Creaciónde un nuevo CICLO
def ciclo_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = CicloForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cicloName = request.POST['cicloName']

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            info = Ciclo.objects.create(
                descripcionCiclo=cicloName)

            return HttpResponseRedirect(reverse('index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CicloForm()

    return render(request, 'ciclo.html', {'form': form})