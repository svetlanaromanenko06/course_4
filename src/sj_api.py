import requests
import os

from src.api_basis import ApiBasis
from src.vacancies import Vacancy


class ApiSuperjob(ApiBasis):
    '''
    Класс для работы с ресурсом SuperJob.ru, наследующийся от абстрактного класса
    '''

    def __init__(self):
        self.api_key = os.getenv('SJ_API_KEY')
        self.headers = {'X-Api-App-Id': self.api_key}
        self.api_url = 'https://api.superjob.ru/2.0/vacancies/'
        self.keyword = None
        self.count = 50
    def get_vacancies(self):
        '''Возвращает список вакансий'''

        vacancies = []
        params = {"keyword": self.keyword, "count": self.count}

        sj_response = requests.get(self.api_url, params, headers=self.headers)

        if sj_response.status_code == 200:
            data = sj_response.json()

            # Перебор вакансий по параметрам
            for item in data['objects']:
                name = item['profession']
                salary_from = item['payment_from']
                salary_to = item['payment_to']
                experience = item['experience']['title']
                area = item['town']['title']
                vacancy_url = item['link']

                # Создаем экземпляр класса - Vacancies
                vacancy = Vacancy(
                    name,
                    salary_from,
                    salary_to,
                    experience,
                    area,
                    vacancy_url
                )

                # Добавляем вакансию в список
                vacancies.append(vacancy)

            return vacancies

        else:
            print(f'Ошибка подключения к серверу - {sj_response.status_code}')

