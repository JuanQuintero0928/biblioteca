from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListadoAutor, ActualizarAutor, CrearAutor, EliminarAutor, ListadoLibro, CrearLibro, ActualizarLibro, EliminarLibro

urlpatterns = [
    path('crear_autor/', login_required(CrearAutor.as_view()), name='crear_autor'),
    path('listar_autor/', login_required(ListadoAutor.as_view()) , name='listar_autor'),
    path('editar_autor/<int:pk>', login_required(ActualizarAutor.as_view()), name='editar_autor'),
    path('eliminar_autor/<int:pk>',login_required(EliminarAutor.as_view()), name='eliminar_autor'),

    path('listar_libro/', login_required(ListadoLibro.as_view()), name='listar_libro'),
    path('crear_libro/', login_required(CrearLibro.as_view()), name='crear_libro'),
    path('editar_libro/<int:pk>', login_required(ActualizarLibro.as_view()), name='editar_libro'),
    path('eliminar_libro/<int:pk>', login_required(EliminarLibro.as_view()), name='eliminar_libro'),
]