from django.db import models
from cuenta.models import Perfil
from producto.models import Producto
from django.contrib.auth.models import User
# Create your models here.


class Pedido(models.Model):
    
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    perfil= models.ForeignKey(Perfil,on_delete=models.CASCADE)


