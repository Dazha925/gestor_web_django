from django import forms
from .models import usuariolist
# BACKEND: Define el formulario 'UsuarioForm' como un ModelForm
class UsuarioForm(forms.ModelForm):
    class Meta:
        # BACKEND: Asocia el formulario al modelo 'usuariolist'
        model = usuariolist

        # BACKEND: Incluye todos los campos del modelo en el formulario
        fields = '__all__'

        # BACKEND: Personaliza los widgets de entrada para cada campo
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
