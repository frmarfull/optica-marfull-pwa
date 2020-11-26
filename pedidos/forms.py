from django import forms
from .models import Perfil
from .models import Producto
from .models import Pedido

class FormPedido(forms.ModelForm):
    class Meta:
        model= Pedido
        fields = [
            'producto',
            'perfil'
        ]
