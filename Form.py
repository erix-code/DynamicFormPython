from Question import *
from StoreForm import StoreForm

store_form = StoreForm()


class Form:
    def __init__(self, name):
        self.questions = []
        self.name = name

    def save(self, option=('json', 'xml')):
        store_form.forms.append(self)
        store_form.store_json()

    @staticmethod
    def get_all():
        return store_form.forms


# form = Form('My form')
# form.save()
