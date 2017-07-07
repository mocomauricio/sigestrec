from django.conf.urls import patterns, include, url
from recursos.ajax import *
from recursos.autocomplete import *
from publico.views import *

from django.contrib.auth.decorators import permission_required

urlpatterns = [

    # Views

    url(r'^recurso/(?P<pk>\d+)/detail/$', RecursoPublicoDetailView.as_view(), name='recurso_det'),
    url(r'^recurso/$', RecursoPublicoListView.as_view(), name='recurso_publico_lis'),
    url(r'^reserva/$', ReservaPublicoListView.as_view(), name='reserva_publico_lis'),

    url(r'^$', publico_presentacion),


]
