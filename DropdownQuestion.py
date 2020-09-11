from Question import Question


class DropdownQuestion(Question):
    def __init__(self, question, options):
        super().__init__(question)
        self.options = options
        self.type = 'DROPDOWN'

    def validate(self, answer: int):
        return len(self.options) > int(answer) >= 0


d_question = DropdownQuestion('Cual es tu genero?', ['shit', 'shit', 'shit'])
# print(dquestion.validate('321321'))
# print(dquestion.validate(0))
# print(dquestion.validate(1))
# print(dquestion.validate(2))
# print(dquestion.validate(3))
