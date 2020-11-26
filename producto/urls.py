from django.urls import path

from .views import agregarProducto, listarProductos,eliminarProducto,editarProducto,catalogo,listadoCatalogo

urlpatterns = [
    path('agregar/',agregarProducto,name='AgregarProducto'),
    path('listar/',listarProductos,name="Listado productos"),
    path('eliminar/<int:id_producto>',eliminarProducto,name='Eliminar producto'),
    path('modificar/<int:id_producto>',editarProducto, name='modificar_producto'),
    path('listarCatalogo/',listadoCatalogo, name='catalogo')
]