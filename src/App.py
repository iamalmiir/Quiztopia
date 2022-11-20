from src.Quiz import QuizGame


class App(QuizGame):
    def __init__(self):
        super().__init__()

    def start(self):
        self.set_up_quiz()
        # self.get_questions()
        self.start_quiz()
