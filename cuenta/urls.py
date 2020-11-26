from django.urls import path
#from .views import home, mostarFormularioRegistro,registroUsuario,iniciarSesion,agregar
from .views import * 
urlpatterns = [
    path('', home, name='home'),                        
    path('registro/',mostarFormularioRegistro,name='Registrar'),
    path('crearUsuario/',registroUsuario, name="crear"),
    path('iniciarSesion/',iniciarSesion, name="iniciar"),
    path('salir/',salir,name="Salir")
    #path('/',, name=""), ejemplo #
   
    

]
