SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    "tests",
]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
USE_TZ = True
LOGGING = {
    'version': 1,
    'handlers': {
        'mail_admins': {
            'level': 'INFO',
            'class': 'logmachine.handlers.ExceptionHandler',
        }
    },
    'loggers': {
        'logmachine': {
            'handlers': ['mail_admins'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
