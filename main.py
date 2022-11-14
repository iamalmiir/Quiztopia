from colorama import init
from questions import QuizGame
from dotenv import load_dotenv
from os import getenv

load_dotenv()
init(autoreset=True)
url = "https://ases-quiz-api1.p.rapidapi.com/questions/random/20"

headers = {
    "X-RapidAPI-Key": getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": getenv("X-RapidAPI-Host"),
}


if __name__ == "__main__":
    quiz = QuizGame()
    quiz.get_questions()
    quiz.start_quiz()
