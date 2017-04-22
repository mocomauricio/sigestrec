# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group

rol = Group(name="Titular")
rol.save()

rol = Group(name="Adjunto")
rol.save()

rol = Group(name="Asistente")
rol.save()

rol = Group(name="Encargado de catedra")
rol.save()

rol = Group(name="Auxiliar de enseñanza")
rol.save()

rol = Group(name="Alumno")
rol.save()

rol = Group(name="Funcionario")
rol.save()

user=User.objects.create_user('admin', password='admin')
user.first_name = "Administrador"
user.is_superuser=True
user.is_staff=True
user.save()