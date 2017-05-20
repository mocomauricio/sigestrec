# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_auto_20170505_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='averiado',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
