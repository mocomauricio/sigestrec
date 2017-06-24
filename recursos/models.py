from django.db import models
from mantenimientos.models import *
from django.contrib.auth.models import User

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
    caracteristicas = models.ManyToManyField(Caracteristica)

    def __unicode__(self):
        return unicode(self.nombre)

DISPONIBLE = 0
RESERVADO = 1
EN_MANTENIMIENTO = 2
ESTADO_RECURSO = (
    (DISPONIBLE, 'disponible'),
    (RESERVADO, 'reservado'),
    (EN_MANTENIMIENTO, 'en mantenimiento')
)

class Recurso(models.Model):
    """
    Modelo que implementa la definicion de un recurso
    """

    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey("TipoDeRecurso")
    observaciones = models.TextField(max_length=1000, null=True, blank=True)
    fecha_mantenimiento = models.DateField(verbose_name="fecha del proximo manteniento preventivo")
    estado = models.IntegerField(default=DISPONIBLE, editable=False, choices=ESTADO_RECURSO)
    creado = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.nombre)
    """
    def save(self, *args, **kwargs):
        super(Recurso, self).save(*args, **kwargs)
        mantenimientos = Mantenimiento.objects.filter(recurso_id=self.pk, tipo=0, activo=True)
        for manteniento in mantenimientos:
            manteniento.activo=False
            manteniento.save()

        nuevo_mantenimiento = Mantenimiento(recurso_id=self.pk, tipo=0, fecha=self.fecha_mantenimiento, activo=True)
        nuevo_mantenimiento.save()
    """


class DetalleDelRecurso(models.Model):
    recurso = models.ForeignKey(Recurso)
    caracteristica = models.ForeignKey(Caracteristica)
    valor = models.CharField(max_length=100, null=True, blank=True)