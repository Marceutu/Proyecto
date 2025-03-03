from django.contrib import admin
from .models import Animal  # Importar el modelo Animal, no Perro ni Gato

admin.site.register(Animal)  # Registrar el modelo Animal en el admin
