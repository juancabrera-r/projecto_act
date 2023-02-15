import json
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ModuloForm, CicloForm, ActForm, UserForm
from .models import Ciclo, Modulo

#Para mostrar por consola
import logging
logger = logging.getLogger(__name__)


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

#Vista de la página donse se inicia la actividad
def act_view(request):
    form = ActForm()
    #Se filtra todos los ciclos y módulos
    ciclos = Ciclo.objects.all()
    modulos = Modulo.objects.all()
    return render(request, 'actividad.html', {'form':form, 'ciclos':ciclos, 'modulos':modulos,})

#Vista de la página donse se crea la actividad
def result_view(request):
    # Se filtra todos los ciclos y módulos
    return render(request, 'result_table.html')

#Vista de la página register
def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileInfoForm(data=request.POST)

        #Se compara si son validos ambos formularios
        if user_form.is_valid() :
            #Almacena la información del formulario user
            user = user_form.save()
            #Hashing the password
            user.set_password(user.password)
            user.save()

            #Almacena la información del formulario profile
            #Commit=False evita que se produzca colisión, evita que se guarde la información y que se
            #produzca una sobreescritura
            # profile = profile_form.save(commit=False)
            # profile.user = user

            #Si se carga una foto,
            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']
            # profile.save()

            #Confirmamos el registro
            registered = True

        #En caso de que no sean válidos los formularios...
        else:
            print(user_form.errors)

    #En caso de que no se produzca un POST
    else:
        user_form = UserForm()
        # profile_form = UserProfileInfoForm()

    return render(request, 'registration.html', {
        'user_form': user_form,
        # 'profile_form': profile_form,
        'registered': registered})


#Creaciónde un nuevo CICLO
def ciclo_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CicloForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cicloName = request.POST['_CicloForm__cicloName']
            info = Ciclo.objects.create(
                descripcionCiclo=cicloName)
            return HttpResponseRedirect(reverse('index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CicloForm()

    return render(request, 'ciclo.html', {'form': form})


#Formulario para crear un nuevo módulo
def modulo_new(request):
    if request.method == 'POST':
        form = ModuloForm(request.POST)
        if form.is_valid():
            #Obtienes los RACE seleccionados
            datas = request.POST['id_RACE']
            #Obtiene el nombre del módulo
            moduloName = request.POST['_ModuloForm__moduloName']
            #Obtiene las siglas del módulo
            sigla = request.POST['_ModuloForm__siglasModulo']
            #Obtiene el nº de RA
            ra = request.POST['_ModuloForm__numRA']
            #Obtiene el id del ciclo y lo transforma en int
            id_Ciclo = int(request.POST['_ModuloForm__idCiclo'])

            #Se genera un array de tipo [RA,CE]
            #IMPORTANTE, NO FUNCIONA CON RA >9
            datas_array=[]
            for data in datas.split(','):
                a,b = int(data[0]),int(data[1:])
                data = [a,b]
                datas_array.append(data)

            info = Modulo.objects.create(
                siglasModulo=sigla,
                descripcionModulo=moduloName,
                numRA=ra,
                ciclo_id=id_Ciclo,
                arrayRACE=datas_array,
                )
            return HttpResponseRedirect(reverse('index'))

    else:
        form = ModuloForm()

    return render(request, 'index.html', {'form': form})


#Creaciónde un nuevo CICLO
def act_new(request):
    if request.method == 'POST':

        form = ActForm(request.POST)
        if form.is_valid():
            # ciclo_select = request.POST['ciclos']
            #Módulo seleccionado
            modulo_select = request.POST['modulos']
            #Número de actividades que se van a crear
            act_select = int(request.POST['_ActForm__numActividades'])

            #Filtra el modulo y se obtiene:
            #Número de RA del módulo seleccionado
            #Matríz de RACE
            modulo_data = Modulo.objects.all().filter(id_modulo=modulo_select).values()
            modulo_data_numRA = Modulo.objects.all().filter(id_modulo=modulo_select).values('numRA')[0]['numRA']
            modulo_data_RACE = Modulo.objects.all().filter(id_modulo=modulo_select).values('arrayRACE')[0]['arrayRACE']

            #Convierte en list un string
            modulo_data_RACE= json.loads(modulo_data_RACE)

            #Genera una lista de ra y ce
            race=[0]
            ce = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']

            #Bucle para cada RA (del 1 al 9), guarda para cada RA los criterios que le corresponden
            for n in range(10):
                temp = []
                for ra in modulo_data_RACE:
                    if ra[0]==n:
                        temp.append(ce[(ra[1]-1)])
                race.append(temp)
                race[n]=temp

            race_len =[]
            for n in range(1,len(race)):
                race_len.append(len(race[n]))

            long_race = race_len.index(max(race_len))+1

            return render(request, 'result_table.html', {
                'modulo_data':modulo_data,
                'act_select':range(1,act_select+1),
                'numRA':range(1,modulo_data_numRA+1),
                'major': race[long_race],
                'race1': race[1],
                'race2': race[2],
                'race3': race[3],
                'race4': race[4],
                'race5': race[5],
                'race6': race[6],
                'race7': race[7],
                'race8': race[8],
                'race9': race[9],
            })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CicloForm()

    return render(request, 'actividad.html', {'form': form})