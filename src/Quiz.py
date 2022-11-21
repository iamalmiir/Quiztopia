from time import sleep

from colorama import Fore, init

from src.SetupQuiz import SetupQuiz
from src.ProcessAnswers import ProcessAnswers
from src.lib import clear

init(autoreset=True)


class QuizGame(SetupQuiz):
    def __init__(self):
        super().__init__()
        # Set the category picked by the user
        self.category = self.set_category()
        # Fetch the questions from the API with choosen category
        self.questions = self.get_questions(self.category)

        # Game variables
        self.score = 0
        self.total_score = 0
        self.correct_answer = int()
        self.answered_correctly = 0
        self.answered_incorrectly = 0

    def start_quiz(self):
        clear()
        answer = ProcessAnswers()
        print(Fore.CYAN + "Welcome to the quiz game!")
        for question in self.questions:
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

                    answer.set_values(question, user_answer, self.correct_answer, self.score)
                    if answer.is_correct():
                        self.score += answer.points_earned
                        self.answered_correctly += 1
                        answer.correct_answer_message()
                    else:
                        self.answered_incorrectly += 1
                        answer.incorrect_answer_message()
                    self.total_score += answer.points_earned
                    sleep(2)
                    clear()
                    break
                except ValueError:
                    print(Fore.YELLOW + "Invalid answer. Please enter a number between 1 and 4")
                    continue

        print(
            Fore.GREEN
            + f"You have answered {self.answered_correctly} questions correctly"
            + Fore.CYAN
            + " & "
            + Fore.RED
            + f"{self.answered_incorrectly} questions incorrectly."
        )
        print("\n-------------------------------------------------------------------\n")
        print(
            Fore.CYAN
            + f"You have earned {self.score} points out of {self.total_score} possible points."
        )
