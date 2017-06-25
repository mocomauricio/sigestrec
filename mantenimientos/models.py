from django.db import models
from django.contrib.auth.models import User
from datetime import date
PREVENTIVO = 0
CORRECTIVO = 1
TIPO_MANTENIMIENTO=(
	(PREVENTIVO, "preventivo"),
	(CORRECTIVO, "correctivo")
)

# Create your models here.
class Mantenimiento(models.Model):
	class Meta:
		permissions = (
			("aprobar_mantenimiento", "Puede aprobar un mantenimiento"),
		)
	recurso = models.ForeignKey("recursos.Recurso")
	tipo = models.IntegerField(default = CORRECTIVO, choices=TIPO_MANTENIMIENTO, editable=False)

	responsable = models.CharField(max_length=100, null=True, blank=True)
	costo  = models.CharField(max_length=100, null=True, blank=True)
	fecha_de_devolucion = models.DateField(null=True, blank=True)
	observaciones = models.TextField(max_length=1000, null=True, blank=True)

	fecha = models.DateField(default=date.today, editable=False)
	activo = models.BooleanField(default=True, editable=False)
	
	def __unicode__(self):
		return unicode(self.recurso.nombre)