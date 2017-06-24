# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0006_auto_20170520_1052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recurso',
            options={},
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='averiado',
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='mantenimiento_preventivo',
        ),
        migrations.AddField(
            model_name='recurso',
            name='estado',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='recurso',
            name='fecha_mantenimiento',
            field=models.DateField(default=datetime.datetime(2017, 6, 23, 17, 17, 55, 272463, tzinfo=utc), verbose_name=b'fecha del proximo manteniento preventivo'),
            preserve_default=False,
        ),
    ]
