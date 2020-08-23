import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def handled_500_error(request):
    try:
        1 / 0
    except Exception as e:
        logger.exception(e)
    return HttpResponse('Hello 500!')


def unhandled_500_error(request):
    _ = 1 / 0
    return HttpResponse('Hello 500!')
