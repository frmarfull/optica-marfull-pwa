from django.shortcuts import render,redirect
from .forms import FormPedido
from .models import Pedido, Perfil,User
from django.contrib.auth.decorators import login_required
from producto.models import Producto
from django.contrib import messages
# Create your views here.

@login_required(login_url='iniciarSesion')
def listarPedidos(request):
    if request.user.is_superuser:    
        return redirect(
            '/'
        )
    else:    
        pedidos= Pedido.objects.all().filter(perfil=(request.user.id)-1)
        print(request.user.id)
        context = {
            'titulo':'Listar pedidos',
            'pedidos':pedidos
        }
        
        return render(
            request,
            'consultar.html',
            context
        )
@login_required(login_url='iniciarSesion')
def agregarPedidos(request,id_producto):
    if request.user.is_superuser:    
        return redirect(
            '/'
        )
    else:
        print(id_producto)
        elproducto= Producto.objects.get(pk=id_producto)
        elusuario = User.objects.get(pk=request.user.id)
        elperfil = Perfil.objects.get(usuario=elusuario)
        Pedido.objects.create(producto=elproducto,perfil=elperfil)
        
        # pedido.save()
        return redirect(
            '/pedidos/pedidos/'
        )

@login_required(login_url='iniciarSesion')
def eliminarPedido(request, id_pedido):
    if request.user.is_superuser:
        return redirect(
            '/'
        )
    else:
        pedidoEncontrado = Pedido.objects.get(pk=id_pedido)
        pedidoEncontrado.delete()

        return redirect('/pedidos/pedidos')
    

            



