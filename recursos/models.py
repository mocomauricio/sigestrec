from django.db import models
from mantenimientos.models import *
from django.contrib.auth.models import User
from reservas.models import *

# Create your models here.
class Caracteristica(models.Model):
    """ 
    Modelo que implementa caracteristicas de la plantilla de los tipos de recursos
    """
    descripcion = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.descripcion)


class TipoDeRecurso(models.Model):
    """ 
    Modelo que implementa tipos de recursos para la clasificacion en recursos
    """
    nombre = models.CharField(max_length=100)
    encargado = models.ForeignKey(User, null=True, blank=False, verbose_name="Encargado del recurso")
    caracteristicas = models.ManyToManyField(Caracteristica, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.nombre)

DISPONIBLE = 0
RESERVADO = 1
EN_MANTENIMIENTO = 2
EN_USO = 3
ESTADO_RECURSO = (
    (DISPONIBLE, 'disponible'),
    (RESERVADO, 'reservado'),
    (EN_MANTENIMIENTO, 'en mantenimiento'),
    (EN_USO, 'en uso')
)

class Recurso(models.Model):
    """
    Modelo que implementa la definicion de un recurso
    """

    codigo = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey("TipoDeRecurso")
    observaciones = models.TextField(max_length=1000, null=True, blank=True)
    mantenimiento_preventivo = models.IntegerField(default=0, verbose_name="Mantenimiento preventido (dias)")
    estado = models.IntegerField(default=DISPONIBLE, editable=False, choices=ESTADO_RECURSO)
    creado = models.DateTimeField(auto_now_add=True)
    borrado = models.BooleanField(default=False, editable=False)

    def __unicode__(self):
        return unicode(self.nombre)

    def get_adjudicado(self):
        las_reservas = Reserva.objects.filter(recurso_id=self.id, activo=True).order_by('-fecha', 'hora_inicio', 'grado_prioridad_solicitante')
        print las_reservas
        if las_reservas.count() > 0:
            una_reserva = las_reservas[0]
            return una_reserva.solicitante
        return None


class DetalleDelRecurso(models.Model):
    recurso = models.ForeignKey(Recurso)
    caracteristica = models.ForeignKey(Caracteristica)
    valor = models.CharField(max_length=100, null=True, blank=True)