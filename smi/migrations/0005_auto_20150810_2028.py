# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smi', '0004_auto_20150809_2003'),
    ]

    operations = [
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
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
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
                ('ambulatorio', models.ForeignKey(to='smi.Ambulatorio')),
            ],
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='ambulatorio',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='persona',
        ),
        migrations.RenameField(
            model_name='consulta',
            old_name='observacione',
            new_name='observaciones',
        ),
        migrations.RemoveField(
            model_name='embarazo',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='historia',
            name='embarazo',
        ),
        migrations.RemoveField(
            model_name='historia',
            name='fractura',
        ),
        migrations.RemoveField(
            model_name='historia',
            name='operaciones',
        ),
        migrations.RemoveField(
            model_name='historia',
            name='paciente',
        ),
        migrations.AddField(
            model_name='cita',
            name='motivo',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='embarazo',
            name='historia',
            field=models.ForeignKey(default=1, to='smi.Historia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enfermero',
            name='ambulatorio',
            field=models.ManyToManyField(to='smi.Ambulatorio'),
        ),
        migrations.AddField(
            model_name='historia',
            name='ambulatorio',
            field=models.ForeignKey(default=1, to='smi.Ambulatorio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historia',
            name='medico',
            field=models.ForeignKey(default=1, to='smi.Medico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historia',
            name='persona',
            field=models.ForeignKey(default=1, to='smi.Persona'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
        migrations.AddField(
            model_name='operacione',
            name='historia',
            field=models.ForeignKey(to='smi.Historia'),
        ),
        migrations.AddField(
            model_name='operacione',
            name='medico',
            field=models.ForeignKey(to='smi.Medico'),
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
    ]
