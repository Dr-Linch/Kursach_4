from src.API_abstract import APIAbstract
import os
import requests
from src.config import SuperJob_key


class APISuperJob(APIAbstract):
    """Класс для получения вакансий с SuperJob"""

    def get_page(self, vacancy_name):
        url = "https://api.superjob.ru/2.0/vacancies/"
        params = {"keywords": vacancy_name,
                  "page": 0,
                  "count": 100,
                  'no_agreement': 1}
        headers = {"X-Api-App-Id": SuperJob_key}
        response = requests.get(url, params, headers=headers)
        response_data = response.json()
        vacancies = response_data["objects"]
        while params["page"] != 2:
            params["page"] += 1
            response = requests.get(url, params, headers=headers)
            response_data = response.json()
            vacancies.extend(response_data["objects"])

        return vacancies
