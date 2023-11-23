# outfits/forms.py
from django import forms
from .models import Outfit



class OutfitForm(forms.ModelForm):
    class Meta:
        model = Outfit
        fields = ['genero', 'estilo_prenda', 'color_prenda', 'imagen']

    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]

    ESTILO_CHOICES = [
        ('Casual', 'Casual'),
        ('Deportivo', 'Deportivo'),
        ('Elegante', 'Elegante'),
        ('Urbano', 'Urbano'),
    ]

    COLOR_CHOICES = [
        ('Negro', 'Negro'),
        ('Blanco', 'Blanco'),
        ('Beige', 'Beige'),
        ('Gris', 'Gris'),
        ('Azul', 'Azul'),
    ]

    genero = forms.ChoiceField(choices=GENERO_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    estilo_prenda = forms.ChoiceField(choices=ESTILO_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    color_prenda = forms.ChoiceField(choices=COLOR_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    imagen = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
