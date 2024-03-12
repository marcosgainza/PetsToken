from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    historia_clinica = models.TextField()
    foto = models.ImageField(upload_to='fotos_mascotas/', null=True, blank=True)

    def __str__(self):
        return self.nombre

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Otros campos personalizados
    
    # Especifica un related_name único para el campo groups
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    
    # Especifica un related_name único para el campo user_permissions
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Reemplaza CustomUser por tu modelo de usuario si es necesario
        fields = ('username', 'email', 'password1', 'password2')  # Campos requeridos para el registro