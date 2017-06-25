from django.contrib import admin
from django.contrib.admin.decorators import register
from mantenimientos.forms import *
from mantenimientos.models import Mantenimiento

# Register your models here.

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

		super(MantenimientoAdmin, self).save_model(request, obj, form, change)


	def delete_model(self, request, obj):
		recurso = obj.recurso
		recurso.estado = 0 #disponible
		recurso.save()
		super(MantenimientoAdmin, self).delete_model(request, obj)