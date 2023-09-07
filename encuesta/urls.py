from django.urls import path

from . import views

app_name='encuesta'

urlpatterns = [
    #PRINCIPAL
    path('', views.index,name="index"),
    #FORMULARIO EJERCICIO 1
    path('formCalculadora/', views.formCalculadora,name="formCalculadora"),
     #resultado EJERCICIO 1
    path('calculadora/',views.calculadora,name="calculadora"),
     #FORMULARIO EJERCICIO 2
    path('formEntrada/',views.formEntrada,name="formEntrada"),
     #resultado EJERCICIO 2
    path('entrada/',views.entrada,name="entrada"),
     #FORMULARIO EJERCICIO 3
    path('formVolumen/',views.formVolumen,name="formVolumen"),
     #resultado EJERCICIO 3
    path('volumen',views.volumen,name="volumen")

]