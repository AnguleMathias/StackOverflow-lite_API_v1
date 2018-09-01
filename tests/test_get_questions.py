import unittest
from flask import json
from run import app


class TestViewingQuestions(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_questions(self):
        """Test to get all questions"""
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="This is my question 1"), ))

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/questions",
                                 content_type='application/json',
                                 data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"], "Successfully viewed questions")
        self.assertEquals(response2.status_code, 200)

    def test_get_single_question(self):
        """Test to get a question by its id"""
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="This is my question 1"), ))
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="This is my question 2"), ))
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/questions/2",
                                 content_type='application/json',
                                 data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(response2.status_code, 200)

    def test_get_question_with_wrong_id(self):
        """Test to get a single question with wrong id"""
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="This is my question 1"), ))
        response = self.app.post("/api/v1/questions",
                                 content_type='application/json',
                                 data=json.dumps(dict(question="This is my question 2"), ))
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/questions/q",
                                 content_type='application/json',
                                 data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"], "Id should be an integer")
        self.assertEquals(response2.status_code, 400)
