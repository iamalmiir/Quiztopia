import requests
from dotenv import load_dotenv
from os import getenv

load_dotenv()
url = "https://ases-quiz-api1.p.rapidapi.com/questions/random/20"
headers = {
    "X-RapidAPI-Key": getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": getenv("X-RapidAPI-Host"),
}


class Question:
    def __init__(self):
        self.questions = list()

    def get_questions(self):
        questions_list = requests.request("GET", url, headers=headers)
        self.questions = questions_list.json()
        return self.questions["questions"]

    def validate_answer(correct_answer, user_answer):
        if correct_answer == user_answer:
            return True
        else:
            return False
