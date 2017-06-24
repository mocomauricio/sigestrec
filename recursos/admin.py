from django.contrib import admin
from django.contrib.admin.decorators import register
from recursos.models import *
from recursos.forms import *
from mantenimientos.models import Mantenimiento

# Register your models here.

@register(Caracteristica)
class CaracteristicaAdmin(admin.ModelAdmin):
	pass

@register(TipoDeRecurso)
class TipoDeRecursoAdmin(admin.ModelAdmin):
	form = TipoDeRecursoForm
	filter_horizontal = ('caracteristicas',)

class DetalleDelRecursoInlineAdmin(admin.TabularInline):
	form = DetalleDelRecursoForm
	model = DetalleDelRecurso
	extra = 0

@register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
	change_form_template = 'recurso_form.html'
	inlines = [DetalleDelRecursoInlineAdmin]

	def save_model(self, request, obj, form, change):
		super(RecursoAdmin, self).save_model(request, obj, form, change)
		mantenimientos = Mantenimiento.objects.filter(recurso_id=obj.pk, tipo=0, activo=True)
		for manteniento in mantenimientos:
			manteniento.activo=False
			manteniento.save()

		nuevo_mantenimiento = Mantenimiento(recurso_id=obj.pk, tipo=0, fecha=obj.fecha_mantenimiento, activo=True)
		nuevo_mantenimiento.save()