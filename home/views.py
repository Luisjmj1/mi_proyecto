from re import template
from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random

from home.models import Persona





def crear_personas(request):
    return HttpResponse('')

def ver_personas(request):
    
    personas = Persona.objects.all()
    
    template = loader.get_template('ver_personas.html')
    template_renderizado =template.render({'personas': personas})
    
    return HttpResponse(template_renderizado)