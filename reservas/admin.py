# -*- coding: utf-8 -*-


from django.contrib import admin
from django.contrib.admin.decorators import register
from reservas.models import *
from reservas.forms import *


@register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
	form = ReservaForm
	change_form_template = 'reserva_form.html'

	def save_model(self, request, obj, form, change):
		solicitante = obj.solicitante
		
		if solicitante.groups.filter(name='Titular').exists():
			obj.grado_prioridad_solicitante = 1 

		elif solicitante.groups.filter(name='Adjunto').exists():
			obj.grado_prioridad_solicitante = 2

		elif solicitante.groups.filter(name='Asistente').exists():
			obj.grado_prioridad_solicitante = 3 

		elif solicitante.groups.filter(name='Encargado de catedra').exists():
			obj.grado_prioridad_solicitante = 4 

		elif solicitante.groups.filter(name='Auxiliar de enseñanza').exists():
			obj.grado_prioridad_solicitante = 5 

		elif solicitante.groups.filter(name='Alumno').exists():
			obj.grado_prioridad_solicitante = 6 

		elif solicitante.groups.filter(name='Funcionario').exists():
			obj.grado_prioridad_solicitante = 7

		else:		 
			obj.grado_prioridad_solicitante = 999999


		super(ReservaAdmin, self).save_model(request, obj, form, change)

@register(MiReserva)
class MiReservaAdmin(admin.ModelAdmin):
	form = MiReservaForm
	change_form_template = 'reserva_form.html'
	
	def save_model(self, request, obj, form, change):
		solicitante = request.user
		
		if solicitante.groups.filter(name='Titular').exists():
			obj.grado_prioridad_solicitante = 1 

		elif solicitante.groups.filter(name='Adjunto').exists():
			obj.grado_prioridad_solicitante = 2

		elif solicitante.groups.filter(name='Asistente').exists():
			obj.grado_prioridad_solicitante = 3 

		elif solicitante.groups.filter(name='Encargado de catedra').exists():
			obj.grado_prioridad_solicitante = 4 

		elif solicitante.groups.filter(name='Auxiliar de enseñanza').exists():
			obj.grado_prioridad_solicitante = 5 

		elif solicitante.groups.filter(name='Alumno').exists():
			obj.grado_prioridad_solicitante = 6 

		elif solicitante.groups.filter(name='Funcionario').exists():
			obj.grado_prioridad_solicitante = 7

		else:		 
			obj.grado_prioridad_solicitante = 999999

		obj.solicitante = solicitante

		super(MiReservaAdmin, self).save_model(request, obj, form, change)
