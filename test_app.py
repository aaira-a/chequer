
import unittest
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_view_should_use_correct_template(self):
        response = self.app.get('/')
        self.assertIn(b'<title>Chequer</title>', response.data)
