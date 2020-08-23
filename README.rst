===================
Django Log Machine
===================

Django app that provides the functionality and connection settings
to be able to send exception information to Log Machine.

Setup
-----

1. Add "logmachine" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'logmachine',
    ]

2. Include the logmachine URLconf in your project urls.py like this::

    url(r'api/', include('logmachine.urls')),

3. Replace the default Django exception handler for mail_admins witht the Log Machine handler::

    LOGGING = {
        ...
        'mail_admins': {
            'level': 'ERROR',
            'class': 'logmachine.handlers.ExceptionHandler',
        },
    }

4. Run ``python manage.py migrate`` to create the logmachine models.


Development
-----------
1. Run setup instructions as above.

2. Run ``(venv) $ pip install --editable /path/to/django-logmachine``

Now every change made in django-logmachine will be reflected in the target project.
