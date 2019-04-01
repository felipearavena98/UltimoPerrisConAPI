from django.shortcuts import render
from .serializers import ProductoSerializer
from core.models import Producto, Lista
from rest_framework import generics

# Create your views here.
class DetalleProducto(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ListarProducto(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CrearProducto(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer