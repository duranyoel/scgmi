# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smi', '0005_auto_20150810_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='medicinas',
            field=models.ManyToManyField(to='smi.Medicina'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='patologias',
            field=models.ManyToManyField(to='smi.Patologia'),
        ),
    ]
