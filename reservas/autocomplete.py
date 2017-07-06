from dal import autocomplete
from django.db.models import Q
from django.contrib.auth.models import User, Group
from recursos.models import *


class ReservaRecursoAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):

		tipo_recurso_id = self.forwarded.get('tipo_recurso', None)

		# Don't forget to filter out results depending on the visitor !
		if not self.request.user.is_authenticated() or tipo_recurso_id == None:
			return Recurso.objects.none()

		qs = Recurso.objects.filter(tipo_id=tipo_recurso_id).exclude(estado=2).exclude(borrado=True)


		if self.q:
			qs = qs.filter( Q(codigo__startswith=q) | Q(nombre__icontains=q) | Q(observaciones__icontains=q) )

		return qs

class ReservaRecursoGeneralAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):

		tipo_recurso_id = self.forwarded.get('tipo_recurso', None)

		# Don't forget to filter out results depending on the visitor !
		if not self.request.user.is_authenticated() or tipo_recurso_id == None:
			return Recurso.objects.none()

		qs = Recurso.objects.filter(tipo_id=tipo_recurso_id, estado=0).exclude(borrado=True)


		if self.q:
			qs = qs.filter( Q(codigo__startswith=q) | Q(nombre__icontains=q) | Q(observaciones__icontains=q) )

		return qs