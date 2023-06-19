from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Categoria, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['idproducto', 'nombre', 'modelo', 'imagen', 'categoria']
        labels = {
            'idproducto': 'Idproducto',
            'nombre': 'Nombre',
            'modelo': 'Modelo',
            'imagen': 'Imagen',
            'categoria': 'Categoria'
        }
        widgets = {
            'idproducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Idproducto..',
                    'id': 'codigo',
                }
            ),
            'nombre':forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre..',
                    'id': 'marca',
                }
            ),
            'modelo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese modelo..',
                    'id': 'modelo',
                }
            ),
            'imagen':forms.FileInput(
                attrs={
                    'id': 'imagen',
                    'class': 'form-control',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id':'categoria',
                }
            )

        }