from django.shortcuts import render
import math

# Create your views here.
def index(request):
    return render(request,'index.html')

#EJERCICIO01
def formCalculadora(request):
    return render(request,'formularios/formulario.html')

def calculadora(request):

    if request.POST['operacion']=='suma':
        context={
            'valor1':request.POST['valor1'],
            'valor2':request.POST['valor2'],
            'resultado':int(request.POST['valor1'])+int(request.POST['valor2']),
            'operacion':request.POST['operacion'],
            
            }
    elif request.POST['operacion']=='resta':
        context={
            'valor1':request.POST['valor1'],
            'valor2':request.POST['valor2'],
            'resultado':int(request.POST['valor1'])-int(request.POST['valor2']),
            'operacion':request.POST['operacion'],

        }
    elif request.POST['operacion']=='producto':
        context={
            'valor1':request.POST['valor1'],
            'valor2':request.POST['valor2'],
            'resultado':int(request.POST['valor1'])*int(request.POST['valor2']),
            'operacion':request.POST['operacion'],

        }  

    return render(request,'resultado.html',context) 

#EJERCICIO02
def formEntrada(request):
    return render(request,'formularios/formEntrada.html')


def entrada(request):

    edad=int(request.POST['edad'])

    if edad<4:
        precio=0
        resultado={
            'edad':edad,
            'precioTotal': precio
            }
    elif edad>=4 and edad<=18 :
        precio=5
        resultado={
            'edad':edad,
            'precioTotal':precio

        }
    elif edad>18:
        precio=10
        resultado={
            'edad':edad,
            'precioTotal':precio
        }  

    return render(request,'resultadoEntrada.html',resultado)  

#EJERCICIO03
def formVolumen(request):
    return render(request,'formularios/formVolumen.html')

def volumen(request):
    diametro=int(request.POST['diametro'])
    altura=int(request.POST['altura'])

    volCilindro=(math.pi*((diametro/2)**2))*altura

    context={
        'volumen':volCilindro
    }

    return render(request,'resultadoVolumen.html',context)