# -*- coding: utf-8 -*-


import unittest
from django.contrib.auth import SESSION_KEY
from django.test import Client
from django.test import TestCase
from django.contrib.auth.models import User
class GTGTestCase(TestCase):

	def test_crear_usuario(self):
		'''
		Test para la creacion de un usuario con contrasenha
		'''
		print('\n------Ejecutando test para crear usuario-------\n')

		u = User.objects.create_user('testuser', 'test1', 'test1')
		self.assertTrue(u.has_usable_password())
		self.assertFalse(u.check_password('bad'))
		self.assertTrue(u.check_password('test1'))
		print('\n------Test para crear usuario correcto-------\n')

		print('\n------Ejecutando test para contraseña incorrecta-------\n')
		# Test para contrasenha incorrecta
		u.set_unusable_password()
		u.save()
		self.assertFalse(u.check_password('test1'))
		self.assertFalse(u.has_usable_password())
		u.set_password('test1')
		self.assertTrue(u.check_password('test1'))
		u.set_password(None)
		self.assertFalse(u.has_usable_password())
		print('\n------Test para crear contraseña incorrecta correcto-------\n')

		print('\n------Ejecutando test para identificar permiso-------\n')
		# Test para identificar permisos
		self.assertTrue(u.is_authenticated())
		self.assertFalse(u.is_staff)
		self.assertTrue(u.is_active)
		self.assertFalse(u.is_superuser)
		print('\n------Test para identificar permiso correcto-------\n')

	def test_eliminar_usuario(self):
		'''
		Test para la eliminacion de un usuario
		'''
		print('\n------Ejecutando test para eliminar usuario-------\n')
		u = User.objects.create_user('test1', 'test1', 'test1')
		a = User.objects.get(pk=u.id)
		self.assertNumQueries(6, a.delete)
		self.assertFalse(User.objects.exists())
		print('\n------Test para eliminar usuario correcto-------\n')

		# Test para creacion sin password
		u2 = User.objects.create_user('testuser2')
		self.assertFalse(u2.has_usable_password())

