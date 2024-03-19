from .base import *  # noqa: F403, F401

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# WAGTAILADMIN_BASE_URL required for notification emails
WAGTAILADMIN_BASE_URL = "http://localhost:8000"

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    'https://lexar.approwess.xyz/'
]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
try:
    from .local import *  # noqa
except ImportError:
    pass
