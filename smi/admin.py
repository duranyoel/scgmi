#encoding:utf-8
from django.contrib import admin
from smi.models import Persona, Estado, \
    Municipio, Parroquia, Medico,\
    Ambulatorio,Almacene,Clase,Categoria,\
    Consulta,Especialidade,Enfermero,Cita,\
    Perfile,Historia,Medicina,Patologia,Embarazo,\
    Fractura,Operacione
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres','apellidos','cedula','parroquia')

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')

class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nombre','estado')

class ParroquiaAdmin(admin.ModelAdmin):
    list_display = ('nombre','municipio')

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('persona','certificado')

class AmbulatorioAdmin(admin.ModelAdmin):
    list_display = ('nombre','parroquia','telefono','tipo')

class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre','ambulatorio')

class ClaseAdmin(admin.ModelAdmin):
    list_display = ('referencia','nombre')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('referencia','nombre','clase')

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('ambulatorio','persona','medico')

class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('codigo','nombre')

class EnfermeroAdmin(admin.ModelAdmin):
    list_display = ('persona','turno')

class CitaAdmin(admin.ModelAdmin):
    list_display = ('persona','ambulatorio','medico','fecha','hora')

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario','cedula','edad','sexo')

class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('persona','codigo','fecha')

class MedicinaAdmin(admin.ModelAdmin):
    list_display = ('nombre','referencia','categoria')

class PatologiaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion','sintomas','tratamiento')

class EmbarazoAdmin(admin.ModelAdmin):
    list_display = ('historia','parto','cantidad_hijos','observaciones')

class FracturaAdmin(admin.ModelAdmin):
    list_display = ('historia','medico','ambulatorio','fecha','motivo')

class OperacioneAdmin(admin.ModelAdmin):
    list_display = ('historia','medico','ambulatorio','fecha','motivo')

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Ambulatorio, AmbulatorioAdmin)
admin.site.register(Almacene, AlmacenAdmin)
admin.site.register(Clase, ClaseAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Enfermero,EnfermeroAdmin)
admin.site.register(Especialidade,EspecialidadeAdmin)
admin.site.register(Cita,CitaAdmin)
admin.site.register(Historia,HistoriaAdmin)
admin.site.register(Perfile,PerfilAdmin)
admin.site.register(Medicina,MedicinaAdmin)
admin.site.register(Patologia,PatologiaAdmin)
admin.site.register(Embarazo,EmbarazoAdmin)
admin.site.register(Fractura,FracturaAdmin)
admin.site.register(Operacione,OperacioneAdmin)