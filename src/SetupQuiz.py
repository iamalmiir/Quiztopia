from os import getenv

from colorama import Fore


class SetupQuiz:
    def __init__(self) -> None:
        self.categories_count = 1
        self.categories = {
            "Sport": getenv("SPORT_ID"),
            "Art & Literature": getenv("ART_AND_LITERATURE_ID"),
            "Geography": getenv("GEOGRAPHY_ID"),
            "General Knowledge": getenv("GENERAL_KNOWLEDGE_ID"),
            "History": getenv("HISTORY_ID"),
            "Science & Nature": getenv("SCIENCE_AND_NATURE_ID"),
        }

    def main(self):
        print("Please pick one of the following categories:")
        for category in self.categories:
            print(Fore.CYAN + f"{self.categories_count}. {category}")
            self.categories_count += 1

        user_pick = int(input(Fore.CYAN + ":> ")) - 1
        if user_pick < 0 or user_pick > 5:
            raise ValueError

        print("You have selected: " + Fore.GREEN + f"{list(self.categories.keys())[user_pick]}")
        self.categories = list(self.categories.values())[user_pick]
