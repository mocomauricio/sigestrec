# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mantenimientos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimiento',
            name='costo',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='fecha_de_devolucion',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='observaciones',
            field=models.TextField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='responsable',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='fecha',
            field=models.DateField(default=datetime.date.today, editable=False),
        ),
    ]
