from fileinput import close
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Context, Template, loader
import random
from home.models import Persona
from home.models import Familia


def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'La hora y fecha actual es {fecha_y_hora}')

def hola(request):
    return HttpResponse('Holaaaaaaaaaaaaaaaaaaa')


def crear_familia(request, nombre, apellido):
    
    familia = Familia(nombre=nombre, apellido=apellido, edad=random.randrange(1, 99), fecha_nacimiento=datetime.now())
    familia.save()
    
    template = loader.get_template('crear_familia.html')
    template_renderizado = template.render({'familia': familia})
    
    return HttpResponse(template_renderizado)




def ver_personas(request):
    
    personas = Familia.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado = template.render({'personas': personas})
    
    return HttpResponse(template_renderizado)