import unittest
from flask import json
from run import app


class TestGetAnswer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

