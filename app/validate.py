import re
from flask import jsonify


class FieldValidation:

    def validate_entered_id(self, id):
        try:
            _id = int(id)
        except ValueError:
            return jsonify({"message": "Id should be an integer"}), 400

    def validate_input(self, input):

        if not input:
            return jsonify({"message": "No input given"}), 400
        if len(input) < 10:
            return jsonify({"message": "Input has to be at least 10 characters long"}), 400

    def validate_type(self, input):
        if re.match("^[1-9]\d*(\.\d+)?$", input) is not None:
            return True
        return False
