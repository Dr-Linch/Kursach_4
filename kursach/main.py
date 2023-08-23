from src.to_json import ToJson
from utils.function import search_by_name, view_vacancies, sorted_by_salary

json_saver = ToJson()


def main():

    search = input("Введите название вакансии для поиска: ")

    searched_vacancies = search_by_name(search)

    print(
        f"Найдено {len(searched_vacancies)} вакансий, повторите ваш запрос или введите цифру "
        f"exit для завершения программы")
    while len(searched_vacancies) == 0:
        search = input("Введите название вакансии для поиска: ")
        if search == "exit":
            print("Программа завершена...")
            exit()

        searched_vacancies = search_by_name(search)
        print(f"Найдено {len(searched_vacancies)} вакансий")

    while True:
        user_answer = input(f"Выберите действие (введите номер):\n"
                            f"1 - показать найденные вакансии:\n"
                            f"2 - показать топ-10 вакансий по зарплатам: \n")

        if user_answer == "1":
            view_vacancies(searched_vacancies)
            user_answer = input(f"Выберите действие (введите номер):\n"
                                f"1 - отсортировать по зарплате:\n"
                                f"2 - сохранить \n")
            if user_answer == "1":
                view_vacancies(sorted_by_salary(searched_vacancies))
                user_answer = input(f"Выберите действие (введите номер):\n"
                                    f"1 - сохранить \n")
                if user_answer == "1":
                    json_saver.add_to_file(sorted_by_salary(searched_vacancies))
                    print(f"Данные сохранены! Программа завершена...")
                    break
            elif user_answer == "2":
                json_saver.add_to_file(searched_vacancies)
                print(f"Данные сохранены! Программа завершена...")
                break

        elif user_answer == "2":
            sort_result = sorted_by_salary(searched_vacancies)
            view_vacancies(sort_result[-10:])
            user_answer = input(f"Выберите действие (введите номер):\n"
                                f"1 - сохранить\n")

            if user_answer == "1":
                json_saver.add_to_file(sort_result[-10:])
                print(f"Данные сохранены! Программа завершена...")

                break

            else:
                print('Выбрано недопустимое действие, введите правильный номер действия\n')

    if __name__ == "__main__":
        main()
