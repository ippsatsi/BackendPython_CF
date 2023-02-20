from django.views.generic import ListView, DetailView
from ..models import Receta

class ListaReceta(ListView):
    model = Receta
    ordering = "nombre"
    paginate_by = 100
    template_name = "lista_recetas.html"


class DetalleReceta(DetailView):
    model = Receta
    template_name = 'detalle_receta.html'
    