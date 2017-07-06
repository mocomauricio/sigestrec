from django.db import models
from mantenimientos.models import *
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
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
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activo = models.BooleanField(default=True, editable=False)
    cancelado = models.BooleanField(default=False, editable=False)
    entregado = models.BooleanField(default=False, editable=False)
    devuelto = models.BooleanField(default=False, editable=False)
    creado = models.DateTimeField(auto_now_add=True)
    grado_prioridad_solicitante = models.IntegerField(default=0, editable=False)

    fecha_hora_entrega = models.DateTimeField(null=True, blank=True, editable=False)
    fecha_hora_devolucion = models.DateTimeField(null=True, blank=True, editable=False)
    fecha_hora_cancelacion = models.DateTimeField(null=True, blank=True, editable=False)

    notificacion_enviada = models.BooleanField(default=False, editable=False)


    def __unicode__(self):
        return unicode(self.id)

    def posicion_en_cola(self):
        pass


class MiReserva(Reserva):
    class Meta:
        proxy = True

