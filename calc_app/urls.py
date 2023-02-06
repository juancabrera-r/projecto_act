from django.urls import path
from . import views

# Template tagging
app_name = 'calc_app'

urlpatterns = [
    #Accede a la funcion relative en views
    # path('relative/', views.relative, name='relative'),
    path('modulo/', views.modulo_view, name='modulo'),
    path('ciclo/', views.ciclo_view, name='ciclo'),
    path('ciclo_new/', views.ciclo_new, name='ciclo_new'),
    path('modulo_new/', views.modulo_new, name='modulo_new'),
]
