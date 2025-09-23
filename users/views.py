from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.hashers import make_password

@api_view(['POST'])
def register_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return Response({"error": "Email y contraseña requeridos"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=email).exists():
        return Response({"error": "El usuario ya existe"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=email,
        email=email,
        password=make_password(password)
    )
    return Response({"message": "Usuario creado con éxito"}, status=status.HTTP_201_CREATED)

