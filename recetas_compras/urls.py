from django.urls import path
from .views.views_semana import Home
from .views.views_ingredientes import ListaIngrediente

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("lista_ingredientes/", ListaIngrediente.as_view(), name="lista_ingredientes"),
    # path('', index, name='index'),
]