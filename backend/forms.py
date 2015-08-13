#encoding:utf-8__
_author__ = 'admin'
from django import forms
from  smi.models import Estado,Municipio,Parroquia


class Perfil(forms.Form):

    SEXO_OPTIONS = (
    ('H','Hombre'),
    ('M','Mujer'),)
    estado = forms.ComboField(widget=forms.Select(attrs={'class':'form-control',
                                                               'data-query':'estados'}))

    municipio = forms.ComboField(widget=forms.Select(attrs={'class':'form-control',
                                                            'data-query':'municipios',
                                                            'data-parent':'estado'}))
    parroquia = forms.ComboField(widget=forms.Select(attrs={'class':'form-control',
                                                            'data-query':'parroquias',
                                                            'data-parent':'municipio'}))
    cedula  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    edad =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    sexo =forms.ComboField(widget=forms.Select(attrs={'class':'form-control'},choices=SEXO_OPTIONS))
    imagen = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))