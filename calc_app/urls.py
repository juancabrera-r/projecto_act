from django.urls import path
from . import views

# Template tagging
app_name = 'calc_app'

urlpatterns = [
    #Accede a la funcion relative en views
    path('modulo/', views.modulo_view, name='modulo'),
    path('ciclo/', views.ciclo_view, name='ciclo'),
    path('actividad/', views.act_view, name='actividad'),
    path('ciclo_new/', views.ciclo_new, name='ciclo_new'),
    path('modulo_new/', views.modulo_new, name='modulo_new'),
    path("act_new/", views.act_new, name='act_new'),
    path("result_view/", views.result_view, name='result'),
    path('register/', views.register, name='register'),

]
