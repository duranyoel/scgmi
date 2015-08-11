#encoding:utf-8_
from django.shortcuts import render,render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.models import User
from smi.models import Estado,Municipio,Parroquia,Ambulatorio,Almacene,Categoria,Cita,\
    Clase,Consulta,Enfermero,Especialidade,ManejadorHombres,\
    ManejadorMujeres,Medico,Persona,Perfile
from backend.forms import Perfil
# Create your views here.

@login_required
def index_view(request):
    #usu = User.objects.select_related().get(id = request.session['id_u'])
    return render_to_response('inicio.html', context=RequestContext(request))

def perfil_view(request):
    formulario = Perfil()
    if request.method=='POST':
        cedula = request.POST.get('cedula','')
        edad  = request.POST.get('edad','')
        sexo = request.POST.get('sexo','')
        imagen = request.POST.get('imagen', '')


        formulario = Perfil(request.POST)
        if formulario.is_valid():
            Perfile.cedula=cedula
            Perfile.edad=edad
            Perfile.sexo= sexo
            Perfile.imagen= imagen
            Perfile.save()

            return HttpResponseRedirect('/backend/')
    return render(request, 'perfil.html', {'formulario':formulario})
