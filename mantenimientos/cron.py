from mantenimientos.models import *
from recursos.models import *
from reservas.models import Reserva
from datetime import datetime, date, time, timedelta


def enviar_recursos_mantenimiento_preventivo():
	hoy = datetime.now().date()
	recursos = Recurso.objects.exclude(mantenimiento_preventivo=0)

	#solo necesario para exponer
	recursos = recursos.exclude(pk__in=[i.recurso_id for i in Mantenimiento.objects.filter(activo=True, tipo=PREVENTIVO)])
	
	for recurso in recursos:
		diferencia_fechas =  hoy - recurso.creado.date()
		# si no se creo ahora mismo y si llego la cantidad de dias del mantenimiento preventivo
		if((diferencia_fechas.days!=0) and (diferencia_fechas.days % recurso.mantenimiento_preventivo == 0)):
			#se crea el mantenimiento preventivo
			nuevo_mantenimiento = Mantenimiento(recurso_id=recurso.id, tipo=0, fecha=hoy, activo=True)
			nuevo_mantenimiento.save()

			#el recurso pasa a estado "en mantenimiento"
			recurso.estado = 2 #en mantenimiento
			recurso.save()

			#todas las reservas activas del recurso dado deben ser canceladas
			reservas = Reserva.objects.filter(recurso_id=recurso.pk, activo=True)
			for reserva in reservas:
				reserva.cancelado = True
				reserva.fecha_hora_cancelacion = datetime.now()
				reserva.activo = False
				reserva.save()