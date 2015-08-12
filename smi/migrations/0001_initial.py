# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import sistema.thumbs


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ambulatorio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=150, blank=True)),
                ('email', models.EmailField(max_length=150, blank=True)),
                ('tipo', models.CharField(max_length=100, choices=[(b'Pub', b'Publico'), (b'Priv', b'Privado'), (b'Part', b'Particular')])),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('motivo', models.CharField(max_length=150)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('motivo', models.CharField(max_length=250)),
                ('tratamiento', models.TextField()),
                ('observaciones', models.TextField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
            ],
        ),
        migrations.CreateModel(
            name='Embarazo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parto', models.BooleanField(verbose_name=b'Indique si hubo parto')),
                ('cantidad_hijos', models.IntegerField()),
                ('observaciones', models.TextField()),
                ('motivo_perdida', models.CharField(max_length=150)),
                ('tipo_parto', models.CharField(max_length=100, choices=[(b'Natural', b'Natural'), (b'Cesaria', b'Cesaria')])),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=100, choices=[(b'Diurno', b'Diurno'), (b'Nocturno', b'Nocturno')])),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('ambulatorio', models.ManyToManyField(to='smi.Ambulatorio')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fractura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugar_cuerpo', models.CharField(max_length=150)),
                ('motivo', models.CharField(max_length=150)),
                ('reaccion', models.TextField(verbose_name=b'Reacci\xc3\xb3n', blank=True)),
                ('descripcion', models.TextField(blank=True)),
                ('tratamiento', models.TextField(blank=True)),
                ('fecha', models.DateField()),
                ('dias_reposo', models.IntegerField(blank=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
            ],
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=30)),
                ('peso', models.FloatField()),
                ('estatura', models.FloatField()),
                ('edad', models.IntegerField()),
                ('fecha', models.DateField()),
                ('tension', models.CharField(max_length=50, verbose_name=b'Tensi\xc3\xb3n Arterial')),
                ('ritmo_cardiaco', models.CharField(max_length=100, blank=True)),
                ('motivo', models.CharField(max_length=150, blank=True)),
                ('diagnostico', models.TextField(blank=True)),
                ('hijos', models.BooleanField()),
                ('alergias', models.TextField(blank=True)),
                ('hipertenso', models.BooleanField()),
                ('discapacidades', models.TextField(blank=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_vencimiento', models.DateField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('almacen', models.ForeignKey(to='smi.Almacene')),
            ],
        ),
        migrations.CreateModel(
            name='Medicina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('presentacion', models.CharField(max_length=100)),
                ('imagen', sistema.thumbs.ImageWithThumbsField(upload_to=b'photos')),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(to='smi.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certificado', models.CharField(max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('estado', models.ForeignKey(to='smi.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Operacione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lugar_cuerpo', models.CharField(max_length=150)),
                ('motivo', models.CharField(max_length=150)),
                ('reaccion', models.TextField(verbose_name=b'Reacci\xc3\xb3n', blank=True)),
                ('descripcion', models.TextField(blank=True)),
                ('tratamiento', models.TextField(blank=True)),
                ('fecha', models.DateField()),
                ('dias_reposo', models.IntegerField(blank=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
                ('historia', models.ForeignKey(to='smi.Historia')),
                ('medico', models.ForeignKey(to='smi.Medico')),
            ],
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('municipio', models.ForeignKey(to='smi.Municipio')),
            ],
        ),
        migrations.CreateModel(
            name='Patologia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField(verbose_name=b'Descripcion')),
                ('sintomas', models.TextField()),
                ('tratamiento', models.TextField()),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=50, choices=[(b'H', b'Hombre'), (b'M', b'Mujer')])),
                ('imagen', sistema.thumbs.ImageWithThumbsField(upload_to=b'photos')),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('parroquia', models.ForeignKey(to='smi.Parroquia')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('apellidos', models.CharField(max_length=150)),
                ('nombres', models.CharField(max_length=150)),
                ('cedula', models.CharField(max_length=15)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=150)),
                ('sexo', models.CharField(max_length=50, choices=[(b'H', b'Hombre'), (b'M', b'Mujer')])),
                ('direccion', models.TextField()),
                ('telefono_casa', models.CharField(max_length=20, verbose_name=b'Telefono Casa', blank=True)),
                ('telefono_cel', models.CharField(max_length=20, verbose_name=b'Telefono Celular', blank=True)),
                ('fecha_nac', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('color_piel', models.CharField(max_length=50, verbose_name=b'Color de Piel', blank=True)),
                ('color_ojos', models.CharField(max_length=50, verbose_name=b'Color de Ojos', blank=True)),
                ('color_cabello', models.CharField(max_length=50, verbose_name=b'Color Cabello', blank=True)),
                ('pais_nac', models.CharField(max_length=50, verbose_name=b'Pais Nacimiento', blank=True)),
                ('numero_ss', models.CharField(max_length=30, verbose_name=b'Numero Seguro Social', blank=True)),
                ('numero_hcm', models.CharField(max_length=50, verbose_name=b'Numero HCM', blank=True)),
                ('nombre_hcm', models.CharField(max_length=150, verbose_name=b'Nombre HCM', blank=True)),
                ('imagen', sistema.thumbs.ImageWithThumbsField(upload_to=b'photos', blank=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('parroquia', models.ForeignKey(to='smi.Parroquia')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='medico',
            name='persona',
            field=models.ForeignKey(to='smi.Persona'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='medicina',
            field=models.ForeignKey(to='smi.Medicina'),
        ),
        migrations.AddField(
            model_name='historia',
            name='medico',
            field=models.ForeignKey(to='smi.Medico'),
        ),
        migrations.AddField(
            model_name='historia',
            name='patologias',
            field=models.ManyToManyField(to='smi.Patologia'),
        ),
        migrations.AddField(
            model_name='historia',
            name='persona',
            field=models.ForeignKey(to='smi.Persona'),
        ),
        migrations.AddField(
            model_name='fractura',
            name='historia',
            field=models.ForeignKey(to='smi.Historia'),
        ),
        migrations.AddField(
            model_name='fractura',
            name='medico',
            field=models.ForeignKey(to='smi.Medico'),
        ),
        migrations.AddField(
            model_name='enfermero',
            name='persona',
            field=models.ForeignKey(to='smi.Persona'),
        ),
        migrations.AddField(
            model_name='embarazo',
            name='historia',
            field=models.ForeignKey(to='smi.Historia'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='medicinas',
            field=models.ManyToManyField(to='smi.Medicina'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(to='smi.Medico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='patologias',
            field=models.ManyToManyField(to='smi.Patologia'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='persona',
            field=models.ForeignKey(to='smi.Persona'),
        ),
        migrations.AddField(
            model_name='cita',
            name='medico',
            field=models.ForeignKey(to='smi.Medico'),
        ),
        migrations.AddField(
            model_name='cita',
            name='persona',
            field=models.ForeignKey(to='smi.Persona'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='clase',
            field=models.ForeignKey(to='smi.Clase'),
        ),
        migrations.AddField(
            model_name='ambulatorio',
            name='parroquia',
            field=models.ForeignKey(to='smi.Parroquia'),
        ),
        migrations.AddField(
            model_name='ambulatorio',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='almacene',
            name='ambulatorio',
            field=models.ForeignKey(to='smi.Ambulatorio'),
        ),
    ]
