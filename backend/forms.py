#encoding:utf-8__
_author__ = 'admin'
from django import forms

class Perfil(forms.Form):
    SEXO_OPTIONS = (
    ('H','Hombre'),
    ('M','Mujer'),)
    cedula  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    edad =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sexo =forms.ComboField(widget=forms.Select(attrs={'class':'form-control'},choices=SEXO_OPTIONS))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))