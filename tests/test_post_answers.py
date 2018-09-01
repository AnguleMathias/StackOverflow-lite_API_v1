import unittest
from run import app
from flask import jsonify, json
from app.models import Answer
from app import views


class TestAnswer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(self):
        """ Test post answer """
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="This is my question 1"), ))
        response2 = self.app.post("/api/v1/questions/1/answer",
                                  content_type='application/json',
                                  data=json.dumps(dict(answer="This is my answer 1"), ))
        reply = json.loads(response2.data)
