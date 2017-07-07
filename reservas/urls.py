from django.conf.urls import patterns, include, url
from reservas.autocomplete import *
from reservas.views import *
from reservas.reports import *

from django.contrib.auth.decorators import permission_required

urlpatterns = [
	# Autocomplete


    url(
        r'^reservarecursoautocomplete/$',
        ReservaRecursoAutocomplete.as_view(),
        name='reservarecurso-autocomplete',
    ),


    url(
        r'^reservarecursogeneralautocomplete/$',
        ReservaRecursoGeneralAutocomplete.as_view(),
        name='reservarecursogeneral-autocomplete',
    ),

    # Views
    url(r'^reserva/$', ReservaListView.as_view(), name='reserva_lis'),
    url(r'^mireserva/$', MiReservaListView.as_view(), name='mireserva_lis'),
    url(r'^mireserva/(?P<pk>\d+)/cancelar/$', permission_required('reservas.cancelar_reserva')(cancelar_mireserva), name='cancelar_mireserva'),

    url(r'^reserva/(?P<pk>\d+)/entregargeneral/$', permission_required('reservas.entregar_recurso')(EntregarRecursoGeneralUpdateView.as_view()), name='entregar_recurso_general'),
    url(r'^reserva/(?P<pk>\d+)/entregarespecifico/$', permission_required('reservas.entregar_recurso')(entregar_recurso_especifico), name='entregar_recurso_especifico'),
    url(r'^reserva/(?P<pk>\d+)/entregar/$', permission_required('reservas.entregar_recurso')(entregar_recurso), name='entregar_recurso'),
    url(r'^reserva/(?P<pk>\d+)/recibir/$', permission_required('reservas.recibir_recurso')(recibir_recurso), name='recibir_recurso'),
    url(r'^reserva/(?P<pk>\d+)/cancelar/$', permission_required('reservas.cancelar_reserva')(cancelar_reserva), name='cancelar_reserva'),
    url(r'^reserva/(?P<pk>\d+)/delete/$', permission_required('reservas.cancelar_reserva')(cancelar_reserva), name='cancelar_reserva'),

    url(r'^reserva/(?P<pk>\d+)/print_entrega/$', permission_required('reservas.imprimir_comprobante')(reporte_entrega_recurso), name='reporte_entrega_recurso'),
    url(r'^reserva/(?P<pk>\d+)/print_devolucion/$', permission_required('reservas.imprimir_comprobante')(reporte_devolucion_recurso), name='reporte_devolucion_recurso'),

    url(r'^$', reservas_presentacion),

]
