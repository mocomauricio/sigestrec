from dal import autocomplete
from django.db.models import Q
from django.contrib.auth.models import User, Group
from recursos.models import *


class CaracteristicaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Caracteristica.objects.none()

        qs = Caracteristica.objects.all()
        
        if self.q:
            qs = qs.filter( descripcion__istartswith=self.q )

        return qs




class EncargadoDeRecursoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return User.objects.none()

        #qs = User.objects.all()
        qs = User.objects.filter(groups__name='Encargado de recursos')

        if self.q:
            qs = qs.filter( Q(first_name__istartswith=self.q) | Q(last_name__istartswith=self.q) | Q(username__istartswith=self.q) )

        return qs


class RecursoAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Recurso.objects.none()

        qs = Recurso.objects.exclude(estado=2).exclude(borrado=True)

        if self.q:
            qs = qs.filter( Q(codigo__startswith=q) | Q(nombre__icontains=q) | Q(observaciones__icontains=q) )

        return qs