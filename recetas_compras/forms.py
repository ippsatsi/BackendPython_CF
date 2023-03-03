from django import forms
from django.forms import Select, ModelForm, inlineformset_factory, modelformset_factory
from .models import M2MRecetario, Receta, Semana


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


class AgregarRecetaForm(ModelForm):
    # Debemos usar como nombre del campo como variable
    nombre = forms.ModelChoiceField(queryset=Receta.objects.all())

SemanaRecetasFormSet = modelformset_factory(
    Receta, fields= ['nombre',], form= AgregarRecetaForm, extra= 7, can_delete= False
)