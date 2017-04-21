from django.db import models

# Create your models here.
class TipoDeRecurso(models.Model):
    """ Models que implementa tipos de recursos para la asignacion en recursos"""
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.nombre)


class Recurso(models.Model):
    """Models que implementa Recursos creacion de recursos"""
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    tipo = models.ForeignKey("TipoDeRecurso")
    observaciones = models.TextField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.nombre)
