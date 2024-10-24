from django.urls import path, include
from .views import registro, login_view, HomeView, logout_view, usuario_perfil, editar_perfil
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', usuario_perfil, name='perfil'),
    path('registro/', registro, name='registro'),

    # URLs for password recovery
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # URL for editing profile
    path('editar_perfil/', editar_perfil, name='editar_perfil'),

    path("accounts/", include("allauth.urls")),
]

