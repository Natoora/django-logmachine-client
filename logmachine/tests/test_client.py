from unittest.mock import patch

import requests
from django.test import TestCase
from django.utils import timezone


class TestLogMachineClient(TestCase):

    def _mock_record(self):
        return {
            "created_at": timezone.localtime(),
            "level": 1,
            "subject": "something happened",
            "logger_name": "Logger Name",
            "path_name": "/path/to/problem",
            "func_name": "func_name",
            "line_num": 134,
            "traceback": "traceback text",
        }

    @patch('requests.post')
    def test_post(self, mock_post):
        record = self._mock_record()
        resp = requests.post("logmachine.natoora.com", data=record)
        mock_post.assert_called_with("logmachine.natoora.com", data=record)
