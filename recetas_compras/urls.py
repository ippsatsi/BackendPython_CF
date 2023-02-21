from django.urls import path
from .views.views_semana import Home
from .views.views_ingredientes import ListaIngrediente, CrearIngrediente, DetalleIngrediente
from .views.views_recetas import ListaReceta, DetalleReceta
from .views.views_semana import ListaSemana, DetalleSemana, CrearSemana

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("lista_ingredientes/", ListaIngrediente.as_view(), name="lista_ingredientes"),
    path("lista_recetas/", ListaReceta.as_view(), name="lista_recetas"),
    path("lista_semanas/", ListaSemana.as_view(), name="lista_semanas"),
    path("ingrediente/create", CrearIngrediente.as_view(), name="crear_ingrediente"),
    path("ingrediente/<pk>", DetalleIngrediente.as_view(), name="detalle_ingrediente"),
    path("semana/create", CrearSemana.as_view(), name="crear_semana"),
    path("semana/<pk>", DetalleSemana.as_view(), name="detalle_semana"),
    path("receta/<pk>", DetalleReceta.as_view(), name="detalle_receta"),

    # path('', index, name='index'),
]