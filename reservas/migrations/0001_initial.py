# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recursos', '0008_auto_20170623_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('activo', models.BooleanField()),
                ('recurso', models.ForeignKey(to='recursos.Recurso')),
                ('solicitante', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
