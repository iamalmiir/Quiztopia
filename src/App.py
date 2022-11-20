from src.Quiz import QuizGame
from src.SetupQuiz import SetupQuiz


class App(QuizGame):
    def __init__(self):
        super().__init__()

    def start(self):
        quiz_setup = SetupQuiz()
        quiz_setup.main()
        self.start_quiz()
