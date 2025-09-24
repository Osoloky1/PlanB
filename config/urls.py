from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health(_):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),  # ajusta al módulo de urls que realmente tengas
    path("health/", health),              # <- prueba de vida
    # path("", health),  # opcional: si quieres que "/" responda algo
]