#encoding:utf-8_
_author__ = 'admin'
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', 'backend.views.index_view'),
    url(r'^index_view', 'backend.views.index_view'),
	url(r'^logout', 'smi.views.logout'),
    url(r'^perfil', 'backend.views.perfil_view'),
    url(r'^geo/(?P<type>estados)/$', 'backend.views.geo', name='geo'),
    url(r'^geo/(?P<type>municipios|parroquias)/(?P<parent_id>[0-9]+)$',  'backend.views.geo', name='geo'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
