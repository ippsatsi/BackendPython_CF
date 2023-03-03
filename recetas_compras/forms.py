from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import M2MRecetario, Receta, Ingrediente


class AgregarRecetaForm(ModelForm):

    class Meta:
        model = Receta
        exclude = ()

class AgregarIngredienteForm(ModelForm):

    class Meta:
        model = M2MRecetario
        exclude = ()

M2mrecetarioFormSet = inlineformset_factory(
    Receta, M2MRecetario, form= AgregarIngredienteForm,
    fields= ['ingrediente', 'cantidad'], extra= 6, can_delete= False
)

M2mrecetarioEditFormSet = inlineformset_factory(
    Receta, M2MRecetario, form= AgregarIngredienteForm,
    fields= ['ingrediente', 'cantidad'], extra= 6, can_delete= True
)