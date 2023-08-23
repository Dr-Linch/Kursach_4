from datetime import datetime
from src.API_hh import APIHeadHanter
from src.API_sj import APISuperJob
from src.Vacancy import Vacancy

# Создание экземпляров классов для работы с платформами по поиску работы
hh_api = APIHeadHanter()
sj_api = APISuperJob()


def search_by_name(search):
    """
    Функция для поиска и парсинга данных с сайтов
    """

    hh_vacancies = hh_api.get_page(search)
    # Создаем экземпляры класса найденных вакансий с HH
    Vacancy.vacancies_from_hh(hh_vacancies)

    sj_vacancies = sj_api.get_page(search)
    # Создаем экземпляры класса найденных вакансий с SJ
    Vacancy.vacancies_from_sj(sj_vacancies)

    # Получаем массив со всеми отсортированными данными
    load_vacancies = Vacancy.all_vacancies
    vacancies_data = []

    # Преобразуем найденные экземпляры классов в словарь
    for vacancy in load_vacancies:
        vacancies_data.append(vacancy.__dict__)

    # Преобразуем дату для сортировки
    for vacancy in vacancies_data:
        vacancy['published'] = datetime.strptime(vacancy['published'], "%d.%m.%Y %H:%M")

    # Сортируем по дате размещения вакансий
    sort_vacancies_data = sorted(vacancies_data,
                                 key=lambda x: x.get('published'),
                                 reverse=False)

    # Преобразуем дату к привычному виду
    for vacancy in vacancies_data:
        vacancy['published'] = datetime.strftime(vacancy['published'], "%d.%m.%Y %H:%M")

    return sort_vacancies_data


def format_salary(data):
    """
    Функция для форматирования зарплаты
    """
    for vacancy in data:
        if vacancy.get("salary_from") is None:
            vacancy["salary_from"] = 0
        elif vacancy.get("salary_to") is None:
            vacancy["salary_to"] = ''


def view_vacancies(data):
    """
    Функция для отображения вакансий
    """
    for vacancy in data:
        format_salary(data)
        print(f"Дата публикации: {vacancy['published']}\n"
              f"Вакансия: {vacancy['vacancy_name']}\n"
              f"Зарплата: {vacancy['salary_from']} - {vacancy['salary_to']}\n"
              f"Требования: {vacancy['requirement']}\n"
              f"Ссылка на вакансию: {vacancy['url']}\n"
              f"--------------------------------------\n")


def sorted_by_salary(data):
    """
    Функция сортировки вакансий по заработной плате от самой наивысшей
    """
    format_salary(data)
    sort_vacancies_data = sorted(
        data,
        key=lambda x: x["salary_from"],
        reverse=False
    )
    return sort_vacancies_data
