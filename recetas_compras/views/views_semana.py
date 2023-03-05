from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from ..forms import *
from ..models import Semana
from django.http import HttpResponse

# Create your views here.


class Home(TemplateView):
    template_name = "home.html"


class ListaSemana(ListView):
    model = Semana
    ordering = "fecha_creacion"
    paginate_by = 100
    template_name = "lista_semanas.html"


class CrearSemana(CreateView):
    model = Semana
    fields = ['nombre', 'recetas']
    template_name = 'semana_form.html'
    success_url = reverse_lazy('lista_semanas')

class ActualizarSemana(UpdateView):
    model = Semana
    fields = ['nombre', 'recetas']
    template_name = 'semana_form.html'
    success_url = reverse_lazy('lista_semanas')
  

class DetalleSemana(DetailView):
    model = Semana
    template_name = 'detalle_semana.html'


class BorrarSemana(DeleteView):
    model = Semana
    success_url = reverse_lazy("lista_semanas")
    template_name = "confirm_delete.html"