from abc import ABC, abstractmethod


class IStoreJson(ABC):
    @abstractmethod
    def store_json(self):
        pass
