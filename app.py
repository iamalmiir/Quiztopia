from src.App import App

if __name__ == "__main__":
    try:
        app = App()
        app.start()
    except KeyboardInterrupt:
        print("\nBye!")
