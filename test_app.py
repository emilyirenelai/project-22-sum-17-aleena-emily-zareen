# tests/test_app.py

import unittest
import os
os.environ['TESTING'] = 'true'

from app import app 

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.clent.get("/")
        