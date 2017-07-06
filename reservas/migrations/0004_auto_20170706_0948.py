# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_auto_20170705_1147'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reserva2',
        ),
        migrations.CreateModel(
            name='MiReserva',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('reservas.reserva',),
        ),
        migrations.AlterModelOptions(
            name='reserva',
            options={'permissions': (('cancelar_reserva', 'Puede cancelar la reserva'), ('entregar_recurso', 'Puede entregar el recurso'), ('recibir_recurso', 'Puede recibir el recurso'), ('imprimir_comprobante', 'Puede imprimir comprobante'))},
        ),
        migrations.AddField(
            model_name='reserva',
            name='notificacion_enviada',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
