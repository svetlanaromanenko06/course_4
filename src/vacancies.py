class Vacancy:
    '''
    Класс для работы с вакансиями
    :param name: Название вакансии
    :param salary_from: Заработная плата от
    :param salary_to: Заработная плата до
    :param experience: Опыт работы
    :param vacancy_url: Ссылка на вакансию
    :param area: Название региона
    '''

    def __init__(self, name, salary_from, salary_to, experience, area, vacancy_url):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.experience = experience
        self.area = area
        self.vacancy_url = vacancy_url


    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'name: {self.name}, salary_from: {self.salary_from}, salary_to: {self.salary_to},  ' \
               f'experience: {self.experience}, area: {self.area},' \
               f' vacancy_url: {self.vacancy_url} '

    def vacancy_info(self):
        """Возвращает данные о вакансии"""

        return f'Вакансия:{self.name}\nЗаработная плата от: {self.salary_from}\n' \
               f'Заработная плата до: {self.salary_to}\n' \
               f'Опыт работы: {self.experience}\nГород: {self.area}\n' \
               f'Ссылка на вакансию: {self.vacancy_url}'

