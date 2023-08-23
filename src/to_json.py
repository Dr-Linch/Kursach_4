from src.to_json_abstract import ToJsonAbstract
import os
import json

path = os.path.join("database", "database.json")


class ToJson(ToJsonAbstract):

    """
        Класс для добавления вакансий в файл
    """

    def add_to_file(self, data):

        if not os.path.isdir("database"):
            os.mkdir("database")
        with open(path, "w") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)


