# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0007_auto_20170623_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='estado',
            field=models.IntegerField(default=0, editable=False, choices=[(0, b'disponible'), (1, b'reservado'), (2, b'en mantenimiento')]),
        ),
    ]
