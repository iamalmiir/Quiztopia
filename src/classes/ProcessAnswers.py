from colorama import Fore


class ProcessAnswers:
    def __init__(self) -> None:
        self.current_answer: int = int()
        self.correct_answer: int = int()
        self.points_earned: int = int()
        self.current_score: int = int()
        self.current_question: dict = dict()
        self.level_points: dict = {
            "Easy": 1,
            "Medium": 2,
            "Hard": 3,
        }

    def set_values(
            self, current_question: dict, current_answer: int, correct_answer: int, current_score: int
    ) -> None:
        self.current_question = current_question
        self.current_answer = current_answer
        self.correct_answer = correct_answer
        self.points_earned = self.level_points.get(current_question["difficulty"]["degree"])
        self.current_score = current_score

    def is_correct(self) -> bool:
        if self.current_question["options"][self.current_answer]["isCorrect"]:
            self.current_score += self.points_earned
            return True
        else:
            return False

    def correct_answer_message(self) -> None:
        print(
            Fore.GREEN
            + f"The correct answer is: {self.current_question['options'][self.correct_answer]['option']}"
        )
        print(Fore.YELLOW + f"You have earned {self.points_earned} points.")
        print(Fore.CYAN + f"Your current score is: {self.current_score}")

    def incorrect_answer_message(self) -> None:
        print(Fore.RED + f"The correct answer is: ", end="")
        print(Fore.GREEN + f"{self.current_question['options'][self.correct_answer]['option']}")

        print(Fore.CYAN + f"Your current score is: {self.current_score}")
