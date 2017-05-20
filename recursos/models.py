from django.db import models
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



class Recurso(models.Model):
    """
    Modelo que implementa la definicion de un recurso
    """
    class Meta:
        permissions = (
            ("averiar_recurso", "Puede marcar como averiado un recurso"),
            ("reparar_recurso", "Puede marcar como reparado un recurso"),
        )

    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey("TipoDeRecurso")
    observaciones = models.TextField(max_length=1000, null=True, blank=True)
    mantenimiento_preventivo = models.IntegerField(default=30, verbose_name="mantenimiento preventivo (dias)")
    creado = models.DateTimeField(auto_now_add=True)
    averiado = models.BooleanField(default=False, editable=False)

    def __unicode__(self):
        return unicode(self.nombre)

class DetalleDelRecurso(models.Model):
    recurso = models.ForeignKey(Recurso)
    caracteristica = models.ForeignKey(Caracteristica)
    valor = models.CharField(max_length=100, null=True, blank=True)