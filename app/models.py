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
