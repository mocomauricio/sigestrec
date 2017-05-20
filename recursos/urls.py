from django.conf.urls import patterns, include, url
from recursos.ajax import *
from recursos.autocomplete import *
from recursos.views import *

from django.contrib.auth.decorators import permission_required

urlpatterns = [
	# Autocomplete
    url(
        'caracteristicaautocomplete/$',
       CaracteristicaAutocomplete.as_view(),
        name='caracteristica-autocomplete',
    ),

    url(
        'encargadoderecursoautocomplete/$',
        EncargadoDeRecursoAutocomplete.as_view(),
        name='encargadoderecurso-autocomplete',
    ),

    # Ajax
    url('get_caracteristicas_tipo_de_recurso/$', get_caracteristicas_tipo_de_recurso),

    # Views
    url(r'^tipoderecurso/$', TipoDeRecursoListView.as_view(), name='tipoderecurso_lis'),

    url(r'^recurso/(?P<pk>\d+)/detail/$', RecursoDetailView.as_view(), name='recurso_det'),
    url(r'^recurso/$', RecursoListView.as_view(), name='recurso_lis'),

    url(r'^recurso/(?P<pk>\d+)/averiar/$', permission_required('recursos.averiar_recurso')(marcar_como_averiado), name='recurso_averiado'),
    url(r'^recurso/(?P<pk>\d+)/reparar/$', permission_required('recursos.reparar_recurso')(marcar_como_reparado), name='recurso_reparado'),

    url(r'^$', recursos_presentacion),

]
