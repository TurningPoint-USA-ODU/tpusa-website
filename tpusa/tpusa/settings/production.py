from .base import *
from tpusa.settings import get_secret

SECRET_KEY = get_secret("SECRET_KEY")

DEBUG = False

raw_hosts: str | None = get_secret("ALLOWED_HOSTS", "")
if raw_hosts:
    ALLOWED_HOSTS = [host.strip() for host in raw_hosts.split(",") if host.strip()]


SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CORS_ALLOW_ALL_ORIGINS = bool(get_secret("CORS_ALLOW_ALL_ORIGINS", 0))
CORS_ALLOW_NULL_ORIGIN = bool(get_secret("CORS_ALLOW_NULL_ORIGIN", 0))
CORS_ALLOWED_ORIGINS = [get_secret("CORS_ALLOWED_ORIGINS", "")]
