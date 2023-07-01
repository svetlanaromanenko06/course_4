from src.json_saver import JsonSaver
from src.hh_api import ApiHH
from src.sj_api import ApiSuperjob
from src.json_saver import JsonSaver


def user_interaction():
    ''' Функция, для взаимодействия с пользователем.'''

    filename = 'src/selected_vacancies.json'
    saver = JsonSaver()

    while True:
        platform = input('Выберите платформу для поиска вакансий:\n'
                             '1 - Headhunter.ru\n'
                             '2 - Superjob.ru\n'
                             '3 - выбрать обе платформы\n'
                             )
        keyword = input('Введите ключевое слово для поиска вакансии:\n')
        top_vacancies = int(input('"Введите количество вакансий, загружаемых с одной платформы:\n'))
        search_word = f'{keyword}'
        print()

        if platform == '1':
            hh_api = ApiHH()
            hh_api.keyword = search_word
            hh_api.per_page = top_vacancies
            vacancies_ = hh_api.get_vacancies()
            saver.write_json(filename, vacancies_)
            break

        elif platform == '2':
            sj_api = ApiSuperjob()
            sj_api.keyword = search_word
            sj_api.count = top_vacancies
            vacancies_ = sj_api.get_vacancies()
            saver.write_json(filename, vacancies_)
            break

        elif platform == '3':
            hh_api = ApiHH()
            hh_api.keyword = search_word
            hh_api.per_page = top_vacancies
            vacancies_ = hh_api.get_vacancies()

            sj_api = ApiSuperjob()
            sj_api.keyword = search_word
            sj_api.count = top_vacancies
            sj_vacancies = sj_api.get_vacancies()
            vacancies_.extend(sj_vacancies)

            saver.write_json(filename, vacancies_)
            break

        else:
            print('Вы ввели некорректный номер!\n'
                      'Будьте внимательны! (Необходимо ввести "1", "2" или "3")\n'
                      )
            continue

    print(f'Загружено {len(vacancies_)} вакансий')

    while True:
        user_answer = input('Выберите вариант вывода на экран загруженных вакансий:\n'
                                '1 - Показать все загруженные вакансии\n'
                                '2 - Показать все вакансии, отсортированные по зарплате\n'
                                )
        print()

        if user_answer == '1':
            vacancies_ = saver.load_from_file(filename)
            for i in vacancies_:
                print(i.vacancy_info())
                print()
            break

        elif user_answer == '2':
            vacancies = saver.load_from_file(filename)
            sorted_vacancies = saver.sort_by_max_salary(vacancies)
            for i in sorted_vacancies:
                print(i.vacancy_info())
                print()
            break

        else:
            print('Вы ввели некорректный номер\n'
                      'Повторите ввод снова.\n'
                      )
            continue


