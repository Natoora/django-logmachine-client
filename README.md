==================
Django Log Machine
==================

Log Machine client app for Django.

Log handling and connection settings to send information to Log Machine.

Setup
-----

1. Add "logmachine" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'logmachine',
    ]

2. Replace the default Django exception handler for mail_admins witht the Log Machine handler::

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
1. Clone the client app repo.

2. Run setup instructions as above.

3. On the target project run::
  
    (venv) $ pip install --editable /path/to/django-logmachine

  Now every change made in django-logmachine will be reflected in the target project.

4. Include the logmachine URLconf in your project urls.py like this::

    url(r'api/', include('logmachine.urls')),

5. Now you can trigger exceptions with the following URLs::

    /api/unhandled_500_error
    /api/handled_500_error
