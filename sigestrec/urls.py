from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'sigestrec.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/recursos/', include('recursos.urls')),
    url(r'^admin/mantenimientos/', include('mantenimientos.urls')),
    url(r'^admin/auth/', include('sistema.urls')),
    url(r'^admin/sistema/', include('sistema.urls')),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
