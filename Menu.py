import pdb
from Form import *


class Menu:
    def __init__(self):
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
            self.fill_form()
        elif option == 3:
            print(option)
        return

    def add_form(self):
        print('Nuevo Formulario')
        print('Nombre: ', end='')
        name = input()
        form = Form(name)
        opt = ''
        while opt != '0':
            print(f'[1] Agregar pregunta [2] Guardar formulario [0] Salir')
            opt = input()
            if opt == '1':
                self.select_type(form)
            elif opt == '2':
                form.save()
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
                if question_type == 3:
                    print('Ejm: Opcion 1-Opcion 2-Opcion 3 SEPARAR CON {}'.format("'-'"))
                    new_question = Question(question, question_type)
                    new_question.options = input().split('-')
                    form.questions.append(new_question)
                else:
                    form.questions.append(Question(question, question_type))

    def show_forms(self):
        print('Lista de formularios')
        if len(Form.get_all()) > 0:
            for num, form in enumerate(Form.get_all()):
                print('Form [{}]\nNombre: {}'.format(num + 1, form['name']))
                for num_q, question in enumerate(form['questions']):
                    print('{}.{} Tipo: {}'.format(num_q + 1, question['question'], question['question_type']['name']))
        else:
            print('No hay formularios.')
            return

    def fill_form(self):
        self.show_forms()
        if len(Form.get_all()) > 0:
            print('Opcion: ', end='')
            opt = int(input())
            form = Form.get_all()[opt - 1]
            pdb.set_trace()


m = Menu()
option = ''
while '0' != option:
    m.print()
    option = input()
    m.choose_option(option)
