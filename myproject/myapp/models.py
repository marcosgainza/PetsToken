from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    historia_clinica = models.TextField()
    foto = models.ImageField(upload_to='fotos_mascotas/', null=True, blank=True)

    def __str__(self):
        return self.nombre
