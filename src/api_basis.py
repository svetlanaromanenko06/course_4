from abc import ABC, abstractmethod

class ApiBasis(ABC):
    '''Абстрактный класс для работы с платформами через Api'''

    def __init__(self):
        self.api_url = None

    @abstractmethod
    def get_vacancies(self):
        '''Возвращает список вакансий'''



