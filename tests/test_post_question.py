import unittest
from run import app
from app import views
from app.models import Question
from flask import jsonify, json


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def empty_question(self):
        """ Validation test for empty post"""
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question=" "), ))
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "No input given")
        self.assertEquals(response.status_code, 400)

    def short_question(self):
        """ Validation test for a short question"""
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="What is?"), ))
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Input has to be at least 10 characters long")
        self.assertEquals(response.status_code, 400)

    def existing_question(self):
        """ Test for posting question successfully """
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="This is question three four"), ))
        response2 = self.app.post("/api/v1/questions",
                                  content_type='application/json',
                                  data=json.dumps(dict(question="This is question three four"), ))
        reply = json.loads(response2.data)
        self.assertEquals(reply["message"], "Question already exists")
        self.assertEquals(response.status_code, 409)
