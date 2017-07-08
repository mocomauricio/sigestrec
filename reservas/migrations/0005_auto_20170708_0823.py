# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_auto_20170706_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='activo',
            field=models.BooleanField(default=True, editable=False, choices=[(True, b'SI'), (False, b'NO')]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='cancelado',
            field=models.BooleanField(default=False, editable=False, choices=[(True, b'SI'), (False, b'NO')]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='devuelto',
            field=models.BooleanField(default=False, editable=False, choices=[(True, b'SI'), (False, b'NO')]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='entregado',
            field=models.BooleanField(default=False, editable=False, choices=[(True, b'SI'), (False, b'NO')]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha',
            field=models.DateField(default=datetime.date.today, editable=False),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_fin',
            field=models.TimeField(choices=[(datetime.time(6, 0), b'6:00'), (datetime.time(6, 30), b'6:30'), (datetime.time(7, 0), b'7:00'), (datetime.time(7, 30), b'7:30'), (datetime.time(8, 0), b'8:00'), (datetime.time(8, 30), b'8:30'), (datetime.time(9, 0), b'9:00'), (datetime.time(9, 30), b'9:30'), (datetime.time(10, 0), b'10:00'), (datetime.time(10, 30), b'10:30'), (datetime.time(11, 0), b'11:00'), (datetime.time(11, 30), b'11:30'), (datetime.time(12, 0), b'12:00'), (datetime.time(12, 30), b'12:30'), (datetime.time(13, 0), b'13:00'), (datetime.time(13, 30), b'13:30'), (datetime.time(14, 0), b'14:00'), (datetime.time(14, 30), b'14:30'), (datetime.time(15, 0), b'15:00'), (datetime.time(15, 30), b'15:30'), (datetime.time(16, 0), b'16:00'), (datetime.time(16, 30), b'16:30'), (datetime.time(17, 0), b'17:00'), (datetime.time(17, 30), b'17:30'), (datetime.time(18, 0), b'18:00'), (datetime.time(18, 30), b'18:30'), (datetime.time(19, 0), b'19:00'), (datetime.time(19, 30), b'19:30'), (datetime.time(20, 0), b'20:00'), (datetime.time(20, 30), b'20:30'), (datetime.time(21, 0), b'21:00'), (datetime.time(21, 30), b'21:30'), (datetime.time(22, 0), b'22:00'), (datetime.time(22, 30), b'22:30'), (datetime.time(23, 0), b'23:00'), (datetime.time(23, 30), b'23:30')]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora_inicio',
            field=models.TimeField(choices=[(datetime.time(6, 0), b'6:00'), (datetime.time(6, 30), b'6:30'), (datetime.time(7, 0), b'7:00'), (datetime.time(7, 30), b'7:30'), (datetime.time(8, 0), b'8:00'), (datetime.time(8, 30), b'8:30'), (datetime.time(9, 0), b'9:00'), (datetime.time(9, 30), b'9:30'), (datetime.time(10, 0), b'10:00'), (datetime.time(10, 30), b'10:30'), (datetime.time(11, 0), b'11:00'), (datetime.time(11, 30), b'11:30'), (datetime.time(12, 0), b'12:00'), (datetime.time(12, 30), b'12:30'), (datetime.time(13, 0), b'13:00'), (datetime.time(13, 30), b'13:30'), (datetime.time(14, 0), b'14:00'), (datetime.time(14, 30), b'14:30'), (datetime.time(15, 0), b'15:00'), (datetime.time(15, 30), b'15:30'), (datetime.time(16, 0), b'16:00'), (datetime.time(16, 30), b'16:30'), (datetime.time(17, 0), b'17:00'), (datetime.time(17, 30), b'17:30'), (datetime.time(18, 0), b'18:00'), (datetime.time(18, 30), b'18:30'), (datetime.time(19, 0), b'19:00'), (datetime.time(19, 30), b'19:30'), (datetime.time(20, 0), b'20:00'), (datetime.time(20, 30), b'20:30'), (datetime.time(21, 0), b'21:00'), (datetime.time(21, 30), b'21:30'), (datetime.time(22, 0), b'22:00'), (datetime.time(22, 30), b'22:30'), (datetime.time(23, 0), b'23:00'), (datetime.time(23, 30), b'23:30')]),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='notificacion_enviada',
            field=models.BooleanField(default=False, editable=False, choices=[(True, b'SI'), (False, b'NO')]),
        ),
    ]
