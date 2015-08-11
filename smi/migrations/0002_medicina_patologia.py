# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sistema.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('smi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(verbose_name=b'Descripci\xc3\xb3n', blank=True)),
                ('presentacion', models.CharField(max_length=100)),
                ('imagen', sistema.thumbs.ImageWithThumbsField(upload_to=b'photos')),
                ('categoria', models.ForeignKey(to='smi.Categoria')),
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
            ],
        ),
    ]
