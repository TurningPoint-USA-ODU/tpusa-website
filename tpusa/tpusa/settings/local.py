from .base import *
from dotenv import load_dotenv


load_dotenv(BASE_DIR / ".env.local")

SECRET_KEY: str = "django-insecure-h!rfn@r1-s=docu2hv*j3*!$t6=5(!dcf_mcj^-9%oaumv=agk"

DEBUG: bool = True

ALLOWED_HOSTS: list[str] = []
