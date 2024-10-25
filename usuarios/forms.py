from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ["username", "email", "password1", "password2"]

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'foto_perfil', 'bio', 'domicilio', 'f_nacimiento', 'preferencias_tema']
        widgets = {
            'f_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'foto_perfil': forms.FileInput(attrs={'accept': 'image/*'}),
        }
