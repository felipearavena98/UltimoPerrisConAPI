from django.urls import path
from .views import  cambiarEstado,charcha_serviceworker,manifest, base_layout, ListarProducto, index, eliminarProducto, actualizarProducto, formularioProducto, formularioLista, listarLista, eliminarLista, actualizarLista, listarProductoFiltro
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', index, name="home"),
    path('listaproductoapi',ListarProducto,name='listpro'),
    path('listarproductofiltro', listarProductoFiltro, name='prodfiltro'),
    path('eliminarproducto', eliminarProducto, name='eliminarproducto'),
    path('modificarproducto', actualizarProducto, name='modificarproducto'),
    path('formularioproducto', formularioProducto, name='formprod'),
    path('formulariolista', formularioLista, name='formlist'),
    path('listarlistas', listarLista, name='listlis'),
    path('eliminarlista', eliminarLista, name='eliminarlista'),
    path('modificarlista',actualizarLista, name='modificarlista'),
    path('cambiarEstado',cambiarEstado, name='cambiarEstado'),

    path('listatienda', views.TiendaListView.as_view(), name='tienda_changelist'),
    path('agregartienda/', views.TiendaCreateView.as_view(), name='tienda_add'),
    path('<int:pk>/', views.TiendaUpdateView.as_view(), name='tienda_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- this one here

    path(r'base_layout', base_layout, name='base_layout'),
    url(r'^serviceworker(.*.js)$', charcha_serviceworker, name='serviceworker'),
    url('^manifest.json$', manifest),
]