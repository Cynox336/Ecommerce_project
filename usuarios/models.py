from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


# Create your models here.

class Usuario(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)
    preferencias_tema = models.CharField(max_length=20, choices=[('claro', 'Claro'), ('oscuro', 'Oscuro')], default='claro')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    f_nacimiento = models.DateField(null=True, blank=True)
    domicilio = models.CharField(max_length=200)
    bio = models.TextField(max_length=500, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Cambia este nombre para evitar conflicto
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Cambia este nombre para evitar conflicto
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )




class DireccionEnvio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,
    related_name='direcciones')
    direccion = models.CharField(max_length=255,
    verbose_name='Dirección')
    ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    codigo_postal = models.CharField(max_length=10,
    verbose_name='Código Postal')
    pais = models.CharField(max_length=50, verbose_name='País')
    fecha_creacion = models.DateTimeField(auto_now_add=True,
    verbose_name='Fecha de creación')






class RegistroForm(UserCreationForm):
        email = forms.EmailField(required=True)
        class Meta:
                model = User
                fields = ['username', 'email', 'password1', 'password2']