
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User


class RegisterView(APIView):
    """Explanation:
    The RegisterView class provides an endpoint for user registration. It accepts a POST request with user data and
    uses the UserRegisterSerializer to validate and create a new user in the system.

    Usage:
    - Receives a POST request with user data for registration.
    - Validates the data using UserRegisterSerializer, saves the user if valid, and returns the user's data in the response.
    - If the data is invalid, it returns the serializer errors with a 400 Bad Request status.
"""
    def post(self, request):
        """Crea un nuevo usuario utilizando los datos proporcionados en la solicitud.

    Parámetros:
    - request: La solicitud HTTP que contiene los datos del nuevo usuario a crear.

    Retorna:
    - Si los datos proporcionados son válidos, se crea un nuevo usuario utilizando el serializador
    `UserRegisterSerializer`.
    - Si los datos son válidos y se crea el usuario con éxito, se devuelve una respuesta con los datos del usuario
    recién creado.
    - Si los datos no son válidos, se devuelve una respuesta con los errores de validación y un estado de solicitud
    incorrecta (HTTP 400).

    Detalles:
    - Utiliza el serializador `UserRegisterSerializer` para validar y procesar los datos de la solicitud.
    - Si los datos son válidos, se guarda el nuevo usuario en la base de datos utilizando el método `save()` del
    serializador.
    - Si hay errores de validación, se devuelve una respuesta con los errores encontrados y un código de estado HTTP 400
     (Bad Request).

    Nota:
    Es importante que la solicitud contenga los datos necesarios para crear un nuevo usuario según las reglas definidas
    en el serializador `UserRegisterSerializer`."""
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    """Explanation:
    The UserView class serves as an API endpoint for retrieving and updating user information. GET request fetches the
    data of the currently authenticated user using the UserSerializer. PUT request updates the user's information based
    on the provided data using the UserUpdateSerializer.

    Usage:
    - GET request returns the serialized data of the currently authenticated user.
    - PUT request updates the information of the currently authenticated user using UserUpdateSerializer.
"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
    Obtiene los datos del usuario actual a partir de la solicitud.

    Parámetros:
    - request: La solicitud HTTP que contiene la información del usuario actual.

    Retorna:
    - Utiliza el serializador `UserSerializer` para procesar y transformar los datos del usuario actual.
    - Devuelve una respuesta HTTP con los datos serializados del usuario actual.

    Detalles:
    - Crea un serializador `UserSerializer` utilizando el usuario asociado con la solicitud actual.
    - El serializador transforma los datos del usuario en un formato específico (puede ser JSON u otro formato según la
    configuración).
    - Retorna una respuesta HTTP con los datos del usuario serializados.

    Nota:
    - Esta función se utiliza para obtener y devolver los datos del usuario actual según la información disponible en
    la solicitud.
    """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self,request):
        """Actualiza los datos del usuario actual con la información proporcionada en la solicitud.

    Parámetros:
    - request: La solicitud HTTP que contiene los datos a utilizar para actualizar el usuario.

    Retorna:
    - Obtiene el usuario actual a partir de la solicitud y actualiza sus datos utilizando el serializador
    `UserUpdateSerializer`.
    - Si la información proporcionada es válida y se actualiza con éxito, se devuelve una respuesta con los datos
    actualizados del usuario.
    - Si la información no es válida, se devuelve una respuesta con los errores de validación y un estado de solicitud
    incorrecta (HTTP 400).

    Detalles:
    - Busca y obtiene el usuario actual mediante su identificación (ID) contenido en la solicitud.
    - Utiliza el serializador `UserUpdateSerializer` para validar y aplicar los datos proporcionados en la solicitud
    para actualizar el usuario.
    - Si los datos son válidos, se guardan y actualizan en la base de datos mediante el método `save()` del serializador.
    - Retorna una respuesta con los datos actualizados del usuario si la operación se realiza con éxito.
    - Si hay errores de validación, se devuelve una respuesta con los errores encontrados y un código de estado
    HTTP 400 (Bad Request).

    Nota:
    - La actualización del usuario se realiza utilizando los datos proporcionados en la solicitud, siempre y cuando
    estos cumplan con las reglas de validación definidas en el serializador `UserUpdateSerializer`."""
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
