# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0008_auto_20170623_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(default=1, editable=False, choices=[(0, b'preventivo'), (1, b'correctivo')])),
                ('fecha', models.DateField()),
                ('activo', models.BooleanField(default=True, editable=False)),
                ('recurso', models.ForeignKey(to='recursos.Recurso')),
            ],
        ),
    ]
