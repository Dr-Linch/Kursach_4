from abc import ABC, abstractmethod


class APIAbstract(ABC):

    """
    Абстрактный класс для рабты с API
    """

    @abstractmethod
    def get_page(self, vacancy_name):
        pass
