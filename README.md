# Óptica Marfull 2.0
[![GitHub version](https://img.shields.io/badge/version-0.1-red.svg)](https://github.com/frmarfull/optica-marfull-with-django)
[![GitHub version](https://img.shields.io/badge/Django-3.1-green.svg)](https://github.com/frmarfull/optica-marfull-with-django)
[![GitHub version](https://img.shields.io/badge/Python-3.7-blue.svg)](https://github.com/frmarfull/optica-marfull-with-django)

Sistema de gestión de cuentas e inventario de una óptica usando Django.
------------
### Características

- Página principal interactiva, intuitiva y amigable.
- Gestiona la venta de los productos.
- Utiliza el Framework Django
- Utiliza MySQL para la base de datos.

------------
### Instalación.
Cómo arrancar el servidor y acceder al sitio web.
                
1. Instalar `git` & `python3` en su sistema operativo.
2. Clonar el repositorio y configurar el entorno.
```
git clone https://github.com/frmarfull/optica-marfull-with-django.git		# clonar el proyecto.
cd optica		# ir a la ruta del proyecto.
python manage.py makemigrations		# Crear archivos de las migraciones de la base de datos.
python manage.py migrate		# Crear las tablas de la base de datos.
python manage.py createsuperuser # Esto es para crear un usuario admin que maneja inventario
python manage.py runserver		# Arrancar el proyecto.
```
3. En un navegador (Google Chrome, Mozilla Firefox, Opera, Edge, etc), ir a `http://127.0.0.1:8000/` para acceder al proyecto.



------------
### Recomendaciones para echar un vistazo a los tipos de usuario
Esto es sólo a modo de ejemplo, se recomienda jamás usar estas credenciales para uso real de la aplicación.

| Nombre de usuario | Tipo | Contraseña |
| :---         |     :---:      |          ---: |
| *admin*   | administrador     | 12345678z    |
| user     | usuario regular       | 12345678z      |
                
------------
### Lista de tareas terminadas y por terminar.

- [x] Realizar el primer commit.
- [x] Documentar los pasos para configurar el entorno.
- [ ] Añadir capturas de pantalla al archivo 'README.md'
- [x] Crear los módulos de autenticación, verificación y autorización.
- [x] Añadir las aplicaciones al proyecto.
- [x] Adaptar la SWA (Single Web Aplication) y optimizar el código usando Django.
- [x] App de Cuentas completa
- [x] App de Productos completa
- [x] App de Pedidos completa

