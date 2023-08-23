from src.API_abstract import APIAbstract
import requests


class APIHeadHanter(APIAbstract):

    """
    Класс для получения вакансий с hh
    """

    def get_page(self, vacancy_name):

        params = {
            'text': f'NAME:{vacancy_name}',
            'area': 1,
            'page': 0,
            'per_page': 100,
            'only_with_salary': True}

        response = requests.get("https://api.hh.ru/vacancies", params)
        response_data = response.json()
        vacancies = response_data["items"]

        while response_data["page"] != 2:
            params["page"] += 1
            response = requests.get("https://api.hh.ru/vacancies", params)
            response_data = response.json()
            vacancies.extend(response_data["items"])

        return vacancies
