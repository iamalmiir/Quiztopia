from src.Quiz import QuizGame


class App(QuizGame):
    def __init__(self):
        super().__init__()

    def start(self):
        self.start_quiz()
