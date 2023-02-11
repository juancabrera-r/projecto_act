from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ModuloForm, CicloForm, ActForm
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

#Vista de la página donde se muestra el formulario para crear un módulo
def modulo_view(request):
    form = ModuloForm()
    return render(request, 'modulo.html', {'form':form})

def act_view(request):
    form = ActForm()
    ciclos = Ciclo.objects.all()
    modulos = Modulo.objects.all()
    return render(request, 'actividad.html', {'form':form, 'ciclos':ciclos, 'modulos':modulos})

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
            # ce = request.POST['numCE']
            id_Ciclo = int(request.POST['idCiclo'])
            # VER PARA CAMBIAR USANDO CLEANED_DATA
            # temp = form.cleaned_data.get('moduloName')
            # print(temp)
            info = Modulo.objects.create(
                siglasModulo=sigla,
                descripcionModulo=moduloName,
                numRA=ra,
                ciclo_id=id_Ciclo,
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


#Creaciónde un nuevo CICLO
def act_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = ActForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # cicloName = request.POST['cicloName']

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # info = Ciclo.objects.create(
            #     descripcionCiclo=cicloName)

            return HttpResponseRedirect(reverse('index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CicloForm()

    return render(request, 'actividad.html', {'form': form})