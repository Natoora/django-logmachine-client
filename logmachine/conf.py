from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    LOG_MACHINE_URL = settings.LOG_MACHINE["LOG_MACHINE_URL"]
    CLIENT_NAME = settings.LOG_MACHINE["CLIENT_NAME"]
except Exception as e:
    raise ImproperlyConfigured(
        "Problem with Log Machine settings: \n{}".format(e)
    )
