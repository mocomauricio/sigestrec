from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Caracteristica(models.Model):
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
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey("TipoDeRecurso")
    observaciones = models.TextField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.nombre)

class DetalleDelRecurso(models.Model):
    recurso = models.ForeignKey(Recurso)
    caracteristica = models.ForeignKey(Caracteristica)
    valor = models.CharField(max_length=100, null=True, blank=True)