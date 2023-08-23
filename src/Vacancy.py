import datetime


class Vacancy:
    """
    Класс для работы с вакансиями
    """

    all_vacancies = []

    def __init__(self, vacancy_name, salary_from, requirement, url, published):
        self.vacancy_name = vacancy_name
        self.salary_from = salary_from
        self.requirement = requirement
        self.url = url
        self.published = published

    @classmethod
    def vacancies_from_hh(cls, list):
        """
        Метод создания экземпляров класса с данными из HeadHunter
        """

        for vacancy in list:
            cls.all_vacancies.append(Vacancy
                                     (vacancy_name=vacancy["name"],
                                      salary_from=vacancy["salary"]["from"],
                                      requirement=vacancy["snippet"]["requirement"],
                                      url=vacancy["alternate_url"],
                                      published=datetime.datetime.fromisoformat(vacancy['published_at']).strftime(
                                      "%d.%m.%Y %H:%M")))

    @classmethod
    def vacancies_from_sj(cls, list):
        """Метод для создания экземпляров классов вакансий с данными из SuperJob"""

        for vacancy in list:
            cls.all_vacancies.append(Vacancy
                                     (vacancy_name=vacancy['profession'],
                                      salary_from=vacancy['payment_from'],
                                      requirement=vacancy['candidat'],
                                      url=vacancy['link'],
                                      published=datetime.datetime.fromtimestamp(vacancy['date_published']).strftime(
                                          "%d.%m.%Y %H:%M")))
