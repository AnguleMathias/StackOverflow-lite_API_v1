from app import app
from flask import request, json, jsonify

all_questions = []
all_answers = []

validate = FieldValidation()
