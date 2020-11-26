from django.urls import path

from .views import * 


urlpatterns=[
    path('pedidos/',listarPedidos, name="pedidos"),
    path('agregarPedidos/<int:id_producto>/',agregarPedidos, name="agregarPedidos"),
    path('eliminarPedido/<int:id_pedido>',eliminarPedido,name ="EliminarPedidos")

]