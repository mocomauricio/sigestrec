# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleDelTipoDeRecurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caracteristica', models.CharField(max_length=50)),
                ('requerido', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='tipoderecurso',
            name='encargado',
            field=models.ForeignKey(verbose_name=b'Encargado del recurso', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='detalledeltipoderecurso',
            name='tipo_de_recuso',
            field=models.ForeignKey(to='recursos.TipoDeRecurso'),
        ),
    ]
