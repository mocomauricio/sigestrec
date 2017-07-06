from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import permission_required

from sistema.views import *
from sistema.autocomplete import *
from sistema.ajax import *

urlpatterns = [

	url(r'^usuarioautocomplete/$', 
		UsuarioAutocomplete.as_view(), 
		name='usuario-autocomplete'
	),

    url(r'^user/$', UsuarioListView.as_view(), name='usuario_list'),
    url(r'^user/add/$', permission_required('auth.user_add')(UsuarioCreateView.as_view()), name='usuario_add'),
    url(r'^user/(?P<pk>\d+)/delete/$', permission_required('auth.user_delete')(anular_usuario), name='usuario_delete'),

    url(r'^group/$', GrupoListView.as_view(), name='grupo_list'),


	url(r'^$', sistema_presentacion),

]

