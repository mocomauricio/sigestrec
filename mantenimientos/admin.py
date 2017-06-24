from django.contrib import admin
from django.contrib.admin.decorators import register
#from mantenimientos.forms import *
from mantenimientos.models import Mantenimiento

# Register your models here.

@register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
	#form = MantenimientoForm

	def save_model(self, request, obj, form, change):
		obj.tipo = 1 #correctivo
		obj.activo = True
		super(MantenimientoAdmin, self).save_model(request, obj, form, change)
