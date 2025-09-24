# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

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