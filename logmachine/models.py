import logging

from django.db import models

LOG_LEVELS = (
    (logging.NOTSET, 'Not Set'),
    (logging.INFO, 'Info'),
    (logging.WARNING, 'Warning'),
    (logging.DEBUG, 'Debug'),
    (logging.ERROR, 'Error'),
    (logging.FATAL, 'Fatal'),
)


class ExceptionLog(models.Model):
    """
    Represents a message written to the logger.
    """
    created_at = models.DateTimeField()
    level = models.IntegerField(
        choices=LOG_LEVELS,
        default=logging.ERROR,
        db_index=True
    )
    subject = models.CharField(max_length=200)
    logger_name = models.CharField(max_length=100)
    path_name = models.CharField(max_length=200)
    func_name = models.CharField(max_length=100)
    line_num = models.IntegerField()
    traceback = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ('-created_at',)
