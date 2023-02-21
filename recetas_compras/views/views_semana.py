from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from ..models import Semana
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('Hola Mundo')

class Home(TemplateView):
    template_name = "home.html"


class ListaSemana(ListView):
    model = Semana
    ordering = "fecha_creacion"
    paginate_by = 100
    template_name = "lista_semanas.html"


class CrearSemana(CreateView):
    model = Semana
    template_name = 'semana_form.html'
    fields = ['nombre']


class DetalleSemana(DetailView):
    model = Semana
    template_name = 'detalle_semana.html'


