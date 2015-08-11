# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sistema.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('smi', '0003_auto_20150809_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='fecha_nac',
            field=models.DateField(verbose_name=b'Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='imagen',
            field=sistema.thumbs.ImageWithThumbsField(upload_to=b'photos', blank=True),
        ),
    ]
