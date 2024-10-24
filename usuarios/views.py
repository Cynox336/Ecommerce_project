from msilib.schema import ListView
from urllib import request
from django.views.generic import ListView
from django.shortcuts import redirect, render
from .forms import RegistroForm,EditarPerfilForm
from .models import Usuario
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView



# @login_required
# def home(request):
#     return render(request, 'home.html')
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html" 
# Create your views here.
# @login_required
def  usuario_perfil(request):
    return render(request,'perfil.html')


# class UsuarioListView(ListView):
#     model = Usuario
#     template_name = 'perfil.html'
#     context_object_name = 'perfilusuarios'



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)

        if user is not None:
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect("home")  # Cambia "home" por la ruta a donde quieras redirigir
    else:
        form = RegistroForm()
    return render(request, "registro.html", {"form": form})


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # O la URL a la que quieras redirigir
    else:
        form = EditarPerfilForm(instance=request.user)

    return render(request, 'editar_perfil.html', {'form': form})
