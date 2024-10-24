from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario  
from django.contrib.auth.models import User
from django import forms



class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User  # Usamos el modelo de usuario
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
    
class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'foto_perfil', 'bio', 'domicilio', 'f_nacimiento', 'preferencias_tema']

        # Opcionalmente, podemos usar widgets personalizados para ciertos campos.
        widgets = {
            'f_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }


