from django.db import models
from mantenimientos.models import *
from django.contrib.auth.models import User

# Create your models here.
class Reserva(models.Model):
    """ 
    Modelo que implementa reservas de recursos
    """
    recurso = models.ForeignKey('recursos.Recurso')
    solicitante = models.ForeignKey(User)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    activo = models.BooleanField(default=True, editable=False)

    def __unicode__(self):
        return unicode(self.recurso.nombre)