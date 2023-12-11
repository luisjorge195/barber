from django.test import TestCase
from django.utils import timezone
from .models import Persona, Agenda, Turno, Cliente, Profesional, Especialidad, Servicio





class TurnoTestCase(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Cliente1", apellido="Apellido1",cedula=12345678, telefono=123456789, mail="cliente1@example.com")
        self.profesional = Profesional.objects.create(nombre="Profesional1", apellido="Apellido2", cedula=87654321, telefono=987654321, mail="profesional1@example.com")
        self.agenda = Agenda.objects.create(fechas_disponibles=timezone.now().date())
        self.turno = Turno.objects.create(fecha=timezone.now().date(), hora=timezone.now().time(), cliente=self.cliente, profesional=self.profesional)

    def test_cliente_reserva_turno(self):
        cliente2 = Cliente.objects.create(nombre="Cliente2", apellido="Apellido3", cedula=11223344, telefono=987654321, mail="cliente2@example.com")
        turno_no_asignado = Turno.objects.create(fecha=timezone.now().date(), hora=timezone.now().time(), cliente=None, profesional=self.profesional)

        cliente2.ReservarTurno(turno_no_asignado)

        self.assertEqual(cliente2.turno_asignado, turno_no_asignado)
        self.assertEqual(turno_no_asignado.cliente, cliente2)

    def test_profesional_habilita_turno(self):
        turno_habilitado = Turno.objects.create(fecha=timezone.now().date(), hora=timezone.now().time(), cliente=None, profesional=None)
        self.profesional.turnos_habilitados.add(turno_habilitado)

        self.assertIn(turno_habilitado, self.profesional.turnos_habilitados.all())
