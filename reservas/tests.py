# -*- coding: utf-8 -*-


from django.test import TestCase

# Create your tests here.

from reservas.models import *
from recursos.models import *
from django.contrib.auth.models import User, Group

class ReservaTestCase(TestCase):
	def setUp(self):
		print('\n------Test para corroborar el adjudicado a un recurso en una lista-------\n')

		print('\n------Creando una reserva con empates-------\n')

		rol = Group.objects.create(name="Titular")

		rol = Group.objects.create(name="Adjunto")

		rol = Group.objects.create(name="Asistente")

		rol = Group.objects.create(name="Encargado de catedra")

		rol = Group.objects.create(name="Auxiliar de enseñanza")

		rol = Group.objects.create(name="Alumno")

		rol = Group.objects.create(name="Funcionario")

		rol = Group.objects.create(name="Encargado de recursos")


		encargado = User.objects.create(id=1,username="cgonzalez", first_name="Carlos Gonzalez")

		solicitante1 = User.objects.create(id=2, username="gotazu", first_name="Gustavo Otazu")
		solicitante2 = User.objects.create(id=3, username="ramarilla", first_name="Rodrigo Amarilla")
		solicitante3 = User.objects.create(id=4, username="mdominguez", first_name="Mauricio Domiguez")

		rol = Group.objects.get(name='Alumno') 
		rol.user_set.add(solicitante1)

		rol = Group.objects.get(name='Titular') 
		rol.user_set.add(solicitante2)
		rol.user_set.add(solicitante3)

		tipo_recurso = TipoDeRecurso.objects.create(nombre = "Aula", encargado=encargado)
		recurso = Recurso.objects.create(codigo="001", nombre="F32", tipo=tipo_recurso)

		reserva1 = Reserva.objects.create(
			id=1,
			tipo_recurso=tipo_recurso, 
			recurso=recurso, 
			solicitante=solicitante1, 
			hora_inicio=time(7,0,0), hora_fin=time(9,0,0), 
			grado_prioridad_solicitante=6
		)
		
		reserva2 = Reserva.objects.create(
			id=2,
			tipo_recurso=tipo_recurso, 
			recurso=recurso, 
			solicitante=solicitante2, 
			hora_inicio=time(7,0,0), hora_fin=time(9,0,0), 
			grado_prioridad_solicitante=1
		)

		reserva2 = Reserva.objects.create(
			id=3,
			tipo_recurso=tipo_recurso, 
			recurso=recurso, 
			solicitante=solicitante3, 
			hora_inicio=time(7,0,0), hora_fin=time(9,0,0), 
			grado_prioridad_solicitante=1
		)


	def test_adjudicado(self):
		print('\n------Test para corroborar el solicitante adjudicado finalizado -------\n')

		recurso = Recurso.objects.get(codigo="001")
		solicitante = User.objects.get(username="ramarilla")
		self.assertEqual(recurso.get_adjudicado(), solicitante)

		solicitante = User.objects.get(username="gotazu")
		self.assertNotEqual(recurso.get_adjudicado(), solicitante)

		solicitante = User.objects.get(username="mdominguez")
		self.assertNotEqual(recurso.get_adjudicado(), solicitante)	



