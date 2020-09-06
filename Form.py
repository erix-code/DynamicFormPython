import json
from Question import *
from StoreForm import StoreForm


class Form:
    def __init__(self, name):
        self.questions = []
        self.name = name

    def save(self, option='json'):
        pass

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2, sort_keys=True)


form = Form('My form')
form.questions.append(question1)
form.questions.append(q2)
form.questions.append(q3)
form.questions.append(q4)
form.save()

sform = StoreForm()
sform.forms.append(form)
sform.forms.append(form)
sform.forms.append(form)
sform.store_json()
