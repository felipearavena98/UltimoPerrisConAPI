from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^lista_producto/$',views.ListarProducto.as_view()),
    url(r'^crear_producto/$',views.CrearProducto.as_view()),
    url(r'^detalle_producto/(?P<pk>[0-9]+)/$',views.DetalleProducto.as_view()),
]
urlpatterns=format_suffix_patterns(urlpatterns)
