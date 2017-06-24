from django.db import models
from django.contrib.auth.models import User

PREVENTIVO = 0
CORRECTIVO = 1
TIPO_MANTENIMIENTO=(
	(PREVENTIVO, "preventivo"),
	(CORRECTIVO, "correctivo")
)

# Create your models here.
class Mantenimiento(models.Model):

    recurso = models.ForeignKey("recursos.Recurso")
    tipo = models.IntegerField(default = CORRECTIVO, choices=TIPO_MANTENIMIENTO, editable=False)
    fecha = models.DateField()
    activo = models.BooleanField(default=True, editable=False)
    
    def __unicode__(self):
        return unicode(self.recurso.nombre)