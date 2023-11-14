"""EcoMind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_1 import views as app1Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1Views.home),
    path('home/', app1Views.home),
    path('mis_puntos/', app1Views.mis_puntos),
    path('mi_actividad/', app1Views.mi_actividad),
    path('store/', app1Views.tienda),
    path('etiquetado/', app1Views.etiquetado),
    path('etiqueta_exito/', app1Views.etiquetaExito),
    path('realizar_etiquetado/', app1Views.realizar_etiquetado),
    path('clasificado/', app1Views.clasificado),
    path('clasificado_etiqueta/', app1Views.clasificado_etiqueta),
    path('clasificado_formulario/', app1Views.clasificado_formulario),
    path('login/', app1Views.login1),
    path('registro/', app1Views.registro),
    path('logout/', app1Views.logoutUser),
    path('creditos/', app1Views.creditos),
]
