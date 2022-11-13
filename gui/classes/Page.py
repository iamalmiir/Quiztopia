import tkinter as tk
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Page(tk.Frame):
    MAIN_WINDOW_SIZE = "1200x700"
    SUCCESS_COLOR = "#00FF00"
    YELLOW = "#fee440"
    DANGER_COLOR = "#E94560"
    BG_COLOR = "#000814"
    ACTIVE_BG_COLOR = "#22223b"
    FG_COLOR = "#4cc9f0"
    TITLE_FONT = "Varino"
    CATEGORIES = [
        "Sport",
        "Art and Literature",
        "Geography",
        "History",
        "Science and Nature",
        "General Knowledge",
    ]
    CATEGORY = {
        "sport": getenv("SPORT_ID"),
        "art&literature": getenv("ART_AND_LITERATURE_ID"),
        "geography": getenv("GEOGRAPHY_ID"),
        "history": getenv("HISTORY_ID"),
        "science&nature": getenv("SCIENCE_AND_NATURE_ID"),
        "general knowledge": getenv("GENERAL_KNOWLEDGE_ID"),
    }

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.configure(bg=self.BG_COLOR)

    def create_label(
        self,
        text,
        row,
        col,
        padx,
        pady,
        font_size,
        bd=0,
        relief=None,
        justify=None,
        fg=FG_COLOR,
    ):

        label = tk.Label(
            self,
            text=text,
            font=(self.TITLE_FONT, font_size),
            foreground=fg,
            bd=bd,
            relief=relief,
            justify=justify,
            background=self.BG_COLOR,
        )
        label.grid(row=row, column=col, padx=padx, pady=pady)
        return label

    def create_button(self, text, x, y, font_size, command, bd=0, fg=FG_COLOR):
        button = tk.Button(
            self,
            text=text,
            font=(self.TITLE_FONT, font_size),
            foreground=fg,
            background=self.BG_COLOR,
            highlightbackground=self.FG_COLOR,
            highlightthickness=2,
            bd=bd,
            command=command,
            activebackground=self.ACTIVE_BG_COLOR,
            activeforeground=fg,
        )
        button.place(x=x, y=y)
        return button

    def show_frame(self):
        self.tkraise()

    def show(self):
        self.lift()
