from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
import logging
log = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        email = (request.data.get('email') or '').strip().lower()
        password = request.data.get('password') or ''
        if not email or not password:
            return Response({'error': 'email y password son requeridos'}, status=400)

        username = email.split('@')[0] or email  # User estándar requiere username
        User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'Usuario creado'}, status=201)

    except IntegrityError:
        return Response({'error': 'El email/usuario ya existe'}, status=409)
    except Exception as e:
        log.exception('Fallo en register_user')
        return Response({'error': str(e)}, status=500)