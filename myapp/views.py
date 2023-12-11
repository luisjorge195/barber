from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Turno
from rest_framework.parsers import JSONParser 
from myapp.serializers import ClienteSerializer, TurnoSerializer
from django.http.response import JsonResponse


@api_view(['POST'])
def reservar_turno(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        # Extraer el objeto cliente del diccionario de datos
        cliente_data = data.pop('cliente', {})
        profesional_pk = data.pop('profesional', None)

        # Crear instancias de los serializadores
        cliente_serializer = ClienteSerializer(data=cliente_data)
        turno_serializer = TurnoSerializer(data=data)

        # Validar los serializadores
        cliente_serializer.is_valid()
        turno_serializer.is_valid()

        if cliente_serializer.is_valid() and turno_serializer.is_valid():
            # Verificar si ya existe un turno con la misma fecha y hora

            # Guardar el cliente
            cliente_instance = cliente_serializer.save()

            # Asignar la clave primaria del cliente al campo 'cliente' del turno
            data['cliente'] = cliente_instance.pk

            # Asignar el ID del profesional al campo 'profesional' del turno
            data['profesional'] = profesional_pk

            print("Datos recibidos:", profesional_pk)

            # Guardar el turno
            turno_instance = turno_serializer.save()

            # Asignar el turno al cliente y guardar
            cliente_instance.turno_asignado = turno_instance
            cliente_instance.save()

            turno_instance.cliente = cliente_instance
            # Asignar la instancia del profesional al turno y guardar
            turno_instance.save()

            print("Datos recibidos:", turno_instance)

            return JsonResponse({'mensaje': f'Cliente (ID: {cliente_instance.pk}) y turno (ID: {turno_instance.pk}) creados exitosamente'}, status=status.HTTP_201_CREATED)
        else:
   
            return Response({'error': 'Error en la solicitud. Verifica los errores en la consola.'}, status=status.HTTP_400_BAD_REQUEST)

"""""
    try:
        data = request.data 
        




   if request.method == 'POST':
        cliente_data = JSONParser().parse(request)
        tutorial_serializer = ClienteSerializer(data=cliente_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




        # Validación de datos
        required_fields = ['nombre', 'apellido', 'cedula', 'telefono', 'mail', 'fecha', 'hora']
        for field in required_fields:
            if field not in data:
                return Response({"error": f"Campo '{field}' faltante en los datos"}, status=status.HTTP_400_BAD_REQUEST)

        # Puedes agregar más validaciones según tus requisitos

        # Obtener o crear el cliente
        nuevo_cliente, created = Cliente.objects.get_or_create(
            nombre=data['nombre'],
            apellido=data['apellido'],
            cedula=data['cedula'],
            telefono=data['telefono'],
            mail=data['mail']
        )

        # Crear el turno y asociarlo al cliente
        nuevo_turno = Turno(
            fecha=data['fecha'],
            hora=data['hora'],
            cliente=nuevo_cliente
        )

        # Validar y guardar el turno
        nuevo_turno.full_clean()
        nuevo_turno.save()

        return Response({'mensaje': 'Turno reservado exitosamente', 'id': nuevo_turno.id}, status=status.HTTP_201_CREATED)

    except json.JSONDecodeError as e:
        return Response({"error": "Error en el formato JSON de la solicitud"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        """