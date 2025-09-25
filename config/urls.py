# config/urls.py
from django.contrib import admin
from django.urls import path  # usa include si delegas a users.urls
from django.http import JsonResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)
from users.views import register_user, private_ping

def health(_): return JsonResponse({"status": "ok"})
def home(_):   return JsonResponse({"message": "Backend online", "health": "/health/", "api": "/api/"})

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth & usuarios
    path("api/register/", register_user),
    path("api/privado/", private_ping),

    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    # health/home
    path("health/", health),
    path("", home),
]
