# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0009_auto_20170625_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='borrado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='estado',
            field=models.IntegerField(default=0, editable=False, choices=[(0, b'disponible'), (1, b'reservado'), (2, b'en mantenimiento'), (3, b'en uso')]),
        ),
    ]
