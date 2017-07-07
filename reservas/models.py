from django.db import models
from mantenimientos.models import *
from django.contrib.auth.models import User
from datetime import datetime, date, time
# Create your models here.

BOOLEANO =( (True, 'SI'), (False,'NO') )


HORAS_RESERVA =(
    (time(6,0,0), '6:00'),
    (time(6,30,0), '6:30'),

    (time(7,0,0), '7:00'),
    (time(7,30,0), '7:30'),

    (time(8,0,0), '8:00'),
    (time(8,30,0), '8:30'),

    (time(9,0,0), '9:00'),
    (time(9,30,0), '9:30'),

    (time(10,0,0), '10:00'),
    (time(10,30,0), '10:30'),

    (time(11,0,0), '11:00'),
    (time(11,30,0), '11:30'),

    (time(12,0,0), '12:00'),
    (time(12,30,0), '12:30'),

    (time(13,0,0), '13:00'),
    (time(13,30,0), '13:30'),

    (time(14,0,0), '14:00'),
    (time(14,30,0), '14:30'),

    (time(15,0,0), '15:00'),
    (time(15,30,0), '15:30'),

    (time(16,0,0), '16:00'),
    (time(16,30,0), '16:30'),

    (time(17,0,0), '17:00'),
    (time(17,30,0), '17:30'),

    (time(18,0,0), '18:00'),
    (time(18,30,0), '18:30'),

    (time(19,0,0), '19:00'),
    (time(19,30,0), '19:30'),

    (time(20,0,0), '20:00'),
    (time(20,30,0), '20:30'),

    (time(21,0,0), '21:00'),
    (time(21,30,0), '21:30'),

    (time(22,0,0), '22:00'),
    (time(22,30,0), '22:30'),

    (time(23,0,0), '23:00'),
    (time(23,30,0), '23:30')

    )


class Reserva(models.Model):
    """ 
    Modelo que implementa reservas de recursos
    """
    class Meta:
        permissions = (
            ("cancelar_reserva", "Puede cancelar la reserva"),
            ("entregar_recurso", "Puede entregar el recurso"),
            ("recibir_recurso", "Puede recibir el recurso"),
            ("imprimir_comprobante", "Puede imprimir comprobante"),

        )

    tipo_recurso = models.ForeignKey('recursos.TipoDeRecurso')
    recurso = models.ForeignKey('recursos.Recurso', null=True, blank=True)
    solicitante = models.ForeignKey(User)
    fecha = models.DateField(default=date.today, editable=False)
    hora_inicio = models.TimeField(choices=HORAS_RESERVA)
    hora_fin = models.TimeField(choices=HORAS_RESERVA)
    activo = models.BooleanField(default=True, editable=False, choices=BOOLEANO)
    cancelado = models.BooleanField(default=False, editable=False,choices=BOOLEANO)
    entregado = models.BooleanField(default=False, editable=False, choices=BOOLEANO)
    devuelto = models.BooleanField(default=False, editable=False, choices=BOOLEANO)
    creado = models.DateTimeField(auto_now_add=True)
    grado_prioridad_solicitante = models.IntegerField(default=0, editable=False)

    fecha_hora_entrega = models.DateTimeField(null=True, blank=True, editable=False)
    fecha_hora_devolucion = models.DateTimeField(null=True, blank=True, editable=False)
    fecha_hora_cancelacion = models.DateTimeField(null=True, blank=True, editable=False)

    notificacion_enviada = models.BooleanField(default=False, editable=False, choices=BOOLEANO)


    def __unicode__(self):
        return unicode(self.id)

    def posicion_en_cola(self):
        pass


class MiReserva(Reserva):
    class Meta:
        proxy = True

