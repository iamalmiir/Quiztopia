from colorama import init

from questions import QuizGame

init(autoreset=True)

if __name__ == "__main__":
    try:
        quiz = QuizGame()
        quiz.get_questions()
        quiz.start_quiz()
    except KeyboardInterrupt:
        print("\nBye!")
