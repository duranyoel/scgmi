#encoding:utf-8__
_author__ = 'admin'
from django import forms
from  smi.models import Estado,Municipio,Parroquia

class Perfil(forms.Form):

    SEXO_OPTIONS = (
    ('H','Hombre'),
    ('M','Mujer'),)
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    municipio = forms.ModelChoiceField(queryset=Estado.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    parroquia = forms.ModelChoiceField(queryset=Estado.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    cedula  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    edad =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sexo =forms.ComboField(widget=forms.Select(attrs={'class':'form-control'},choices=SEXO_OPTIONS))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))