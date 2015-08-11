#encoding:utf-8__
_author__ = 'admin'
from django import forms

class Registrarse(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email =forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    usuario=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    reppassword= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_nombre(self):
        nombre =self.cleaned_data['nombre']
        return nombre
    def clean_apellido(self):
        apellido=self.cleaned_data['apellido']
        return apellido
    def clean_email(self):
        email =self.cleaned_data['email']
        return email
    def clean_usuario(self):
        usuario= self.cleaned_data['usuario']

        return usuario
    def clean_password(self):
        password = self.cleaned_data['password']
        return password
    def clean_reppassword(self):
        reppassword =self.cleaned_data['reppassword']
        password = self.cleaned_data['password']
        if password != reppassword:
             raise forms.ValidationError("Las Contraseñas No Son Iguales!")
        return reppassword
