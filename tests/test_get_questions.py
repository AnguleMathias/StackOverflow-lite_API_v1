import unittest
from run import app
from flask import json, jsonify
from app.models import Question
from app import views


class TestViewingQuestions(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_fetching_available_questions(self):
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

