from re import match
from Question import Question


class DropdownQuestion(Question):
    def __init__(self, question, options):
        super().__init__(question)
        self.options = options
        self.type = 'DROPDOWN'

    def validate(self, answer):
        pattern = r'^[0-9]+$'
        check = match(pattern, answer)
        if check:
            return len(self.options) > int(answer) >= 0
        else:
            return False

