from django.conf.urls import patterns, include, url

from mantenimientos.views import *

from django.contrib.auth.decorators import permission_required

urlpatterns = [

	# Views
	url(r'^mantenimiento/$', MantenimientoListView.as_view(), name='mantenimiento_lis'),

	url(r'^mantenimiento/(?P<pk>\d+)/aprobar_correctivo/$', permission_required('mantenimientos.delete_mantenimiento')(aprobar_mantenimiento_correctivo), name='aprobar_mantenimiento_correctivo'),
	#url(r'^mantenimiento/(?P<pk>\d+)/aprobar_preventivo/$', permission_required('mantenimientos.delete_mantenimiento')(aprobar_mantenimiento_preventivo), name='aprobar_mantenimiento_preventivo'),

	url(r'^$', mantenimientos_presentacion),

]




