from django.db import models
from django.contrib.auth import get_user_model

class Album(models.Model):
    nombre = models.CharField(max_length=150)
    artista = models.CharField(max_length=150)
    genero = models.CharField(max_length=80)
    anio = models.PositiveIntegerField(verbose_name="Año")
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    creado_por = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-creado_en']

    def __str__(self):
        return f"{self.artista} - {self.nombre} ({self.anio})"
