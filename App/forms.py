from django import forms
from .models import Animal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['tipo_animal', 'sexo', 'edad', 'descripcion', 'estado_salud']


