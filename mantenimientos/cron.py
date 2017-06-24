from mantenimientos.models import *
from datetime import * 

def enviar_recursos_mantenimiento_preventivo():
	mantenimientos = Mantenimiento.objects.filter(activo=True, tipo=PREVENTIVO)

	for mantenimiento in mantenimientos:
		if mantenimiento.fecha <= date.today():
			recurso = mantenimiento.recurso
			recurso.estado = 2 # en mantenimiento
			recurso.save()