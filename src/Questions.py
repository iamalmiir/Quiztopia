from os import getenv

from dotenv import load_dotenv
from requests import request

load_dotenv()
headers = {
    "X-RapidAPI-Key": getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": getenv("X-RapidAPI-Host"),
}


class Questions:
    def __init__(self) -> None:
        self.all_questions = list()

    def get_questions(self, category) -> list:
        url = f"https://ases-quiz-api1.p.rapidapi.com/questions/random/category/{category}"
        questions_list = request("GET", url, headers=headers)
        self.all_questions = questions_list.json()
        return self.all_questions["questions"]
