# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0005_auto_20170520_1021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recurso',
            options={'permissions': (('averiar_recurso', 'Puede marcar como averiado un recurso'), ('reparar_recurso', 'Puede marcar como reparado un recurso'))},
        ),
    ]
