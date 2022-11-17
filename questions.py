from os import getenv
from time import sleep

import requests
from colorama import Fore
from dotenv import load_dotenv

from lib import clear

load_dotenv()
url = "https://ases-quiz-api1.p.rapidapi.com/questions/random/20"
headers = {
    "X-RapidAPI-Key": getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": getenv("X-RapidAPI-Host"),
}


class QuizGame:
    def __init__(self):
        self.questions = list()
        self.correct_answer = 0
        self.score = 0
        self.total_score = 0
        self.answered_correctly = 0
        self.answered_incorrectly = 0
        self.levels_points = {
            "Easy": 1,
            "Medium": 2,
            "Hard": 3,
        }
        self.categories = {
            "Sport": getenv("SPORT_ID"),
            "Art & Literature": getenv("ART_AND_LITERATURE_ID"),
            "Geography": getenv("63357abb3ab81af9ad154eb0"),
            "General Knowledge": getenv("GENERAL_KNOWLEDGE_ID"),
            "History": getenv("HISTORY_ID"),
            "Science & Nature": getenv("SCIENCE_AND_NATURE_ID"),
        }

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
            self.score += self.levels_points.get(question["difficulty"]["degree"])
            self.answered_correctly += 1
            print(
                Fore.GREEN
                + f"You have earned {self.levels_points.get(question['difficulty']['degree'])} points"
            )
            print(Fore.CYAN + f"Your current score is: {self.score}")
        else:
            self.answered_incorrectly += 1
            print(
                Fore.RED
                + f"Wrong answer! The correct answer is: {Fore.GREEN + question['options'][self.correct_answer]['option']}"
            )
        self.total_score += self.levels_points.get(question["difficulty"]["degree"])

    def set_up_quiz(self):
        categories_count = 1
        print("Please pick one of the following categories:")
        for category in self.categories:
            print(Fore.CYAN + f"{categories_count}. {category}")
            categories_count += 1
        user_pick = int(input(Fore.CYAN + ":> ")) - 1
        if user_pick < 0 or user_pick > 5:
            raise ValueError

        self.categories = list(self.categories.values())[user_pick]

    def start_quiz(self):
        clear()
        # self.set_up_quiz()
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
                    sleep(2)
                    clear()
                    break
                except ValueError:
                    print(Fore.YELLOW + "Invalid answer. Please enter a number between 1 and 4")
                    continue

        print(Fore.GREEN + f"You answered {self.answered_correctly} questions correctly")
        print(Fore.RED + f"You answered {self.answered_incorrectly} questions incorrectly")
        print(Fore.CYAN + f"Your final score is: {self.score}/{self.total_score}")


class App(QuizGame):
    def __init__(self):
        super().__init__()

    def start(self):
        self.set_up_quiz()
        self.get_questions()
        self.start_quiz()
