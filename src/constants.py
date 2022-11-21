from os import getenv

from dotenv import load_dotenv

load_dotenv()


headers = {
    "X-RapidAPI-Key": getenv("X-RapidAPI-Key"),
    "X-RapidAPI-Host": getenv("X-RapidAPI-Host"),
}

CATEGORIES = {
    "Sport": getenv("SPORT_ID"),
    "Art & Literature": getenv("ART_AND_LITERATURE_ID"),
    "Geography": getenv("GEOGRAPHY_ID"),
    "General Knowledge": getenv("GENERAL_KNOWLEDGE_ID"),
    "History": getenv("HISTORY_ID"),
    "Science & Nature": getenv("SCIENCE_AND_NATURE_ID"),
}
