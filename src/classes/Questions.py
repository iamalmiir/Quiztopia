from src.constants import HEADERS
from requests import request


class Questions:
    def __init__(self) -> None:
        self.all_questions = list()

    def get_questions(self, category) -> list:
        url = f"https://ases-quiz-api1.p.rapidapi.com/questions/random/category/{category}"
        self.all_questions = request("GET", url, headers=HEADERS).json()
        return self.all_questions["questions"]
