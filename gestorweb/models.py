# Módulo de modelos de Django para definir estructuras de base de datos
from django.db import models

# Modelo de usuario que Django usa para autenticación
from django.contrib.auth.models import User

# Modelo personalizado que extiende la información del usuario
class usuariolist(models.Model):
    # Relación uno a uno con el modelo User (cada usuario tiene una entrada única en usuariolist)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    # Campo adicional para almacenar el correo (puede duplicar o complementar el campo email de User)
    correo = models.EmailField(unique=True,verbose_name="Correo")

    # Representación en texto del objeto (para el panel de administración)
    def __str__(self):
        return f"Usuario: {self.user.username} | Correo: {self.correo}"

'''
class userlist(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100, verbose_name='Usuario')
    correo = models.CharField(max_length=100, verbose_name='Correo')
    contraseña = models.CharField(max_length=100, verbose_name='Contraseña')

    def __str__(self):
        fila = "Usuario: " + self.usuario + " | Correo: " + self.correo + " | Contraseña: " + self.contraseña
        return fila
'''
