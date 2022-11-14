import requests
from colorama import Fore
from dotenv import load_dotenv
from lib import Helper
from os import getenv
from time import sleep

load_dotenv()
url = "https://ases-quiz-api1.p.rapidapi.com/questions/random/20"
headers = {
    "X-RapidAPI-Key": getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": getenv("X-RapidAPI-Host"),
}

helper = Helper()


class QuizGame:
    def __init__(self):
        self.questions = list()
        self.correct_answer = int()
        self.score = 0

    def get_questions(self):
        questions_list = requests.request("GET", url, headers=headers)
        self.questions = questions_list.json()
        return self.questions["questions"]

    def validate_answer(self, question, answer):
        if question["options"][answer]["isCorrect"]:
            print(
                Fore.GREEN
                + f"You are correct! The answer is: {question['options'][self.correct_answer]['option']}"
            )
        else:
            print(
                Fore.RED
                + f"Wrong answer! The correct answer is: {Fore.GREEN + question['options'][self.correct_answer]['option']}"
            )

    def start_quiz(self):
        for question in self.questions["questions"]:
            print(question["text"])
            question_option = 1

            for option in question["options"]:
                print(Fore.CYAN + f"{question_option}. {option['option']}")
                if option["isCorrect"]:
                    self.correct_answer = question_option - 1
                question_option += 1

            print("Enter your answer (1-4)")
            while True:
                try:
                    user_answer = int(input(Fore.CYAN + ":> ")) - 1
                    if user_answer < 0 or user_answer > 3:
                        raise ValueError

                    self.validate_answer(question, user_answer)
                    sleep(4)
                    helper.clear()
                    break
                except ValueError:
                    print(Fore.YELLOW + "Invalid answer. Please enter a number between 1 and 4")
                    continue
