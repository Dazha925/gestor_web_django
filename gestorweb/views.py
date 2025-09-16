# Renderiza plantillas HTML y redirige entre vistas
from django.shortcuts import render, redirect

# Modelo extendido de usuario (relación con User)
from .models import usuariolist  # acceso a datos adicionales del usuario

# Decorador para proteger vistas que requieren autenticación
from django.contrib.auth.decorators import login_required  # aplicado en la vista 'inicio'

# Sistema de mensajes para mostrar alertas en el frontend
from django.contrib import messages  # Se usa en login, registro y recuperación (mensajes de error y éxito)

# Modelo base de usuarios de Django (tabla auth_user)
from django.contrib.auth.models import User  # Crear, buscar y modificar usuarios

# Funciones de autenticación y gestión de sesión
from django.contrib.auth import authenticate, login  # Logica en la vista 'login_usuario'

from django.conf import settings

from django.core.mail import send_mail

# Vista para iniciar sesión (django)
def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return render(request, 'login/sesion.html')

    return render(request, 'login/sesion.html')

# Vista para registrar nuevos usuarios
def registrar(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        password = request.POST['password']
        confirmar = request.POST['confirmar']

        if password != confirmar:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'login/registrar.html')

        if User.objects.filter(username=nombre).exists():
            messages.error(request, "El nombre de usuario ya está registrado.")
            return render(request, 'login/registrar.html')

        user = User.objects.create_user(username=nombre, email=email, password=password)
        usuariolist.objects.create(user=user, correo=email)

        messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
        return redirect('login')

    return render(request, 'login/registrar.html')

# Vista para recuperar contraseña por correo (sin envío de codigo a email)
def recuperacion(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        confirmar = request.POST.get('confirmar')

        if password != confirmar:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'login/recuperacion.html')

        try:
            user = User.objects.get(email=correo)
            user.set_password(password)
            user.save()
            messages.success(request, "Contraseña actualizada correctamente.")
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "No se encontró un usuario con ese correo.")
            return render(request, 'login/recuperacion.html')
    return render(request, 'login/recuperacion.html')

# Vista  de entrada al sistema protegida (requiere login)
@login_required
def inicio(request):
    return render(request, 'paginas/inicio.html')

# Vista para contactar al desarrollador 
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

# Vista para enviar correo desde el formulario de contacto
def enviar_correo(request):
    if request.method == 'POST':
        remitente = request.POST.get('remitente')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        mensaje_completo = f"Mensaje enviado por: {remitente}\n\n{mensaje}"

        send_mail(
            subject=asunto,
            message=mensaje_completo,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['jajr1305@gmail.com'],  # correo fijo
            fail_silently=False,
        )
        return redirect('nosotros')


# Vista para listar usuarios registrados (tabla)
def usuarios(request):
    listado_usuarios = usuariolist.objects.select_related('user').all()
    return render(request, 'usuarios/index.html', {'usuarios': listado_usuarios})

# Vista para editar datos de un usuario (formulario)
def editar_usuario(request, id):
    usuario_extendido = usuariolist.objects.get(id=id)
    usuario = usuario_extendido.user

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        nueva_contraseña = request.POST.get('password')

        usuario.username = username
        usuario.email = email
        if nueva_contraseña:
            usuario.set_password(nueva_contraseña)
        usuario.save()

        usuario_extendido.correo = email
        usuario_extendido.save()

        return redirect('usuarios')

    return render(request, 'usuarios/editar.html', {
        'usuario': usuario,
        'usuario_extendido': usuario_extendido
    })

# Vista para confirmar eliminación de usuario 
def eliminar_usuario(request, id):
    usuario = usuariolist.objects.get(id=id)
    return render(request, 'usuarios/eliminar.html', {'user': usuario})

# Vista que ejecuta la eliminación del usuario
def confirmacion_eliminar_usuario(request, id):
    usuario = usuariolist.objects.get(id=id)
    usuario.user.delete()  # Elimina el usuario relacionado en auth_user
    usuario.delete()
    return redirect('usuarios')

