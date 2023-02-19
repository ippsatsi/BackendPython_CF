from django.views.generic import ListView
from ..models import Ingrediente

class ListaIngrediente(ListView):
    model = Ingrediente
    ordering = "nombre"
    paginate_by = 100
    template_name = "lista_ingredientes.html"
    