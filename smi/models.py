#encoding:utf-8
from django.db import models
from sistema.thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from django.utils.timezone import LocalTimezone
# Create your models here.

#Estados
class Estado(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self): # __unicode__ en Python 2
        return self.nombre

#Municipios
class Municipio(models.Model):
    estado = models.ForeignKey(Estado)
    nombre = models.CharField(max_length=150)

    def __str__(self): # __unicode__ en Python 2
        return self.nombre

#Parroquias
class Parroquia(models.Model):
    municipio =  models.ForeignKey(Municipio)
    nombre = models.CharField(max_length=150)

    def __str__(self): # __unicode__ en Python 2
        return self.nombre

#Especialidades
class Especialidade(models.Model):
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)

    def __str__(self): # __unicode__ en Python 2
        return self.nombre

#Personas
class ManejadorHombres(models.Manager):
    def get_query_set(self):
        return  super(ManejadorHombres,self).get_query_set().filter(sexo='H')


class ManejadorMujeres(models.Manager):
    def get_query_set(self):
        return  super(ManejadorMujeres,self).get_query_set().filter(sexo='M')


class Persona(models.Model):
    SEXO_OPTIONS = (
    ('H','Hombre'),
    ('M','Mujer'),
    )
    usuario =models.ForeignKey(User)
    parroquia = models.ForeignKey(Parroquia)
    apellidos = models.CharField(max_length=150)
    nombres = models.CharField(max_length=150)
    cedula  = models.CharField(max_length=15)
    edad = models.IntegerField()
    email = models.EmailField(max_length=150)
    sexo = models.CharField(max_length=50, choices=SEXO_OPTIONS)
    hombre  = ManejadorHombres()
    mujer   = ManejadorMujeres()
    gente   = models.Manager()
    direccion   = models.TextField()
    telefono_casa = models.CharField(max_length=20,verbose_name='Telefono Casa',blank=True)
    telefono_cel = models.CharField(max_length=20, verbose_name='Telefono Celular',blank=True)
    fecha_nac   =  models.DateField(verbose_name='Fecha de Nacimiento')
    color_piel  = models.CharField(max_length=50,verbose_name='Color de Piel',blank=True)
    color_ojos  = models.CharField(max_length=50, verbose_name='Color de Ojos',blank=True)
    color_cabello = models.CharField(max_length=50,verbose_name='Color Cabello',blank=True)
    pais_nac = models.CharField(max_length=50,verbose_name='Pais Nacimiento',blank=True)
    numero_ss = models.CharField(max_length=30,verbose_name='Numero Seguro Social',blank=True)
    numero_hcm = models.CharField(max_length=50,verbose_name='Numero HCM',blank=True)
    nombre_hcm = models.CharField(max_length=150,verbose_name='Nombre HCM',blank=True)
    imagen = ImageWithThumbsField(upload_to='photos', sizes=((125,125),(200,200)),verbose_name='Imágen',blank=True)


    def __str__(self): # __unicode__ en Python 2
        return self.nombres

#Medicos
class Medico(models.Model):
    persona = models.ForeignKey(Persona)
    certificado = models.CharField(max_length=100)

    def __str__(self): # __unicode__ en Python 2
        return self.certificado

#Ambulatorio
class Ambulatorio(models.Model):
    TIPO_OPCION = (
        ('Pub','Publico'),
        ('Priv','Privado'),
        ('Part','Particular'),
    )
    usuario =models.ForeignKey(User)
    parroquia = models.ForeignKey(Parroquia)
    nombre = models.CharField(max_length=150)
    direccion = models.TextField()
    telefono = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    tipo = models.CharField(max_length=100,choices=TIPO_OPCION)

    def __str__(self): # __unicode__ en Python 2
        return self.nombre

#Almacen
class Almacene(models.Model):
    ambulatorio = models.ForeignKey(Ambulatorio)
    nombre  = models.CharField(max_length=150)

    def __str__(self): # __unicode__ en Python 2
        return self.nombre

#Clase
class Clase(models.Model):
    referencia = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)

    def __str__(self): # __unicode__ en Python 2
        return self.nombre

#Categorias
class Categoria(models.Model):
    clase = models.ForeignKey(Clase)
    referencia = models.CharField(max_length=50)
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()

    def __str__(self): # __unicode__ en Python 2
        return self.nombre

class Patologia(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(verbose_name='Descripcion')
    sintomas = models.TextField()
    tratamiento = models.TextField()
    def __str__(self):
        return self.nombre

class Medicina(models.Model):
    categoria = models.ForeignKey(Categoria)
    referencia = models.CharField(max_length=50)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(verbose_name='Descripción',blank=True)
    presentacion = models.CharField(max_length=100)
    imagen = ImageWithThumbsField(upload_to='photos', sizes=((125,125),(200,200)),verbose_name='Imágen')
    def __str__(self):
        return self.referencia

class Inventario(models.Model):
    medicina = models.ForeignKey(Medicina)
    almacen= models.ForeignKey(Almacene)
    cantidad = models.IntegerField()
    fecha_vencimiento= models.DateField()
    def __str__(self):
       return self.medicina

#Consultas
class Consulta(models.Model):
    persona = models.ForeignKey(Persona)
    ambulatorio = models.ForeignKey(Ambulatorio)
    medico =models.ForeignKey(Medico)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=250)
    patologias = models.ManyToManyField(Patologia)
    medicinas = models.ManyToManyField(Medicina)
    tratamiento = models.TextField()
    observaciones = models.TextField()

    def __str__(self): # __unicode__ en Python 2
        return self.persona


class Enfermero(models.Model):
    TURNO_OPCION = (
        ('Diurno','Diurno'),
        ('Nocturno','Nocturno'),

    )
    persona= models.ForeignKey(Persona)
    turno = models.CharField(choices=TURNO_OPCION,max_length=100)
    ambulatorio = models.ManyToManyField(Ambulatorio)

    def __str__(self): # __unicode__ en Python 2
        return self.persona


class Cita(models.Model):
    persona = models.ForeignKey(Persona)
    medico = models.ForeignKey(Medico)
    ambulatorio = models.ForeignKey(Ambulatorio)
    motivo = models.CharField(max_length=150)
    fecha = models.DateField()
    hora = models.TimeField()


    def __str__(self): # __unicode__ en Python 2
        return self.persona

class Perfile(models.Model):
    SEXO_OPTIONS = (
    ('H','Hombre'),
    ('M','Mujer'),
    )
    usuario =models.ForeignKey(User)
    parroquia = models.ForeignKey(Parroquia)
    cedula  = models.CharField(max_length=15)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=50, choices=SEXO_OPTIONS)
    imagen = ImageWithThumbsField(upload_to='photos', sizes=((125,125),(200,200)),verbose_name='Imágen')
    def __str__(self): # __unicode__ en Python 2
        return self.cedula

class Historia(models.Model):
    persona= models.ForeignKey(Persona)
    ambulatorio = models.ForeignKey(Ambulatorio)
    medico = models.ForeignKey(Medico)
    codigo= models.CharField(max_length=30)
    peso = models.FloatField()
    estatura = models.FloatField()
    edad = models.IntegerField()
    fecha = models.DateField()
    tension = models.CharField(max_length=50,verbose_name='Tensión Arterial')
    ritmo_cardiaco = models.CharField(blank=True,max_length=100)
    motivo = models.CharField(blank=True,max_length=150)
    diagnostico = models.TextField(blank=True)
    patologias = models.ManyToManyField(Patologia)
    hijos = models.BooleanField(blank=True)
    alergias= models.TextField(blank=True)
    hipertenso=models.BooleanField(blank=True)
    discapacidades=models.TextField(blank=True)
    def __str__(self): # __unicode__ en Python 2
        return self.codigo


class Embarazo(models.Model):
    OPTIONS = (
    ('Natural','Natural'),
    ('Cesaria','Cesaria'),
    )
    historia=models.ForeignKey(Historia)
    parto = models.BooleanField(blank=True,verbose_name='Indique si hubo parto')
    cantidad_hijos=models.IntegerField()
    observaciones=models.TextField()
    motivo_perdida=models.CharField(max_length=150)
    tipo_parto =models.CharField(max_length=100,choices=OPTIONS)
    def __str__(self):
        return self.paciente

class  Fractura(models.Model):
    historia=models.ForeignKey(Historia)
    medico =models.ForeignKey(Medico)
    ambulatorio = models.ForeignKey(Ambulatorio)
    lugar_cuerpo = models.CharField(max_length=150)
    motivo = models.CharField(max_length=150)
    reaccion = models.TextField(verbose_name='Reacción',blank=True)
    descripcion = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    fecha = models.DateField()
    dias_reposo= models.IntegerField(blank=True)
    def __str__(self):
        return self.historia

class Operacione(models.Model):
    historia = models.ForeignKey(Historia)
    medico = models.ForeignKey(Medico)
    ambulatorio = models.ForeignKey(Ambulatorio)
    lugar_cuerpo = models.CharField(max_length=150)
    motivo = models.CharField(max_length=150)
    reaccion = models.TextField(verbose_name='Reacción',blank=True)
    descripcion = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    fecha = models.DateField()
    dias_reposo= models.IntegerField(blank=True)
    def __str__(self):
        return self.historia
