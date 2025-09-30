from .base import *
from tpusa.settings import get_secret

SECRET_KEY = get_secret("SECRET_KEY")

raw_hosts: str | None = get_secret("ALLOWED_HOSTS", "")
if raw_hosts:
    ALLOWED_HOSTS = [host.strip() for host in raw_hosts.split(",") if host.strip()]


EMAIL_BACKEND = get_secret(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = get_secret("EMAIL_HOST")
EMAIL_PORT = int(get_secret("EMAIL_PORT", 587))
EMAIL_USE_TLS = get_secret("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = get_secret("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_secret("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = get_secret(
    "DEFAULT_FROM_EMAIL", f"Turning Point USA @ ODU <{EMAIL_HOST_USER}>"
)

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CORS_ALLOW_ALL_ORIGINS = bool(get_secret("CORS_ALLOW_ALL_ORIGINS", 0))
CORS_ALLOW_NULL_ORIGIN = bool(get_secret("CORS_ALLOW_NULL_ORIGIN", 0))
CORS_ALLOWED_ORIGINS = [get_secret("CORS_ALLOWED_ORIGINS", "")]
