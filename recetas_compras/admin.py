from django.contrib import admin
from .models import Ingrediente, Receta, Semana, M2M_Recetario

# Register your models here.
admin.site.register(Ingrediente)
admin.site.register(Receta)
admin.site.register(Semana)
admin.site.register(M2M_Recetario)