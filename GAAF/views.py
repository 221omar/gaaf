from django.shortcuts import render
from django.views.generic import TemplateView

class Inicio (TemplateView):
    template_name = "Paginas/inicio.html"

class prueba (TemplateView):
    template_name = "Paginas/prueba.html"