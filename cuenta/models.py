from django.db import models
from django.contrib.auth.models import User

# Create your models here.    


class Perfil(models.Model):
    region= models.CharField(max_length=50,default="")
    comuna= models.CharField(max_length=50,default="")
    calle= models.CharField(max_length=50,default="")
    departamento= models.CharField(max_length=20,default="")
    rut= models.CharField(max_length=12)
    usuario= models.OneToOneField(User, on_delete=models.CASCADE)