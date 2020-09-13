from abc import ABC, abstractmethod


class Question(ABC):

    def __init__(self, question):
        self.question = question
        self.type = None

    @abstractmethod
    def validate(self, answer: str):
        """ Validate the answer by the type """
        pass