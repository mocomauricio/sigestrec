from django.contrib import admin
from django.contrib.admin.decorators import register
from mantenimientos.forms import *
from mantenimientos.models import Mantenimiento

from reservas.models import Reserva
from datetime import datetime, date, time, timedelta

# Register your models here.

from django.core.mail import EmailMessage

def enviar_notificacion(asunto, mensaje, destinatario):
	email = EmailMessage(asunto, mensaje, to=[destinatario.email])
	email.send()

@register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
	form = MantenimientoForm

	def save_model(self, request, obj, form, change):
		if change == False:
			obj.tipo = 1 #correctivo
			obj.activo = True

			recurso = obj.recurso
			recurso.estado = 2 #mantenimiento
			recurso.save()

			#todas las reservas activas del recurso dado deben ser canceladas
			reservas = Reserva.objects.filter(recurso_id=recurso.pk, activo=True)
			for reserva in reservas:
				reserva.cancelado = True
				reserva.fecha_hora_cancelacion = datetime.now()
				reserva.activo = False
				reserva.save()


				enviar_notificacion(
					asunto="Cancelacion de reserva",
					mensaje="Usted cancelo su reserva del recurso " + reserva.recurso.nombre,
					destinatario=reserva.solicitante
				)

		super(MantenimientoAdmin, self).save_model(request, obj, form, change)


	def delete_model(self, request, obj):
		recurso = obj.recurso
		recurso.estado = 0 #disponible
		recurso.save()
		super(MantenimientoAdmin, self).delete_model(request, obj)