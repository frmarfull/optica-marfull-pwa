from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Perfil

class FormIniciarSesion(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(FormIniciarSesion,self).__init__(*args,**kwargs)
        # print(self.visible_fields())
        for campoVisible in self.visible_fields():
            campoVisible.field.widget.attrs['class'] = 'form-control'

class FormularioCreacion(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(FormularioCreacion,self).__init__(*args,**kwargs)
        # print(self.visible_fields())
        for campoVisible in self.visible_fields():
            campoVisible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')

class FormularioPerfil(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(FormularioPerfil,self).__init__(*args,**kwargs)
        # print(self.visible_fields())
        for campoVisible in self.visible_fields():
            campoVisible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Perfil
        fields = ('rut','region','comuna','calle','departamento')
    