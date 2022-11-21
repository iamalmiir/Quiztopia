from colorama import Fore

from src.Questions import Questions
from src.constants import CATEGORIES


class SetupQuiz(Questions):
    def __init__(self):
        super().__init__()
        self.categories = CATEGORIES

    def set_category(self) -> str:
        print("Please pick one of the following categories:")
        categories_count = 1
        for category in self.categories:
            print(Fore.CYAN + f"{categories_count}. {category}")
            categories_count += 1

        user_pick = int(input(Fore.CYAN + ":> ")) - 1
        if user_pick < 0 or user_pick > 5:
            raise ValueError

        print("You have selected: " + Fore.GREEN + f"{list(self.categories.keys())[user_pick]}")
        return list(self.categories.values())[user_pick]
