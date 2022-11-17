from os import system, name as os_name


def clear():
    if os_name == "nt":
        system("cls")
    else:
        system("clear")
