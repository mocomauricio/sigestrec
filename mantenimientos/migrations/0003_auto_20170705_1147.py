# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimientos', '0002_auto_20170625_1120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mantenimiento',
            options={'permissions': (('aprobar_mantenimiento', 'Puede aprobar un mantenimiento'),)},
        ),
    ]
