# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0010_auto_20170705_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='borrado',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
