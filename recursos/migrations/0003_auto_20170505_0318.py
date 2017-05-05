# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0002_auto_20170504_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleDelRecurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.CharField(max_length=100, null=True, blank=True)),
                ('caracteristica', models.ForeignKey(to='recursos.Caracteristica')),
                ('recurso', models.ForeignKey(to='recursos.Recurso')),
            ],
        ),
        migrations.RemoveField(
            model_name='detalledeltipoderecurso',
            name='tipo_de_recuso',
        ),
        migrations.DeleteModel(
            name='DetalleDelTipoDeRecurso',
        ),
        migrations.AddField(
            model_name='tipoderecurso',
            name='caracteristicas',
            field=models.ManyToManyField(to='recursos.Caracteristica'),
        ),
    ]
