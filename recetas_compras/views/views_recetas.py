from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.db import transaction
from ..forms import *
from ..models import Receta, Ingrediente

class ListaReceta(ListView):
    model = Receta
    ordering = "nombre"
    paginate_by = 100
    template_name = "lista_recetas.html"


class CrearReceta(CreateView):
    model = Receta
    fields = ['nombre', 'image', 'ingr_principal', 'preparacion']
    template_name = 'receta2_form.html'
    success_url = reverse_lazy('lista_recetas')

    def get_context_data(self, **kwargs):
        data = super(CrearReceta, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ingredientes'] = M2mrecetarioFormSet(self.request.POST)
        else:
            data['ingredientes'] = M2mrecetarioFormSet()

        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        ingredientes = context['ingredientes']
        with transaction.atomic():
            self.object = form.save()

            if ingredientes.is_valid():
                ingredientes.instance = self.object
                ingredientes.save()
        return super(CrearReceta, self).form_valid(form)

        

class DetalleReceta(DetailView):
    model = Receta
    template_name = 'detalle_receta.html'

    # funcion para obtener las cantidades y unidades que estan en la tabla intermedia
    def get_context_data(self, **kwargs):
        context = super(DetalleReceta, self).get_context_data(**kwargs)
        lista_ingredientes = []
        m2m_lista = self.object.m2mrecetario_set.all()

        for m2m_ingrediente in self.object.m2mrecetario_set.all():
            dict_ingr = {}
            dict_ingr['cantidad'] = m2m_ingrediente.cantidad
            ingrediente_id = m2m_ingrediente.ingrediente_id
            dict_ingr['unidad'] = Ingrediente.objects.get(id= ingrediente_id).get_tipo_unidad_display()
            dict_ingr['nombre'] = Ingrediente.objects.get(id= ingrediente_id).nombre
            lista_ingredientes.append(dict_ingr)

        if lista_ingredientes:
            context["lista_ingre"] = lista_ingredientes

        return context
    

class BorrarReceta(DeleteView):
    model = Receta
    success_url = reverse_lazy("lista_recetas")
    template_name = "confirm_delete.html"