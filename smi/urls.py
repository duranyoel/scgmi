#encoding:utf-8_
from django.conf.urls import  url
from smi.views import index_view,ingresar_view,logout,registrarse,gracias_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index_view),

    url(r'^login', ingresar_view),
    url(r'^logout', logout),
    url(r'^registrarse', registrarse),
    url(r'^gracias', gracias_view),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)