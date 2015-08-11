# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smi', '0002_medicina_patologia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Embarazo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parto', models.BooleanField(verbose_name=b'Indique si hubo parto')),
                ('cantidad_hijos', models.IntegerField()),
                ('observaciones', models.TextField()),
                ('motivo_perdida', models.CharField(max_length=150)),
                ('tipo_parto', models.CharField(max_length=100, choices=[(b'Natural', b'Natural'), (b'Cesaria', b'Cesaria')])),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
                ('persona', models.ForeignKey(to='smi.Persona')),
            ],
        ),
        migrations.RemoveField(
            model_name='historia',
            name='persona',
        ),
        migrations.AddField(
            model_name='embarazo',
            name='paciente',
            field=models.ForeignKey(to='smi.Paciente'),
        ),
        migrations.AddField(
            model_name='historia',
            name='paciente',
            field=models.ForeignKey(default='', to='smi.Paciente'),
            preserve_default=False,
        ),
    ]
