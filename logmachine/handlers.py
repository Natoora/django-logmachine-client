import logging.config  # needed when logging_config doesn't start with logging.config

from django.conf import settings
from django.utils import timezone
from django.views.debug import ExceptionReporter


class ExceptionHandler(logging.Handler):
    """An exception log handler that saves to LogMachine.

    If the request is passed as the first argument to the log record,
    request data will be provided as part of the record.
    """

    def __init__(self):
        super().__init__()

    def emit(self, record):
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
        report = self.get_report(request, record)
        self.save_to_db(
            subject=self.format_subject(subject),
            record=record,
            traceback=report.get_traceback_text()
        )

    def get_report(self, request, record):
        if record.exc_info:
            exc_info = record.exc_info
        else:
            exc_info = (None, record.getMessage(), None)
        report = ExceptionReporter(request, *exc_info)
        return report

    def format_subject(self, subject):
        """
        Escape CR and LF characters.
        """
        return subject.replace('\n', '\\n').replace('\r', '\\r')

    def save_to_db(self, subject, record, traceback):
        from .models import ExceptionLog
        ExceptionLog.objects.create(
            created_at=timezone.localtime(),
            level=record.levelno,
            subject=subject,
            logger_name=record.name,
            path_name=record.pathname,
            func_name=record.funcName,
            line_num=record.lineno,
            traceback=traceback
        )
