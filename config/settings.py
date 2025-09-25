from pathlib import Path
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------- Env ----------------
env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)
env_file = BASE_DIR / ".env"
if env_file.exists():
    environ.Env.read_env(str(env_file))

SECRET_KEY = env("SECRET_KEY", default="unsafe-dev-key")
DEBUG = env.bool("DEBUG", default=False)

# Producción: pon dominios reales (Railway + localhost)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[
    "planb-production.up.railway.app", "localhost", "127.0.0.1"
])

# ---------------- Apps ----------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # terceros
    "rest_framework",
    "corsheaders",
    # "whitenoise.runserver_nostatic",  # opcional si usas WhiteNoise

    # tus apps
    "users",
]

# ⚠️ SOLO deja esto si realmente tienes un modelo custom en users/models.py
# que hereda de AbstractUser + migraciones creadas ANTES del primer migrate.
# Si NO lo tienes, comenta esta línea y usa el User estándar.
AUTH_USER_MODEL = "users.User"

# ---------------- Middleware ----------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",      # debe ir primero
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",  # si sirves estáticos con WhiteNoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "config.wsgi.application"

# ---------------- Base de datos (PostgreSQL por DATABASE_URL) ----------------
# Ejemplo DATABASE_URL (Railway): postgres://USER:PASSWORD@HOST:PORT/DBNAME
DATABASES = {
    "default": env.db(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}")
}
# Mantener conexiones abiertas (mejor para PaaS)
DATABASES["default"]["CONN_MAX_AGE"] = env.int("DB_CONN_MAX_AGE", default=600)

# ---------------- Auth REST ----------------
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

# ---------------- i18n ----------------
LANGUAGE_CODE = "es-cl"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_TZ = True

# ---------------- Static ----------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
# Si usas WhiteNoise:
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ---------------- CORS / CSRF ----------------
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://fastidious-hamster-a7997b.netlify.app",
    "http://localhost:5173",
]
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=[
    "https://fastidious-hamster-a7997b.netlify.app",
    "https://planb-production.up.railway.app",
])

# Detrás de proxy (Railway usa HTTPS)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
# SECURE_SSL_REDIRECT = not DEBUG  # opcional en prod


CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://fastidious-hamster-a7997b.netlify.app",
    "http://localhost:5173",
]