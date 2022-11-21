from src.constants import HEADERS
from requests import request


class Questions:
    def __init__(self) -> None:
        self.all_questions: list = list()

    def get_questions(self, category: str) -> list:
        url: str = f"https://ases-quiz-api1.p.rapidapi.com/questions/random/category/{category}"
        self.all_questions = request("GET", url, headers=HEADERS).json()
        return self.all_questions["questions"]
