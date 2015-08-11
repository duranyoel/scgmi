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


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
