
import unittest
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_view_should_use_correct_template(self):
        response = self.app.get('/')
        self.assertIn(b'<title>Chequer</title>', response.data)

    def test_index_view_with_querystring_also_uses_correct_template(self):
        response = self.app.get('/?number=1234567.89')
        self.assertIn(b'<title>Chequer</title>', response.data)

    def test_index_view_with_querystring_returns_correct_output(self):
        response = self.app.get('/?number=123.45')
        self.assertIn(b'RINGGIT MALAYSIA SATU RATUS DUA PULUH TIGA DAN SEN EMPAT PULUH LIMA SAHAJA', response.data)
