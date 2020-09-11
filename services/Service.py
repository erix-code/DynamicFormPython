from abc import ABC, abstractmethod


class Service(ABC):
    def __init__(self):
        self.url = '/home/mars/Projects/python/DynamicForm/files/'
        self.file = None
        pass

    @abstractmethod
    def fetch(self):
        pass

    @abstractmethod
    def store(self):
        pass
