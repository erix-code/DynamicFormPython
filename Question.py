from datetime import datetime
from QuestionType import *


class Question:
    def __init__(self, question, question_type):
        self.question = question
        self.question_type = question_types[question_type - 1]
        if 'DROPDOWN' == self.question_type.name:
            self.options = []
        else:
            self.options = None

    def validate(self, answer: str):
        """ Validate the answer by the type """
        if self.question_type.name == 'TEXT':
            for char in answer:
                if char == ' ' or char.isalpha():
                    continue
                else:
                    return False
            return True
        elif self.question_type.name == 'NUMBER':
            return answer.isnumeric()
        elif self.question_type.name == 'DATE':
            try:
                datetime.strptime(answer, '%Y-%m-%d')
                return True
            except ValueError:
                return False
        elif self.question_type.name == 'DROPDOWN':
            return answer.isnumeric() and len(self.options) >= int(answer) > 0

    def add_option(self, option):
        self.options.append(option)


question1 = Question('Whats your name?', 1)
# print(question1.question, question1.validate('dsfafdsa dfaafasdfads fasdsfad'))
# print(question1.question, question1.validate('fdafsad323123fasfsadfads'))

q2 = Question('What\'s your favorite number?', 2)
# print(q2.question, q2.validate('32142141124'))
# print(q2.question, q2.validate('2232frew'))
# Dropdown testing
q3 = Question('What\'s your gender?', 3)
q3.add_option('Male')
q3.add_option('Female')
q3.add_option('Other')
# print(q3.question, q3.validate('1'))
# print(q3.question, q3.validate('2'))
# print(q3.question, q3.validate('3'))
# print(q3.question, q3.validate('dsfafdsa dfaafasdfads fasdsfad'))

q4 = Question('How are you?', 4)
# print(q4.question, q4.validate('2003-3-4'))
# print(q4.question, q4.validate('200334'))
