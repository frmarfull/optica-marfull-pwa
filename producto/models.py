from django.db import models

# Create your models here.

class Producto(models.Model):
    nombreLente= models.CharField(max_length=50,blank=False)
    codLente= models.CharField(max_length=50,blank=False)
    precioLente= models.CharField(max_length=50,blank=False)
    imagenLente= models.ImageField(upload_to='img')