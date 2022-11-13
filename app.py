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


class StartPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.create_label("Quzzler", 0, 0, 100, 50, 54, justify="center", fg=self.YELLOW)
        self.create_label("Levels", 1, 0, 100, 50, 24, justify="center")
        space_between_buttons = 150
        for level in ["Easy", "Medium", "Hard"]:
            self.create_button(
                text=level,
                x=space_between_buttons,
                y=280,
                font_size=8,
                command=lambda: self.quit(),
                fg=level == "Easy"
                and self.SUCCESS_COLOR
                or level == "Medium"
                and self.YELLOW
                or self.DANGER_COLOR,
            )
            space_between_buttons += 150

        self.create_label("Categories", 2, 0, 100, 50, 24, justify="center")


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = StartPage(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        # b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        # b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        # b1.pack(side="left")
        # b2.pack(side="left")
        # b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    MAIN_WINDOW_SIZE = "1200x700"
    root = tk.Tk()
    root.title("Quizzler")
    root.geometry(MAIN_WINDOW_SIZE)
    root.resizable(False, False)
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry(MAIN_WINDOW_SIZE)
    root.mainloop()
