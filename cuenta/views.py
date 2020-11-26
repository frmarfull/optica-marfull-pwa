from django.shortcuts import render, redirect
from .forms import FormularioCreacion, FormularioPerfil,FormIniciarSesion
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'cuenta/home.html')
    
    # Create your views here.
def mostarFormularioRegistro(request):
    formulario1 = FormularioCreacion()
    formulario2 = FormularioPerfil()
    context = {
        'formulario1':formulario1,
        'formulario2':formulario2
    }
    return render(
        request,
        'registrar.html',
        context
    )

def registroUsuario(request):
    if request.method == 'POST':
        formulario1 = FormularioCreacion(request.POST)
        formulario2 = FormularioPerfil(request.POST)
        if formulario1.is_valid() and formulario2.is_valid():
            usuarioGuardado = formulario1.save()
            perfilGuardado = formulario2.save(commit=False)
            perfilGuardado.usuario = usuarioGuardado
            perfilGuardado.save()
            print(perfilGuardado)
            messages.add_message(request,
                messages.SUCCESS,
                'Usuario registrado con éxito :D'
            )
            return redirect('/')
        context = {
        'formulario1':formulario1,
        'formulario2':formulario2
        }
        return render(
            request,
            'registrar.html',
            context
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            'No puedes estar aquí'
        )
        return redirect('/registro/')

def iniciarSesion(request):
    formulario = FormIniciarSesion()
    if request.method == 'POST':
        formulario = FormIniciarSesion(data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            usuarioLogeado = authenticate(username=username,password=password)
            if usuarioLogeado is not None:
                login(request,usuarioLogeado)
                if usuarioLogeado.is_superuser:
                    pass
                    #Redireccion a pagina admin
                else:
                    pass
                    #Redireccion a pagina normal
                return redirect('/')
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    'Usuario o contraseña son incorrectos'
                )
    context = {
        'formulario':formulario
    }
    return render(
        request,
        'iniciar_sesion.html',
        context)
   
def agregar(request):
    return render(request,'agregar.html')

def cancelar(request):
    return render(request,'cancelar.html')
    
    
def consultar(request):
    return render(request,'consultar.html')
                                                                                                                                                    
def listar_producto(request):
    return render(request,'listar_producto.html')
                                                                                                                                                        
def modificar_producto(request):
    return render(request,'modificar_producto.html')
                                                                                                                                                        



def salir(request):
    logout(request)
    return redirect('/iniciarSesion/')

