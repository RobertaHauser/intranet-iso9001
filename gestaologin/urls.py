from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PaginaInicial

urlpatterns = [
    path('', PaginaInicial.as_view(),name='index'),
    path('', auth_views.LoginView.as_view(template_name='index.html'), name='index'),
]