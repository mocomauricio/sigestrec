
"""
from django.test import TestCase
from django.test import TestCase
from recursos.models import Recurso

class RecursoTestCase(TestCase):
    def setUp(self):
        Recurso.objects.create(codigo=12334, nombre="proyector",tipo= "", observaciones="")
        Recurso.objects.create(codigo=12335, nombre="Aula", tipo="", observaciones="")
    def test_recurso(self):
        proyector = Recurso.objects.get(name="proyector")
        Aula= Recurso.objects.get(name="Aula")
"""
