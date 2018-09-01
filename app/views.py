from app import app
from flask import request, json, jsonify
from app.models import Question
from app.validate import FieldValidation

all_questions = []
all_answers = []

validate = FieldValidation()


@app.route("/api/v1/questions", methods=["POST"])
# posting a question
def post_question():
    data = request.get_json()
    question = data.get("question").strip()
    question_id = len(all_questions) + 1
    validation = validate.validate_input(question)
    if validation:
        return validation
    valid = validate.validate_type(question)
    if valid:
        return jsonify({"message": "Invalid question entered, please try again"}), 400
    if any(d["question"] == question for d in all_questions):
        return jsonify({"message": "Question already exists, check it out for the answer"}), 409

    new_question = Question(question_id, question)
    all_questions.append(new_question)

    for question in range(len(all_questions)):
        if (all_questions[question]["question_id"]) == int(question_id):
            return jsonify({"message": "New question successfully posted",
                            "Question": all_questions[question]["question"]
                            }), 201


@app.route("/api/v1/questions", methods=["GET"])
# View all questions
def get_all_questions():
    if len(all_questions) > 0:
        return jsonify({
            "message": "Successfully viewed questions",
            "available questions": [
                question.__dict__ for question in all_questions
            ]
        }), 200
    else:
        return jsonify({"message": "No Question has been posted yet"}), 400
