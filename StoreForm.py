import json
from Interfaces.IStoreJson import IStoreJson


class StoreForm(IStoreJson):

    def __init__(self):
        self.forms = []
        pass

    def store_json(self):
        with open('/home/mars/Projects/python/DynamicForm/files/Forms.json', 'w') as file:
            file.write(self.forms_to_json())

    def forms_to_json(self):
        return json.dumps(self.forms, default=lambda o: o.__dict__, indent=2, sort_keys=True)
