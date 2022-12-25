from django import forms
from .models import Autor

class AutorForm(forms.ModelForm): #puede heredar de ModelForm o Form
    class Meta:
        model = Autor
        fields = ['nombre','apellido','nacionalidad','descripcion']