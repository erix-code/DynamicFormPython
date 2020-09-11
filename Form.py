from DropdownQuestion import DropdownQuestion
from TextQuestion import TextQuestion
# from services.FormService import FormService


class Form:
    def __init__(self, name):
        self.questions = []
        self.name = name

