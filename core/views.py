from django.shortcuts import render
from .models import Ciudad, Lista, Producto, Region, Tienda
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
import json
import requests
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import TiendaForm
from django.db.models import Sum
from django.db.models import Count
from django.db.models import Q
##


def index(request):
    template = 'core/home.html'
    return render(request, template)

# Consumo API listar Producto


def ListarProducto(request):
    resp = requests.get("http://127.0.0.1:8000/api/lista_producto/")
    lista = resp.json()
    return render(request, 'core/listaproductoapi.html', {'lista': lista})

# CRUD PRODUCTO


def formularioProducto(request):
    ti = Tienda.objects.all()
    li = Lista.objects.all()
    resp = False
    if request.POST:
        idp = request.POST.get('idProducto')
        no = request.POST.get('nombre')
        cost = request.POST.get('costoPresupuesto')
        costr = request.POST.get('costoReal')
        nos = request.POST.get('notas')
        est = request.POST.get('estado')
        idt = request.POST.get('idTienda')
        idl = request.POST.get('idLista')
        obj_tienda = Tienda.objects.get(idTienda=idt)
        obj_lista = Lista.objects.get(idLista=idl)
        pr = Producto(
            idProducto=idp,
            nombre=no,
            costoPresupuesto=cost,
            costoReal=costr,
            notas=nos,
            estado=est,
            idTienda=obj_tienda,
            idLista=obj_lista
        )
        pr.save()
        resp = True
    return render(request, 'core/formularioproducto.html', {'respuesta': resp, 'tienda': ti, 'lista': li})


def actualizarProducto(request):
    pr = Producto.objects.all()
    mensaje = False
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Modificar":
            idp = request.POST.get('idProducto')
            prod = Producto.objects.get(idProducto=idp)
            mensaje = False
            return render(request, 'core/actualizarproducto.html', {'productos': pr, 'prod': prod, 'mensaje': mensaje})
        if accion == "Editar":
            idp = request.POST.get('idProducto')
            prod = Producto.objects.get(idProducto=idp)
            no = request.POST.get('nombre')
            cost = request.POST.get('costoPresupuesto')
            costr = request.POST.get('costoReal')
            nos = request.POST.get('notas')
            est = request.POST.get('estado')
            prod.nombre = no
            prod.costoPresupuesto = cost
            prod.costoReal = costr
            prod.notas = nos
            prod.estado = est
            prod.save()
            mensaje = True
            return render(request, 'core/actualizarproducto.html', {'productos': pr, 'mensaje': mensaje})
    return render(request, 'core/actualizarproducto.html', {'productos': pr})


def cambiarEstado(request):
    pr = Producto.objects.all()
    mensaje = False
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Cambiar estado":
            idp = request.POST.get('idProducto')
            prod = Producto.objects.get(idProducto=idp)
            if prod.estado == "Pendiente":
                prod.estado = "Comprado"
                prod.save()
                resp = requests.get("http://127.0.0.1:8000/api/lista_producto/")
                lista = resp.json()
                return render(request, 'core/listaproductoapi.html', {'lista': lista})
            if prod.estado == "Comprado":
                prod.estado = "Pendiente"
                prod.save()
                resp = requests.get("http://127.0.0.1:8000/api/lista_producto/")
                lista = resp.json()
                return render(request, 'core/listaproductoapi.html', {'lista': lista})
    return render(request, 'core/listaproductoapi.html', {'lista': lista})


def listarProductoFiltro(request):
    idl = request.POST.get('idLista')
    prod = Producto.objects.filter(idLista=idl)
    return render(request, 'core/listarproductofiltro.html', {'productos': prod})


def eliminarProducto(request):
    lista = Producto.objects.all()
    resp = False
    if request.POST:
        idp = request.POST.get('idProducto')
        pro = Producto.objects.get(idProducto=idp)
        pro.delete()
        resp = True
        return render(request, 'core/listaproducto.html', {'lista': lista, 'respuesta': resp})
    return render(request, 'core/listaproducto.html', {'lista': lista, 'respuesta': resp})


##############################################################################################################

# CRUD LISTA

def formularioLista(request):
    resp = False
    if request.POST:
        idl = request.POST.get('idLista')
        no = request.POST.get('nombre')
        cor = request.POST.get('correo')
        li = Lista(
            idLista=idl,
            nombre=no,
            correo=cor
        )
        li.save()
        resp = True
    return render(request, 'core/formulariolista.html', {'respuesta': resp})


def actualizarLista(request):
    li = Lista.objects.all()
    mensaje = False
    if request.POST:
        accion = request.POST.get("btnAccion", "")
        if accion == "Modificar":
            idl = request.POST.get('idLista')
            lista = Lista.objects.get(idLista=idl)
            mensaje = False
            return render(request, 'core/actualizarlistas.html', {'listas': li, 'lista': lista, 'mensaje': mensaje})
        if accion == "Editar":
            idl = request.POST.get('idLista')
            lista = Lista.objects.get(idLista=idl)
            no = request.POST.get('nombre')
            lista.nombre = no
            lista.save()
            mensaje = True
            return render(request, 'core/actualizarlistas.html', {'listas': li, 'mensaje': mensaje})
    return render(request, 'core/actualizarlistas.html', {'listas': li})


def listarLista(request):
    lista = Lista.objects.all()
    total_pre = Lista.objects.annotate(sum_prod=Sum('producto__costoPresupuesto'))
    total_rea = Lista.objects.annotate(sum_prod=Sum('producto__costoReal'))
    pubs = Lista.objects.annotate(num_prod=Count('producto'))
    compr = Lista.objects.annotate(comprados=Count('producto', filter=Q(producto__estado='Comprado')))
    return render(request, 'core/listarlistas.html', {'lista': lista, 'total_pre': total_pre, 'total_rea': total_rea, 'pubs': pubs, 'compr':compr})


def eliminarLista(request):
    lista = Lista.objects.all()
    resp = False
    if request.POST:
        idl = request.POST.get('idLista')
        li = Lista.objects.get(idLista=idl)
        li.delete()
        resp = True
        return render(request, 'core/listarlistas.html', {'lista': lista, 'respuesta': resp})
    return render(request, 'core/listarlistas.html', {'lista': lista, 'respuesta': resp})

##############################################################################################################

# CRUD TIENDA


class TiendaListView(ListView):
    model = Tienda
    content_object_name = 'tiendas'


class TiendaCreateView(CreateView):
    model = Tienda
    form_class = TiendaForm
    success_url = reverse_lazy('tienda_changelist')


class TiendaUpdateView(UpdateView):
    model = Tienda
    form_class = TiendaForm
    success_url = reverse_lazy('tienda_changelist')


def load_cities(request):
    idreg = request.GET.get('idRegion')
    ciudades = Ciudad.objects.filter(idRegion=idreg).order_by('descripcion')
    return render(request, 'core/city_dropdown_list_options.html', {'ciudades': ciudades})

##############################################################################################################


def base_layout(request):
    template = 'core/base.html'
    return render(request, template)


def manifest(request):
    return render(request, 'core/manifest.json')


def charcha_serviceworker(request, js):
    template = get_template('serviceworker.js')
    html = template.render()
    return HttpResponse(html, content_type="application/x-javascript")
