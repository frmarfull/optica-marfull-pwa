# Óptica Marfull 3.0
[![GitHub version](https://img.shields.io/badge/version-0.1-red.svg)](https://github.com/frmarfull/optica-marfull-with-django)
[![GitHub version](https://img.shields.io/badge/Django-3.1-green.svg)](https://github.com/frmarfull/optica-marfull-with-django)
[![GitHub version](https://img.shields.io/badge/Python-3.7-blue.svg)](https://github.com/frmarfull/optica-marfull-with-django)

Sistema de gestión de cuentas e inventario de una óptica usando Django.
------------
### Características

- Página web progresiva, interactiva, intuitiva y amigable.
- Gestiona la venta de los productos.
- Utiliza el Framework Django.
- Utiliza MySQL para la base de datos.
- Incorpora una API de conversión de divisas.
- Permite autenticación con cuenta de Google.
- Disponible sin conexión (después del primer uso con internet).
- Utiliza Materialize para el diseño y retoques.
------------
### Instalación.
Cómo arrancar el servidor y acceder al sitio web.
                
1. Instalar `git` & `python3` en su sistema operativo.
2. Clonar el repositorio y configurar el entorno.
```
git clone https://github.com/frmarfull/optica-marfull-pwa.git		# clonar el proyecto.
cd optica				            # ir a la ruta del proyecto.
python manage.py makemigrations		# Crear archivos de las migraciones de la base de datos.
python manage.py migrate		    # Crear las tablas de la base de datos.
python manage.py createsuperuser 	# Esto es para crear un usuario admin que maneja inventario
python manage.py runserver		    # Arrancar un servidor local del proyecto.
```
3. En un navegador (Google Chrome, Mozilla Firefox, Opera, Edge, etc), ir a `http://127.0.0.1:8000/` para acceder al proyecto. (también es posible ingresando )

### Capturas de pantalla.
Vistas del sitio desde un computador de escritotio.
![](https://github.com/frmarfull/optica-marfull-pwa/blob/master/Capturas%20de%20pantalla/opt-home.png)
> Index Page Desktop pt1

![](https://github.com/frmarfull/optica-marfull-pwa/blob/master/Capturas%20de%20pantalla/opt-home-desc.png)
> Index Page Desktop pt2

------------
### Recomendaciones para echar un vistazo a los tipos de usuario
Esto es sólo a modo de ejemplo, se recomienda NUNCA usar estas credenciales para uso real de la aplicación.

| Nombre de usuario | Tipo | Contraseña |
| :---         |     :---:      |          ---: |
| *admin*   | administrador     | admin    |
| user     | usuario regular       | 123456_7      |
                
------------
### Lista de tareas terminadas y por terminar.

- [x] Realizar el primer commit.
- [x] Documentar los pasos para configurar el entorno.
- [x] Añadir capturas de pantalla al archivo 'README.md'
- [x] Permitir autenticación, verificación y autorización con Google.
- [x] Añadir manifest al proyecto.
- [x] Añadir service worker.
- [x] PWA usando Django.
