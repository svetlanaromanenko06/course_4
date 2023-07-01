import json
from src.vacancies import Vacancy

class JsonSaver:
    """Работа с файлом json"""

    @staticmethod
    def write_json(filename, vacancies):
        """Запись вакансий в файл json"""

        with open(filename, 'w', encoding='utf-8') as file:
            json_file = []

            # Создаем словарь, который запишется в файл
            for vacancy in vacancies:
                vacancies_dict = {'name': vacancy.name,
                                  'salary_min': vacancy.salary_from,
                                  'salary_max': vacancy.salary_to,
                                  'experience': vacancy.experience,
                                  'area': vacancy.area,
                                  'vacancy_url': vacancy.vacancy_url
                                  }

                json_file.append(vacancies_dict)
            file.write(json.dumps(json_file, sort_keys=False, indent=2, ensure_ascii=False))

    @staticmethod
    def load_from_file(filename):
        """Чтение вакансий из файл json"""

        with open(filename, 'r', encoding='UTF-8') as file:
            json_data = file.read()
            data = json.loads(json_data)

        vacancies = []

        for i in data:
            name = i["name"]
            salary_from = i["salary_min"]
            salary_to = i["salary_max"]
            experience = i["experience"]
            area = i["area"]
            vacancy_url = i["vacancy_url"]

            # Создаем экземпляр класса Vacancy
            vacancy = Vacancy(
                name,
                salary_from,
                salary_to,
                experience,
                area,
                vacancy_url
            )
            vacancies.append(vacancy)

        return vacancies

    @staticmethod
    def sort_by_max_salary(vacancies):
        '''Сортировка вакансий по наибольшей зарплате

        salary_sorted = sorted(vacancies,
                                 key=lambda
                                 vacancy: vacancy.salary_to if vacancy.salary_to != 0 else vacancy.salary_from,
                                 reverse=True)'''
        salary_sorted = sorted(vacancies,
                               key=lambda
                                   vacancy: vacancy.salary_from,
                               reverse=True)
        return salary_sorted

