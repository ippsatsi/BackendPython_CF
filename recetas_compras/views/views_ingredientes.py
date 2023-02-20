from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from ..models import Ingrediente

class ListaIngrediente(ListView):
    model = Ingrediente
    ordering = "nombre"
    paginate_by = 100
    template_name = "lista_ingredientes.html"
    

class CrearIngrediente(CreateView):
    model = Ingrediente
    template_name = 'ingrediente_form.html'
    fields = ['nombre', 'tipo_ingrediente', 'tipo_unidad']

class DetalleIngrediente(DetailView):
    model = Ingrediente
    template_name = 'detalle_ingrediente.html'