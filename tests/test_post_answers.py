import unittest
from flask import json
from run import app


class TestAnswer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post(self):
        """ Test post answer """
        response = self.app.post("/api/v1/questions/1/answer",
                                 content_type='application/json',
                                 data=json.dumps(dict(answer="This is my answer 1"), ))
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Answer already exists")
        self.assertEquals(response.status_code, 409)

    def test_empty_answer_post(self):
        """ Test for posting an empty answer post"""
        response = self.app.post("/api/v1/questions/1/answer",
                                 content_type='application/json',
                                 data=json.dumps(dict(answer="  "), ))
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "No input given")
        self.assertEquals(response.status_code, 400)
        response2 = self.app.post("/api/v1/questions/1/answer",
                                  content_type='application/json',
                                  data=json.dumps(dict(answer="This is"), ))
        reply = json.loads(response2.data)
        self.assertEquals(reply["message"], "Input has to be at least 10 characters long")
        self.assertEquals(response2.status_code, 400)

    def test_wrong_question_id(self):
        response = self.app.post("/api/v1/questions/a/answer",
                                 content_type='application/json',
                                 data=json.dumps(dict(answer="This is my answer 1"), ))
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Id should be an integer")
        self.assertEquals(response.status_code, 400)
