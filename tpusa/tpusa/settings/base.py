from pathlib import Path
from typing import Dict, Union

from tpusa.tpusa.settings import get_secret

DEBUG = bool(get_secret("DEBUG", "False"))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent


# Application definition

INSTALLED_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
    "register",
]

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF: str = "tpusa.urls"

TEMPLATES: list[Dict[str, Union[str, list[Path], bool, Dict[str, list[str]]]]] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "tpusa" / "templates"],
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

WSGI_APPLICATION: str = "tpusa.wsgi.application"

# Password Reset timeout (60 seconds * 10 minutes)
PASSWORD_RESET_TIMEOUT = 60 * 10

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES_PROD: Dict[str, Dict[str, Union[str, Path, int, None]]] = {
    "default": {
        "ENGINE": f"django.db.backends.{get_secret("DATABASE_ENGINE", "sqlite3")}",
        "NAME": get_secret("DATABASE_NAME", "bibleqna"),
        "USER": get_secret("DATABASE_USERNAME", "admin"),
        "PASSWORD": get_secret("DATABASE_PASSWORD", "admin"),
        "HOST": get_secret("DATABASE_HOST", "db"),
        "PORT": int(get_secret("DATABASE_PORT", 5432)),
    }
}

DATABASES_LOCAL: Dict[str, Dict[str, Union[str, Path, int, None]]] = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DATABASES: Dict[str, Dict[str, Union[str, Path, int, None]]] = (
    DATABASES_PROD if not DEBUG else DATABASES_LOCAL
)


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS: list[Dict[str, str]] = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE: str = "en-us"

TIME_ZONE: str = "America/New_York"

USE_I18N: bool = True

USE_TZ: bool = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL: str = "static/"

STATICFILES_DIRS: list[Path] = [BASE_DIR / "tpusa" / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD: str = "django.db.models.BigAutoField"
