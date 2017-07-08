# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0012_auto_20170708_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='codigo',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
