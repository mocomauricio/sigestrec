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
