#encoding:utf-8
from django.core.mail import send_mail
from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth,sessions
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from smi.forms import Registrarse

# Create your views here.
def index_view(request):
    return render_to_response('index.html', context=RequestContext(request))

def registrarse(request):
    formulario = Registrarse()
    if request.method=='POST':
        apellido = request.POST.get('apellido','')
        nombre  = request.POST.get('nombre','')
        correo = request.POST.get('email','')
        usuario = request.POST.get('usuario', '')
        clave = request.POST.get('password', '')

        formulario = Registrarse(request.POST)
        if formulario.is_valid():

            cd = formulario.cleaned_data

            # send_mail(
            # 'Registro de Usuario',
            # 'Registro de Usuario',
            # cd.get('email', 'noreply@example.com'),
            # ['sistemaspruebas01@gmail.com'],)
            user = User.objects._create_user(username=usuario,
                                         email=correo,password=clave,
                                         is_staff=False,is_superuser=False)
            user.last_name=apellido
            user.first_name=nombre

            user.save()
            return HttpResponseRedirect('/smi/gracias/')
    return render(request, 'registrarse.html', {'formulario':formulario})

@login_required
def admin_index(request):
    return render_to_response('admin_index.html', context=RequestContext(request))

def ingresar_view(request):

    errors=[]

    if request.method == 'POST':
        username = request.POST.get('usuario', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        try:

            if user.is_active:
                # Contraseña correcta y usuario marcado como "activo"
                auth.login(request, user)
                # Redireccciona a una página de entrada correcta.
                return HttpResponseRedirect("/backend/")

            else:
                errors.append('Disculpe su usuario no esta activo.')

        except User.DoesNotExist:
            errors.append('Disculpe el usuario o contraseña son erroneas.')

    return render(request,'ingresar.html', {'errors':errors})

def registro_view(request):
    errors=[]

    if request.method == 'POST':
        apellido = request.POST.get('apellido','')
        nombre  = request.POST.get('nombre','')
        correo = request.POST.get('email','')
        usuario = request.POST.get('usuario', '')
        clave = request.POST.get('password', '')
        reppassword = request.POST.get('reppassword', '')
        condiciones = request.POST.get('terminos','')
        if clave != reppassword:
          errors.append('Las Contraseñas no son iguales.')

        elif condiciones == '':
            errors.append('Debe Aceptar Los Terminos.')
        elif correo=='':
             errors.append('Debe Ingresar Un Correo.')
        elif apellido=='' or  nombre=='':
             errors.append('Debe Ingresar Apellido y Nombre.')
        else:
            user = User.objects._create_user(username=usuario,
                                         email=correo,password=clave,
                                         is_staff=False,is_superuser=False)
            user.last_name=apellido
            user.first_name=nombre

            user.save()
            errors.append('Felicidades ya estas registrado.')

    return render(request,'registro.html', {'errors':errors})


def gracias_view(request):
    return render_to_response('gracias.html', context=RequestContext(request))

def logout(request):
    auth.logout(request)

    # Redireccciona a una página de entrada correcta.
    return HttpResponseRedirect("/")

