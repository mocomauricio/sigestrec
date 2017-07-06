# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0010_auto_20170705_1147'),
        ('reservas', '0002_auto_20170625_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva2',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('reservas.reserva',),
        ),
        migrations.AddField(
            model_name='reserva',
            name='cancelado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='reserva',
            name='creado',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 5, 11, 46, 56, 679280, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='devuelto',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='reserva',
            name='entregado',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_hora_cancelacion',
            field=models.DateTimeField(null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_hora_devolucion',
            field=models.DateTimeField(null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='fecha_hora_entrega',
            field=models.DateTimeField(null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='reserva',
            name='grado_prioridad_solicitante',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='reserva',
            name='tipo_recurso',
            field=models.ForeignKey(default=1, to='recursos.TipoDeRecurso'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reserva',
            name='recurso',
            field=models.ForeignKey(blank=True, to='recursos.Recurso', null=True),
        ),
    ]
