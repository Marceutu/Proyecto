from django import forms
from .models import Animal

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['tipo_animal', 'sexo', 'edad', 'descripcion', 'estado_salud']


