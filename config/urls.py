# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # /api/token/  
    TokenRefreshView,     # /api/token/refresh/
    TokenVerifyView,      # /api/token/verify/
)
from users.views import register_user, private_ping  



def health(_):
    return JsonResponse({"status": "ok"})

def home(_):
    return JsonResponse({"message": "Backend online", "health": "/health/", "api": "/api/"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),   # <-- ajusta si tu app NO se llama "users"
    path("health/", health),               # GET /health/ -> {"status":"ok"}
    path("", home),                        # GET / -> {"message": ...}
]




urlpatterns = [
    path("admin/", admin.site.urls),

    # tu registro existente
    path("api/register/", register_user),

    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    # endpoint protegido de prueba
    path("api/privado/", private_ping),
]