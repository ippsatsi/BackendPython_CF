from django.shortcuts import render
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from ..forms import *
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
    fields = ['nombre',]
    template_name = 'semana_form.html'
    success_url = reverse_lazy('lista_semanas')

    def get_context_data(self, **kwargs):
        data = super(CrearSemana, self).get_context_data(**kwargs)
        if self.request.POST:
            data['recetas'] = SemanaRecetasFormSet(self.request.POST)
        else:
            data['recetas'] = SemanaRecetasFormSet(queryset=Receta.objects.none())

        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        recetas = context['recetas']
        with transaction.atomic():
            self.object = form.save()

            if recetas.is_valid():
                recetas.instance = self.object
                recetas.save()
        return super(CrearSemana, self).form_valid(form)
    

class DetalleSemana(DetailView):
    model = Semana
    template_name = 'detalle_semana.html'


