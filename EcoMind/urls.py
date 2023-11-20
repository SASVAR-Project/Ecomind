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
from web_app import views as webAppViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', webAppViews.home),
    path('home/', webAppViews.home),
    path('my_points/', webAppViews.my_points),
    path('my_activity/', webAppViews.my_activity),
    path('store/', webAppViews.store),
    path('tagging/', webAppViews.tagging),
    path('save_tag/', webAppViews.save_tag),
    path('create_tag/', webAppViews.create_tag),
    path('clasify/', webAppViews.clasify),
    path('clasify_by_tag/', webAppViews.clasify_by_tag),
    path('clasify_by_form/', webAppViews.clasify_by_form),
    path('login/', webAppViews.login1),
    path('register/', webAppViews.register),
    path('logout/', webAppViews.logoutUser),
    path('credits/', webAppViews.credits),
]
