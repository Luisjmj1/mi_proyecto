from fileinput import close
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random
from home.models import Persona


def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La hora y fecha actual es {fecha_y_hora}')

def hola(request):
    return HttpResponse('Holaaaaaaaaaaaaaaaaaaa')


def crear_familia(request):
    
    persona1 = Persona(nombre=Luis, apellido=Moreno, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    persona2 = Persona(nombre=Freddy, apellido=Druguer, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    persona3 = Persona(nombre=Rosame, apellido=Eltrozo, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    persona4 = Persona(nombre=Caia, apellido=Parada, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    persona1.save()
    persona2.save()
    persona3.save()
    persona4.save()
    
    template = loader.get_template('crear_familia.html')
    template_renderizado = template.render({})
    
    return HttpResponse(template_renderizado)




def ver_personas(request):
    
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})
    
    return HttpResponse(template_renderizado)