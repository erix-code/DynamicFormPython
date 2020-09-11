from datetime import datetime
from Question import Question


class DateQuestion(Question):
    def __init__(self, question):
        super().__init__(question)
        self.type = 'DATE'
    def validate(self, answer):
        try:
            datetime.strptime(answer, '%Y-%m-%d')
            return True
        except ValueError:
            return False

