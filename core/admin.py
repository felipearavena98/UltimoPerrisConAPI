from django.contrib import admin
from .models import Ciudad, Lista, Producto, Region, Tienda

admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Producto)
admin.site.register(Lista)
admin.site.register(Tienda)
