from django.conf.urls import patterns, include, url
from recursos.views import *


urlpatterns = [
    url(r'^tipoderecurso/$', TipoDeRecursoListView.as_view(), name='tipoderecurso_lis'),

    url(r'^recurso/(?P<pk>\d+)/detail/$', RecursoDetailView.as_view(), name='recurso_det'),
    url(r'^recurso/$', RecursoListView.as_view(), name='recurso_lis'),

    url(r'^$', recursos_presentacion),
]
