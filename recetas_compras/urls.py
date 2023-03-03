from django.urls import path
from .views.views_semana import Home
from .views.views_ingredientes import ListaIngrediente, CrearIngrediente, DetalleIngrediente, BorrarIngrediente, ActualizarIngrediente
from .views.views_recetas import ListaReceta, DetalleReceta, CrearReceta, BorrarReceta, ActualizarReceta
from .views.views_semana import ListaSemana, DetalleSemana, CrearSemana

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("lista_ingredientes/", ListaIngrediente.as_view(), name="lista_ingredientes"),
    path("lista_recetas/", ListaReceta.as_view(), name="lista_recetas"),
    path("lista_semanas/", ListaSemana.as_view(), name="lista_semanas"),
    path("ingrediente/create", CrearIngrediente.as_view(), name="crear_ingrediente"),
    path("ingrediente/delete/<int:pk>", BorrarIngrediente.as_view(), name="borrar_ingrediente"),
    path("ingrediente/edit/<int:pk>", ActualizarIngrediente.as_view(), name="actualizar_ingrediente"),
    path("ingrediente/<int:pk>", DetalleIngrediente.as_view(), name="detalle_ingrediente"),
    path("semana/create", CrearSemana.as_view(), name="crear_semana"),
    path("semana/<int:pk>", DetalleSemana.as_view(), name="detalle_semana"),
    path("receta/create", CrearReceta.as_view(), name="crear_receta"),
    path("receta/<int:pk>", DetalleReceta.as_view(), name="detalle_receta"),
    path("receta/delete/<int:pk>", BorrarReceta.as_view(), name="borrar_receta"),
    path("receta/edit/<int:pk>", ActualizarReceta.as_view(), name="actualizar_receta"),
    # path('', index, name='index'),
]