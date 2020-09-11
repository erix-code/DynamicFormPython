import json

from services.Service import Service
from Form import Form
from TextQuestion import TextQuestion
from DropdownQuestion import DropdownQuestion
from NumberQuestion import NumberQuestion
from DateQuestion import DateQuestion


class FormService(Service):
    def __init__(self):
        super().__init__()
        self.file = 'forms.json'
        self.forms = []

    def fetch(self):
        try:
            with open(f'{self.url}{self.file}', 'r') as file:
                dictionaries = json.load(file)
                forms = []
                for item in dictionaries:
                    new_form = Form(item['name'])
                    for question in item['questions']:
                        if question['type'] == 'TEXT':
                            new_form.questions.append(TextQuestion(question['question']))
                        elif question['type'] == 'NUMBER':
                            new_form.questions.append(NumberQuestion(question['question']))
                        elif question['type'] == 'DROPDOWN':
                            new_form.questions.append(DropdownQuestion(question['question'], question['options']))
                        elif question['type'] == 'DATE':
                            new_form.questions.append(DateQuestion(question['question']))
                    forms.append(new_form)
                self.forms = forms
                return forms
        except Exception as error:
            pass

    def store(self):
        with open(f'{self.url}{self.file}', 'w') as file:
            file.write(self.forms_to_json())

    def forms_to_json(self):
        return json.dumps(self.forms, default=lambda o: o.__dict__, indent=2, sort_keys=True)
