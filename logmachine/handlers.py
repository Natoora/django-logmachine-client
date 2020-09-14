import json
import logging.config  # needed when logging_config doesn't start with logging.config

import requests
from django.conf import settings
from django.utils import timezone
from django.views.debug import ExceptionReporter

from .conf import PROJECT_NAME, APPENV, APP_LOCATION, LOG_MACHINE_URL

logger = logging.getLogger()


class ExceptionHandler(logging.Handler):
    """
    An exception log handler that gathers data to be posted to LogMachine.
    """

    def __init__(self):
        super().__init__()

    def emit(self, record):
        """
        Gather data required for the reocrd and post to log machine.
        Overrides emit method of parent Handler.

        If the request is passed as the first argument to the log record,
        request data will be provided as part of the record.
        """
        try:
            request = record.request
            subject = '%s (%s IP): %s' % (
                record.levelname,
                ('internal' if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS
                 else 'EXTERNAL'),
                record.getMessage()
            )
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            request = None
        data = self.gather_data(request=request, subject=subject, record=record)
        self.post_record(payload=data)

    @staticmethod
    def get_report(request, record):
        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)
        report = ExceptionReporter(request, *exc_info)
        return report

    @staticmethod
    def format_subject(subject):
        """
        Escape CR and LF characters.
        """
        return subject.replace('\n', '\\n').replace('\r', '\\r')

    def gather_data(self, request, subject, record):
        report = self.get_report(request, record)
        return {
            "project_name": PROJECT_NAME,
            "appenv": APPENV,
            "app_location": APP_LOCATION,
            "created_at": timezone.localtime(),
            "level": record.levelno,
            "subject": self.format_subject(subject),
            "logger_name": record.name,
            "path_name": record.pathname,
            "func_name": record.funcName,
            "line_num": record.lineno,
            "traceback": report.get_traceback_text(),
        }

    @staticmethod
    def post_record(payload):
        try:
            r = requests.post(
                "{}/api/logs/".format(LOG_MACHINE_URL),
                data=json.dumps(payload, default=str),  # This converts types to str if they're not "json serializable"
                timeout=1,
                headers={
                    'Content-type': 'application/json',
                    'Accept': 'application/json'
                }
            )
            r.raise_for_status()
        except Exception as e:
            print(e)
            logger.info("Exception thrown when posting record to Log Machine")
