from Answer import Answer
from services.CompletedFormService import CompletedFormService
from services.FormService import FormService

from Form import Form
from TextQuestion import TextQuestion
from NumberQuestion import NumberQuestion
from DropdownQuestion import DropdownQuestion
from DateQuestion import DateQuestion
from QuestionType import *
from CompletedForm import CompletedForm


class Menu:
    def __init__(self):
        """Starting the menu and fetching the forms in the service"""
        # Recovering the data
        self.completed_form_service = CompletedFormService()
        self.completed_form_service.fetch()
        self.form_service = FormService()
        self.form_service.fetch()

        self.title = 'Dynamic Forms'
        self.options = [
            'Nuevo formulario',
            'Lista de formularios',
            'Responder formulario',
            'Lista de respuestas',
            'Salir'
        ]

    def print(self):
        text = '{}\n'.format(self.title)
        for num, option in enumerate(self.options):
            if len(self.options) == num + 1:
                text += f'[0] {option}\n'
            else:
                text += f'[{num + 1}] {option}\n'
        print(text)

    def choose_option(self, option):
        option = int(option)
        option -= 1
        if option == 0:
            self.add_form()
        elif option == 1:
            self.show_forms()
        elif option == 2:
            self.complete_form()
        elif option == 3:
            self.show_completed_forms()
        return

    def add_form(self):
        print('Nuevo Formulario')
        print('Nombre: ', end='')
        name = input()
        new_form = Form(name)
        opt = ''
        while opt != '0':
            print(f'[1] Agregar pregunta [2] Guardar formulario [0] Salir')
            opt = input()
            if opt == '1':
                self.select_type(new_form)
            elif opt == '2':
                self.form_service.forms.append(new_form)
                self.form_service.store()
                break

    def select_type(self, form: Form):
        text = ''
        for num, q_type in enumerate(question_types):
            text += '[{}] {} '.format(num + 1, q_type.name)
        text += '[0] Salir'
        question_type = ''
        while question_type != 0:
            print(text)
            question_type = int(input())
            if 0 < question_type <= len(question_types):
                print('[{}] Pregunta: '.format(question_types[question_type - 1].name), end='')
                question = input()
                if question_type == 1:
                    form.questions.append(TextQuestion(question))
                elif question_type == 2:
                    form.questions.append(NumberQuestion(question))
                elif question_type == 3:
                    print('Ejm: Opcion 1-Opcion 2-Opcion 3 SEPARAR CON {}'.format("'-'"))
                    options = input().split('-')
                    new_question = DropdownQuestion(question, options)
                    form.questions.append(new_question)
                else:
                    form.questions.append(DateQuestion(question))

    def show_forms(self):
        print('Lista de formularios')
        try:
            if len(self.form_service.fetch()) > 0:
                for num, form in enumerate(self.form_service.fetch()):
                    print('Form [{}]\nNombre: {}'.format(num + 1, form.name))
                    for num_q, question in enumerate(form.questions):
                        print('{}.{} Tipo: {}'.format(num_q + 1, question.question, question.type))
            else:
                print('No hay formularios.')
                return
        except Exception as e:
            print('No hay formularios.')
            return

    def complete_form(self):
        self.show_forms()
        if len(self.form_service.fetch()) > 0:
            print('Opcion: ', end='')
            opt = int(input())
            form = self.form_service.forms[opt - 1]
            print(f'Selecionaste: {form.name}')
            completed_form = CompletedForm(form)
            answers = []
            for question in form.questions:
                print(question.question)
                if question.type == 'DATE':
                    print('Formato: %Y-%m-%d')
                if hasattr(question, 'options'):
                    [print(f'[{num}] {opt} ', end=' ') for num, opt in enumerate(question.options)]
                    print()
                answer = input()
                while not question.validate(answer):
                    answer = input()
                answers.append(Answer(answer))
            completed_form.answers = answers
            self.completed_form_service.completed_forms.append(completed_form)
            self.completed_form_service.store()

    def show_completed_forms(self):
        print('Lista de respuestas')
        try:
            if len(self.completed_form_service.fetch()) > 0:
                for num, form in enumerate(self.completed_form_service.fetch()):
                    print('Respuesta [{}]'.format(num + 1))
                    print(form.form.name)
                    index = 0
                    for num_q, question in enumerate(form.form.questions):
                        print('{}.{} Tipo: {}'.format(num_q + 1, question.question, question.type))
                        print(f"Respuesta: {form.answers[index].answer}")
                        index += 1
            else:
                print('No hay respuestas.')
                return
        except Exception as e:
            print('No hay respuestas.')
            return

m = Menu()
option = ''
while '0' != option:
    m.print()
    option = input()
    m.choose_option(option)
