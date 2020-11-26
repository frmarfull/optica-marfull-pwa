from django.shortcuts import render, redirect
from .forms import FormProducto
from django.contrib import messages
from .models import Producto
from django.contrib.auth.decorators import login_required
from cuenta.models import User

# Create your views here.
@login_required(login_url='/iniciarSesion/')
def listarProductos(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
        context = {
            'titulo':'Listar productos',
            'productos':productos
        }
        return render(
            request,
            'listar_producto.html',
            context
        )
    else:
        return redirect(
            '/'
        )

def listadoCatalogo(request):
    productos = Producto.objects.all()
    context = {
        'titulo':'Catalogo',
        'productos':productos
    }
    for producto in productos:
        print(producto.codLente)
    return render(
        request,
        'catalogo.html',
        context
    )


@login_required(login_url='/iniciarSesion/')
def agregarProducto(request):
    if request.user.is_superuser:
        formulario= FormProducto()
        if request.method =='POST':
            formulario = FormProducto(request.POST,request.FILES)
            if formulario.is_valid():
                productoNuevo= formulario.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'producto agregado'
                )
                return redirect('/productos/listar')
        context = {
            'formulario':formulario
        }
        return render(
            request,
            'agregar.html',
            context
        )
    else:
        return redirect(
            '/'
        )
@login_required(login_url='/iniciarSesion/')
def eliminarProducto(request, id_producto):
    if request.user.is_superuser:
        productoEncontrado = Producto.objects.get(pk=id_producto)
        productoEncontrado.delete()

        return redirect('/productos/listar/')
    else:
        return redirect(
            '/'
        )

def editarProducto(request,id_producto):
    if request.user.is_superuser:
        productoEncontrado = Producto.objects.get(pk = id_producto)
        formulario = None

        if request.method == 'POST':
            formulario = FormProducto(request.POST,request.FILES, instance= productoEncontrado)
            if formulario.is_valid():
                formulario.save()
                return redirect('/productos/listar')
        else:
            formulario = FormProducto(instance= productoEncontrado)
        context = {
            'titulo':'Modificar producto',
            'formulario':formulario
        }

        return render(
            request,
            'modificar_producto.html',
            context
        )
    else:
         return redirect(
            '/'
        )

def catalogo(request):
    return render(request,'catalogo.html')