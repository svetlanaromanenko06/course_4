from utils.user import user_interaction

def main():
    print('Привет!\n'
          'Я помогу подобрать нужные Вам вакансии с платформ:\n'
          '"Headhunter.ru" и "Superjob.ru"')
    print()

    # Вызов функции взаимодействия с пользователем
    user_interaction()


if __name__ == '__main__':
    main()