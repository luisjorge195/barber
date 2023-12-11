Este repositorio contiene una aplicación de una peluqueria o barberia(en este caso la llamo barberia) construida con Django REST Framework. La aplicación incluye modelos definidos, implementación de pruebas y un conjunto básico de rutas para reservar turnos.

Antes de ejecutar la aplicación, asegúrate de tener instalados los siguientes paquetes:

Django (pip install django)
Django REST Framework (pip install djangorestframework)
Django CORS Headers (pip install django-cors-headers) --esto se hizo para hacer una prueba adicional pero no está ligada 
Además, se recomienda crear y activar un entorno virtual para encapsular las dependencias del proyecto asi:
python -m venv env          # Crear entorno virtual
env\Scripts\activate        # Activar entorno virtual (Windows)
source env/bin/activate      # Activar entorno virtual (Linux/Mac)
Antes de iniciar el servidor, realiza las migraciones para crear las tablas en la base de datos: python manage.py migrate
incia el servidor python manage.py runserver


