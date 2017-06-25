# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0008_auto_20170623_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurso',
            name='fecha_mantenimiento',
        ),
        migrations.AddField(
            model_name='recurso',
            name='mantenimiento_preventivo',
            field=models.IntegerField(default=0, verbose_name=b'Mantenimiento preventido (dias)'),
        ),
    ]
