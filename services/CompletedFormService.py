import json

from Answer import Answer
from DateQuestion import DateQuestion
from DropdownQuestion import DropdownQuestion
from Form import Form
from NumberQuestion import NumberQuestion
from TextQuestion import TextQuestion
from services.Service import Service
from CompletedForm import CompletedForm


class CompletedFormService(Service):

    def __init__(self):
        super().__init__()
        self.file = 'completed_form.json'
        self.completed_forms = []

    def fetch(self):
        try:
            with open(f'{self.url}{self.file}', 'r') as file:
                dictionaries = json.load(file)
                completed_forms = []
                for item in dictionaries:
                    form = Form(item['form']['name'])
                    for question in item['form']['questions']:
                        if question['type'] == 'TEXT':
                            form.questions.append(TextQuestion(question['question']))
                        elif question['type'] == 'NUMBER':
                            form.questions.append(NumberQuestion(question['question']))
                        elif question['type'] == 'DROPDOWN':
                            form.questions.append(DropdownQuestion(question['question'], question['options']))
                        elif question['type'] == 'DATE':
                            form.questions.append(DateQuestion(question['question']))

                    completed_form = CompletedForm(form)
                    answers = []

                    for answer in item['answers']:
                        answers.append(Answer(answer['answer']))
                    completed_form.answers = answers
                    completed_forms.append(completed_form)
                self.completed_forms = completed_forms
                return completed_forms
        except Exception as error:
            pass

    def store(self):
        with open(f'{self.url}{self.file}', 'w') as file:
            file.write(self.forms_to_json())

    def forms_to_json(self):
        return json.dumps(self.completed_forms, default=lambda o: o.__dict__, indent=2, sort_keys=True)
