from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cedula = models.IntegerField()
    telefono = models.IntegerField()
    mail = models.EmailField()
    
    def __str__(self):
        return self.nombre

class Agenda(models.Model):
    fechas_disponibles = models.DateField()

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True, related_name='turnos_asignados')
    profesional = models.ForeignKey('Profesional', on_delete=models.SET_NULL, null=True) 
    servicio = models.ForeignKey('Servicio', on_delete=models.SET_NULL, null=True, related_name='turnos_asignados') 

class Cliente(Persona):
    turno_asignado = models.ForeignKey('Turno', on_delete=models.SET_NULL, null=True, related_name='cliente_asignado')
    def __str__(self):
        return self.nombre
    def ReservarTurno(self, turno):
        if not self.turno_asignado:
            if turno.cliente is None:
                self.turno_asignado = turno
                turno.cliente = self
                self.save()
                turno.save()

class Profesional(Persona):
    turnos_habilitados = models.ManyToManyField(Turno, related_name='profesionales_habilitados')
    dias_habilitados = models.ManyToManyField(Agenda) 

class Especialidad(models.Model):
    nombre = models.CharField(max_length=150)
    servicio = models.ForeignKey('Servicio', on_delete=models.SET_NULL, null=True)
    profesional = models.ForeignKey(Profesional, on_delete=models.SET_NULL, null=True) 
    
class Servicio(models.Model):
    nombre = models.CharField(max_length=150)
    profesional = models.ForeignKey(Profesional, on_delete=models.SET_NULL, null=True)
    turno = models.ForeignKey(Turno, on_delete=models.SET_NULL, null=True, related_name='servicio_asignado')
    
    def __str__(self):
        return self.nombre
