from django.urls import path
from . import views

urlpatterns = [
    #  Ruta raíz: inicio de sesión 
    path('', views.login_usuario, name='login'),  

    # Ruta: Registro de nuevos usuarios
    path('registrar/', views.registrar, name="registrar"),

    # Ruta: Recuperación de contraseña
    path('recuperacion', views.recuperacion, name="recuperacion"),

    # Ruta: Página principal protegida (requiere login para acceder)
    path('inicio/', views.inicio, name='inicio'),

    # Ruta: Contacto con desarrolladores (enlaces a WhatsApp)
    path('nosotros', views.nosotros, name='nosotros'),

    # Ruta: Envío de correo desde el formulario de contacto
    path('enviar-correo/', views.enviar_correo, name='enviar_correo'),

    # Ruta: Listado de usuarios registrados
    path('usuarios', views.usuarios, name='usuarios'),

    # Ruta: Edición de usuario (con ID específico)
    path('usuarios/editar_usuario/<int:id>', views.editar_usuario, name="editar_usuario"),

    # Ruta: Confirmación de eliminación (con ID específico)
    path('usuarios/eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),

    # Ruta: Ejecución de eliminación (con ID específico)
    path('usuarios/confirmacion_eliminar_usuario/<int:id>', views.confirmacion_eliminar_usuario, name="confirmacion_eliminar_usuario"),
]

