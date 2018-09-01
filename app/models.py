class Question:
    """
    Model class for the question
    """
    def __init__(self, question_id, question):
        self.question_id = question_id
        self.question = question

    def __getitem__(self, item):
        return getattr(self, item)

    def __repr__(self):
        return repr(self.__dict__)


class Answer:
    """
        Model class for Answers
        """
    def __init__(self, answer_id, answer, question_id):
        self.answer_id = answer_id
        self.answer = answer
        self.question_id = question_id

    # method to enable us access class attributes as items
    def __getitem__(self, item):
        return getattr(self, item)

    # method to enable us display class objects as dictionaries
    def __repr__(self):
        return repr(self.__dict__)
