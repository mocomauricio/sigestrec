# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0011_auto_20170706_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoderecurso',
            name='caracteristicas',
            field=models.ManyToManyField(to='recursos.Caracteristica', null=True, blank=True),
        ),
    ]
