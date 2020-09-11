from Question import Question
import re


class TextQuestion(Question):
    def __init__(self, question):
        super().__init__(question)
        self.type = 'TEXT'

    def validate(self, answer):
        pattern = r'^[a-zA-Z]+$'
        result = re.match(pattern, answer)
        return result is not None


# question = TextQuestion('What is your name?')
# print(question.validate('fadfasfsadshit'))
