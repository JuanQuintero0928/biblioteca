"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.contrib.auth.views import LoginView, logout_then_login  #Para iniciar y cerrar sesion
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from libro.views import Inicio
from usuario.views import Login, LogoutUsuario

urlpatterns = [
    path("admin/", admin.site.urls),
    path('libro/',include(('libro.urls','libro'))),
    path('',login_required(Inicio.as_view()), name='index'),
    # path('accounts/login/',LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', logout_then_login, name='logout'),
    # path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/login/',Login.as_view(), name ='login'),
    path('logout/',login_required(LogoutUsuario), name='logout'),
]
