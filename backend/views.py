#encoding:utf-8_
from django.shortcuts import render,render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from smi.models import Estado,Municipio,Parroquia,Ambulatorio,Almacene,Categoria,Cita,\
    Clase,Consulta,Enfermero,Especialidade,ManejadorHombres,\
    ManejadorMujeres,Medico,Persona,Perfile
from backend.forms import Perfil
import json
from django.core import serializers
import re

# Create your views here.
@login_required
def index_view(request):

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

def geo(request, type = None, parent_id = None):

    if not request.is_ajax():
        return HttpResponseBadRequest('<h1>%s</h1>' % 'bad request')

    # para testear el efecto loading
    #time.sleep(1);

    locations = {

    ###################################################################
    #    Localidad => [modelo, modelo padre, foreignkey, parent type] #
    ###################################################################
        'estados' : [Estado],
        'municipios' : [Municipio, Estado, 'estado_id', 'estado'],
        'parroquias' : [Parroquia, Municipio, 'municipio_id', 'municipio']
    }

    location_exists = False

    if parent_id != None:
        location_exists = (locations[type][2].objects.filter(id = parent_id).count() > 0)
    else:
        location_exists = (locations[type][0].objects.count() > 0)

    if not location_exists:
        return HttpResponseBadRequest('Identificador inválido')

    data_fields = {
        'estados' : ('id', 'nombre'),
        'municipios' : ('id', 'nombre'),
        'parroquias' : ('id', 'nombre')
    }

    extra_where = None

    if parent_id != None:
        extra_where = ['%s = %d' % (locations[type][2], int(parent_id))]

    location_result = locations[type][0].objects.extra(where = extra_where).values(*data_fields[type]).order_by('id')

    if not location_result.count() > 0:
        return HttpResponseNotFound(json.dumps({'error' : 'empty'}))

    data = {
        'parent' : None,
        'data' : list(location_result)
    }

    if parent_id != None:
        data['parent'] = {
            'id' : parent_id,
            'type' : locations[type][3]
        }

    output = json.dumps(data)

    return HttpResponse(output, content_type = 'application/json')