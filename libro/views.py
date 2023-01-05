from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView,ListView, UpdateView, CreateView, DeleteView
from .forms import AutorForm, LibroForm
from .models import Autor, Libro

# Create your views here.

# dispatch : valida la peticion y elige que metodo HTTP se utilizo para la solicitud
# http_method_not_allowed(): retorna un error cuando se utiliza un metodo http no soportado o definido
# options():
# TemplateView hereda de view
# ***

class Inicio(TemplateView):
    template_name = 'index.html'
    # def get(self, request, *args, **kwargs):
    #     return render(request,'index.html') 

class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)

class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')

class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class EliminarAutor(DeleteView):
    model = Autor

    def post(self, request, pk, *args, **kwargs):
        object = Autor.objects.get(id=pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')

class ListadoLibro(View):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/listar_libro.html' #queryset = libro.objects.all() -> object_list

    def _get_queryset(self):    # Retorna la consulta
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):   #Retorna la informacion que va hacer enviada al Template
        context = {}
        context['libros'] = self._get_queryset
        context['form'] = self.form_class   #Envio el formulario al template
        return context
    
    def get(self, request, *args, **kwargs):    # Retorna toda la informacion cuando se hace la peticion
        return render(request, self.template_name, self.get_context_data())

    # def post(self,request,*args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('libro:listar_libro')

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listar_libro')

class ActualizarLibro(UpdateView):
    model = Libro
    template_name = 'libro/libro/libro.html'
    form_class = LibroForm
    success_url = reverse_lazy('libro:listar_libro')

    #se realiza la consulta para mostrar en el template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['libros'] = Libro.objects.filter(estado = True)
        return context

class EliminarLibro(DeleteView):
    model = Libro

    def post(self, request, pk, *args, **kwargs):
        object = Libro.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_libro')