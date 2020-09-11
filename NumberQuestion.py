import re
from Question import Question


class NumberQuestion(Question):
    def __init__(self, question):
        super().__init__(question)
        self.type = 'NUMBER'

    def validate(self, answer):
        pattern = r'^[0-9]+$'
        match = re.match(pattern, answer)
        return match is not None


