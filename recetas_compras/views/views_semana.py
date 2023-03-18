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


class CrearSemana2(CreateView):
    model = Semana
    fields = ['nombre', ]
    template_name = 'semana_form_old.html'
    success_url = reverse_lazy('lista_semanas')

    def get_context_data(self, **kwargs):
        data = super(CrearSemana2, self).get_context_data(**kwargs)
        if self.request.POST:
            data['recetas'] = M2mSemanaFormSet2(self.request.POST)
        else:
            data['recetas'] = M2mSemanaFormSet2()

        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        print(context)
        recetas = context['recetas']
        with transaction.atomic():
            self.object = form.save()

            if recetas.is_valid():
                print('valido')
                recetas.instance = self.object
                recetas.save()
        return super(CrearSemana2, self).form_valid(form)