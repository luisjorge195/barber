from django.contrib import admin

from myapp.models import Persona
from myapp.models import Agenda
from myapp.models import Turno
from myapp.models import Cliente
from myapp.models import Profesional
from myapp.models import Especialidad
from myapp.models import Servicio

# Register your models here.
admin.site.register(Persona)
admin.site.register(Agenda)
admin.site.register(Turno)
admin.site.register(Cliente)
admin.site.register(Profesional)
admin.site.register(Especialidad)
admin.site.register(Servicio)