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
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=100)),
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
                ('observacione', models.TextField()),
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=100, choices=[(b'Diurno', b'Diurno'), (b'Nocturno', b'Nocturno')])),
            ],
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=30)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
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
                ('operaciones', models.BooleanField()),
                ('fractura', models.BooleanField()),
                ('embarazo', models.BooleanField()),
                ('hijo', models.BooleanField()),
                ('alergia', models.BooleanField()),
                ('hipertenso', models.BooleanField()),
                ('discapacidades', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certificado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('estado', models.ForeignKey(to='smi.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=150)),
                ('municipio', models.ForeignKey(to='smi.Municipio')),
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
                ('fecha_nac', models.DateField(blank=True)),
                ('color_piel', models.CharField(max_length=50, verbose_name=b'Color de Piel', blank=True)),
                ('color_ojos', models.CharField(max_length=50, verbose_name=b'Color de Ojos', blank=True)),
                ('color_cabello', models.CharField(max_length=50, verbose_name=b'Color Cabello', blank=True)),
                ('pais_nac', models.CharField(max_length=50, verbose_name=b'Pais Nacimiento', blank=True)),
                ('numero_ss', models.CharField(max_length=30, verbose_name=b'Numero Seguro Social', blank=True)),
                ('numero_hcm', models.CharField(max_length=50, verbose_name=b'Numero HCM', blank=True)),
                ('nombre_hcm', models.CharField(max_length=150, verbose_name=b'Nombre HCM', blank=True)),
                ('imagen', sistema.thumbs.ImageWithThumbsField(upload_to=b'photos')),
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
            model_name='historia',
            name='persona',
            field=models.ForeignKey(to='smi.Persona'),
        ),
        migrations.AddField(
            model_name='enfermero',
            name='persona',
            field=models.ForeignKey(to='smi.Persona'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(to='smi.Medico'),
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
