from flask import request, jsonify
from app import app
from app.models import Question, Answer
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
    if "question" not in question:
        return jsonify({"message": "Invalid question key has been entered, please try again"}), 400
    if valid:
        return jsonify({"message": "Invalid question entered, please try again"}), 400
    if any(d["question"] == question for d in all_questions):
        return jsonify({"message": "Question already exists, check it out for the answer"}), 409

    new_question = Question(question_id, question)
    all_questions.append(new_question)

    for question in range(len(all_questions)):
        if (all_questions[question]["question_id"]) == int(question_id):
            return jsonify({"message": "New question successfully posted",
                            "Question": all_questions[question]["question"]}), 201


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
    return jsonify({"message": "No Question has been posted yet"}), 400


@app.route("/api/v1/questions/<question_id>", methods=["GET"])
# GET a specific question by id
def get_a_question(question_id):
    _id = question_id.strip()
    validation = validate.validate_entered_id(_id)
    if validation:
        return validation
    for question in range(len(all_questions)):
        if (all_questions[question]["question_id"]) == int(_id):
            return jsonify({
                "Question":
                    all_questions[question]["question"]
            }), 200
    return jsonify({
        "message": "No such question is available",
    }), 204


@app.route("/api/v1/questions/<question_id>/answer", methods=["POST"])
# POST answer to a specific question
def post_answer(question_id):
    _id = question_id.strip()
    validation = validate.validate_entered_id(_id)
    if validation:
        return validation

    data = request.get_json()
    answer = data.get("answer")
    ans = answer.strip()
    validation2 = validate.validate_input(ans)
    if validation2:
        return validation2

    if "answer" not in answer:
        return jsonify({"message": "Invalid answer key entered, please try again"}), 400
    if any(dy["answer"] == ans for dy in all_answers):
        if any(xy["question_id"] == _id for xy in all_answers):
            return jsonify({"message": "Answer already exists"}), 409

    for question in range(len(all_questions)):
        if (all_questions[question]["question_id"]) == int(_id):
            ans_id = len(all_answers) + 1
            new_answer = Answer(ans_id, ans, _id)
            all_answers.append(new_answer)
            return jsonify({
                "message": "Answer successfully posted to question",
                "Question answered": [all_questions[question]["question"]]}), 201
    return jsonify({"message": "No such question is available", }), 204


@app.route("/api/v1/answers", methods=["GET"])
def get_all_answers():
    if len(all_answers) > 0:
        return jsonify({
            "message": "Successfully viewed Answers",
            "Available answers": [answer.__dict__ for answer in all_answers]}), 200
    return jsonify({"message": "No answer has been posted yet"}), 404
