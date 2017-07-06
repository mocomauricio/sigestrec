from django.conf.urls import patterns, include, url
from recursos.ajax import *
from recursos.autocomplete import *
from publico.views import *

from django.contrib.auth.decorators import permission_required

urlpatterns = [

    # Views

    #url(r'^recurso/(?P<pk>\d+)/detail/$', RecursoDetailView.as_view(), name='recurso_det'),
    url(r'^recurso/$', RecursoPublicoListView.as_view(), name='recurso_lis'),



]
