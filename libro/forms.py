from django import forms
from .models import Autor

class AutorForm(forms.ModelForm): #puede heredar de ModelForm o Form
    class Meta:
        model = Autor
        fields = ['nombre','apellido','nacionalidad','descripcion']
        labels = {
            'nombre': 'Nombres del autor',
            'apellido': 'Apellidos del autor',
            'nacionalidad': 'Nacionalidad',
            'descripcion': 'Descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese los nombres del autor',
                    'id':'nombre',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos del autor',
                    'id':'apellido',
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese la nacionalidad del autor',
                    'id':'nacionalidad',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Escriba una pequeña descripción del autor',
                    'id':'descripcion',
                }
            )
        }