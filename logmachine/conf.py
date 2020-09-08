from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    LOG_MACHINE_URL = settings.LOG_MACHINE["LOG_MACHINE_URL"]
    PROJECT_NAME = settings.LOG_MACHINE["PROJECT_NAME"]
    APPENV = settings.LOG_MACHINE["APPENV"]
    APP_LOCATION = settings.LOG_MACHINE["APP_LOCATION"]
except Exception as e:
    raise ImproperlyConfigured(
        "Problem with Log Machine settings: \n{}".format(e)
    )
