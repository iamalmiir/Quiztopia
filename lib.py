from os import system, name as os_name


class Helper:
    def clear(self):
        if os_name == "nt":
            system("cls")
        else:
            system("clear")
