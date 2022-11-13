from colorama import init, Fore, Back, Style

init()

# Create decorator to print in color
def colorize(color):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(color, end="")
            func(*args, **kwargs)
            print(Style.RESET_ALL, end="")

        return wrapper

    return decorator
