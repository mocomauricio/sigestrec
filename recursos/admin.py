from django.contrib import admin
from django.contrib.admin.decorators import register
from recursos.models import *

# Register your models here.
@register(TipoDeRecurso)
class TipoDeRecursoAdmin(admin.ModelAdmin):
	pass

@register(Recurso)
class RecursoAdmin(admin.ModelAdmin):
	pass