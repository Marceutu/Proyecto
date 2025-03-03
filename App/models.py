import uuid
from django.db import models

class Animal(models.Model):
    TIPO_ANIMAL_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
    ]
    
    codigo_registro = models.CharField(max_length=36, unique=True, blank=False, null=False)  # UUID siempre presente
    tipo_animal = models.CharField(max_length=50, choices=TIPO_ANIMAL_CHOICES, null=True, blank=True)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    descripcion = models.TextField()
    estado_salud = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.codigo_registro:
            self.codigo_registro = str(uuid.uuid4())  # Genera un UUID único
        super().save(*args, **kwargs)

    class Meta:
        app_label = 'App'
