from colorama import init

from questions import App

init(autoreset=True)

if __name__ == "__main__":
    try:
        app = App()
        app.start()
    except KeyboardInterrupt:
        print("\nBye!")
