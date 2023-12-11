from rest_framework import serializers 
from myapp.models import Persona, Agenda, Turno, Cliente, Profesional, Especialidad, Servicio
 
class PersonaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Persona
        fields = ('nombre',
                  'apellido',
                  'cedula',
                  'telefono',
                  'mail')

class AgendaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Agenda
        fields = ('fechas_disponibles')


class TurnoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Turno
        fields = ('fecha',
                  'hora',
                  'cliente',
                  'profesional',)
                  #'servicio')
    def validate(self, data):
        # Imprime solo los campos específicos de Cliente
        Turno_data = {key: data[key] for key in self.Meta.fields if key in data}
        print(f'Validando datos completos de Turno: {Turno_data}')

        return data

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre', 'apellido', 'cedula', 'telefono', 'mail', 'turno_asignado',)

    def validate(self, data):
        # Imprime solo los campos específicos de Cliente
        cliente_data = {key: data[key] for key in self.Meta.fields if key in data}
        print(f'Validando datos completos de cliente: {cliente_data}')

        return data


class ProfesionalSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(max_length=255) 

    class Meta:
        model = Profesional
        fields = ('nombre', 'turnos_habilitados')

        
    def validate(self, data):
        # Imprime solo los campos específicos de Cliente
        Profesional_data = {key: data[key] for key in self.Meta.fields if key in data}
        print(f'Validando datos completos de profesional: {Profesional_data}')

        return data
        
        
class EspecialidadSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Especialidad
        fields = ('nombre',
                  'servicio',
                  'profesional')
        
class ServicioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Servicio
        fields = ('nombre',
                  'profesional',)