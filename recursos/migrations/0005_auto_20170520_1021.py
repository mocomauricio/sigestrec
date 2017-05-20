# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0004_recurso_averiado'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='creado',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 20, 10, 21, 1, 238467, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recurso',
            name='mantenimiento_preventivo',
            field=models.IntegerField(default=30, verbose_name=b'mantenimiento preventivo (dias)'),
        ),
    ]
