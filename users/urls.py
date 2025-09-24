
from django.urls import path
from .views import register_user
from django.http import JsonResponse

def api_root(_):
    return JsonResponse({"api": "ok", "register": "/api/register/"})

urlpatterns = [
    path("", api_root),                     # GET /api/ -> {"api":"ok",...}
    path("register/", register_user),       # POST /api/register/
]