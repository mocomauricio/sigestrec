from django.db import models

# Create your models here.
class TipoDeRecurso(models.Model):
    """ 
    Modelo que implementa tipos de recursos para la clasificacion en recursos
    """
    nombre = models.CharField(max_length=100)

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
