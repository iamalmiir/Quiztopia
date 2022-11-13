from colorama import init, Fore, Back, Style
from lib import colorize
import requests
from questions import Question
from dotenv import load_dotenv
from os import getenv

load_dotenv()
init(autoreset=True)
url = "https://ases-quiz-api1.p.rapidapi.com/questions/random/20"

headers = {
    "X-RapidAPI-Key": getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": getenv("X-RapidAPI-Host"),
}

quiz = Question()
quiz.get_questions()

for question in quiz.questions["questions"]:
    print(question["text"])
    question_option = 1
    correct_answer = str()
    for option in question["options"]:
        print(Fore.CYAN + f"{question_option}. {option['option']}")
        if option["isCorrect"]:
            correct_answer = question_option - 1
        question_option += 1
    while True:
        print("Enter your answer (1-4):")
        print(correct_answer)
        user_answer = int(input(Fore.CYAN + ":> "))
        if question["options"][user_answer - 1]["isCorrect"]:
            print(
                Fore.GREEN
                + f"You are correct! The answer is: {question['options'][correct_answer]['option']}"
            )
            break
        else:
            break
