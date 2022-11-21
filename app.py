from src.App import App
from src.lib import clear

if __name__ == "__main__":
    try:
        clear()
        app: App = App()
        app.start()
    except KeyboardInterrupt:
        clear()
        print("Thanks for playing!")
        exit()
