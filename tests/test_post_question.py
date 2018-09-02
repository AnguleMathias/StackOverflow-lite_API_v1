import unittest
from flask import json
from run import app


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_empty_question(self):
        """ Validation test for empty post"""
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question=" "), ))
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "No input given")
        self.assertEqual(response.status_code, 400)

    def test_adding_question_with_short_post(self):
        """ Validation test for a short question"""
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="What is?"), ))
        reply = json.loads(response.data)
        self.assertEqual(reply["message"], "Input has to be at least 10 characters long")
        self.assertEqual(response.status_code, 400)

    def test_adding_existing_question(self):
        """ Test for posting question successfully """
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="This is question three four"), ))
        response2 = self.app.post("/api/v1/questions",
                                  content_type='application/json',
                                  data=json.dumps(dict(question="This is question three four"), ))
        reply = json.loads(response2.data)
        self.assertEqual(reply["message"], "Question already exists, check it out for the answer")
        self.assertEqual(response.status_code, 201)
