from abc import ABC, abstractmethod

class ToJsonAbstract(ABC):

    """
          Абстрактный класс для добавления вакансий в файл
    """

    @abstractmethod
    def add_to_file(self, data):
        pass
