from django.test import TestCase


class TestHandler(TestCase):

    def test_post(self):
        try:
            0 / 2
        except Exception:
            print("Hi")
