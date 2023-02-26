from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import M2MRecetario, Receta, Ingrediente


class AgregarIngredienteForm(ModelForm):

    class Meta:
        model = M2MRecetario
        fields =