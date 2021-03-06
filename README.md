Django Log Machine
==================

Log Machine client app for Django.

Log handling and connection settings to send information to Log Machine.

Client Installation
-------------------

1. Install with pip:

    ```
    pip install git+https://github.com/Natoora/django-logmachine-client.git@{version}
   
    # Where version can be a tag, a branch, or a commit.
    ```

2. Add "logmachine" to your INSTALLED_APPS setting like this:

    ``` 
    INSTALLED_APPS = [
        ...
        'logmachine',
    ]
    ```

3. Replace the default Django exception handler for mail_admins witht the Log Machine handler:

    ``` 
    LOGGING = {
        ...
        'mail_admins': {
            'level': 'ERROR',
            'class': 'logmachine.handlers.ExceptionHandler',
        },
    }
    ```

Development
-----------
1. Clone the repo.

2. On the target project run:
    ``` 
    (venv) $ pip install --editable /path/to/django-logmachine
    ```  

3. Run setup instructions as above.

4. Include the logmachine URLconf in your project urls.py like this:
    ``` 
    url(r'api/', include('logmachine.urls')),
    ```

5. Now you can trigger exceptions with the following URLs:
    ``` 
    /api/unhandled_500_error
    /api/handled_500_error
    ```
   
6. Checkout the Log Machine server and run it locally.
    ```
    git checkout https://github.com/Natoora/LogMachine
    ```
   
7. Set the LOG_MACHINE_URL in the project settings to the address the local Log Machine is running at.

Testing
-------

1. Install test requirements
    ```
    pip install -r requirements/requirements-testing.txt
    ```

2. Run test script:
    ```
    (venv) $ python runtests.py
    ```

Releasing
---------

1. Increment version number in setup.py

2. Commit and push changes.

3. Create release on GitHub with the version number.

4. The release can then be installed into Django projects like this:
    ``` 
    git+https://github.com/Natoora/django-logmachine-client.git@{version number}
    ```
